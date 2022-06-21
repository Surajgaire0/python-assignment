import json

import boto3


def client(service, aws_access_key_id, aws_secret_access_key, **kwargs):
    return boto3.client(
        service,
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        **kwargs,
    )


def create_bucket(client, bucket_name):
    response = client.create_bucket(Bucket=bucket_name)
    return response


def upload_to_bucket(client, file, bucket, key):
    response = client.upload_file(file, bucket, key)
    return response


def create_lambda(client, params: dict):
    lambda_func = client.create_function(**params)
    lambda_arn = lambda_func["FunctionArn"]
    return lambda_arn


def add_permission(client, lambda_arn, source_arn, **kwargs):
    client.add_permission(
        FunctionName=lambda_arn,
        SourceArn=source_arn,
        **kwargs,
    )


def create_sns_topic(client, name):
    return client.create_topic(Name=name)["TopicArn"]


def create_sns_subscription(client, topic_arn, protocol, endpoint):
    return client.subscribe(
        TopicArn=topic_arn, Protocol=protocol, Endpoint=endpoint, ReturnSubscriptionArn=True
    )["SubscriptionArn"]


def set_sns_topic_policy(client, topic_arn, bucket_name):
    policy = {
        "Id": "Policy1655807977975",
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "Stmt1655807970487",
                "Action": ["sns:Publish"],
                "Effect": "Allow",
                "Resource": topic_arn,
                "Condition": {"ArnEquals": {"aws:SourceArn": f"arn:aws:s3:::{bucket_name}"}},
                "Principal": "*",
            }
        ],
    }
    client.set_topic_attributes(
        TopicArn=topic_arn,
        AttributeName="Policy",
        AttributeValue=json.dumps(policy),
    )


def add_bucket_notification_config(client, bucket_name, NotificationConfiguration):
    client.put_bucket_notification_configuration(
        Bucket=bucket_name, NotificationConfiguration=NotificationConfiguration
    )


def main():
    with open("config.json", "r") as f:
        config = json.load(f)

    s3_client = client("s3", **config["credentials"], verify=False)
    lambda_client = client("lambda", **config["credentials"], verify=False)
    sns_client = client("sns", **config["credentials"], verify=False)

    # create bucket
    create_bucket(s3_client, bucket_name=config["s3_bucket"]["name"])

    # add zipfile for lambda function
    upload_to_bucket(
        s3_client, config["lambda_zipfile"], *config["lambda_func_params"]["Code"].values()
    )

    # create lambda func
    lambda_arn = create_lambda(lambda_client, config["lambda_func_params"])

    # create sns topic
    topic_arn = create_sns_topic(sns_client, config["sns"]["topic"]["Name"])
    # print(topic_arn)

    # creating 2 subscriptions--1 email and 1 lambda
    email = input("Enter your email to subscribe: ")
    create_sns_subscription(sns_client, topic_arn, "email", email)

    create_sns_subscription(sns_client, topic_arn, "lambda", lambda_arn)

    set_sns_topic_policy(sns_client, topic_arn, bucket_name=config["s3_bucket"]["name"])

    add_bucket_notification_config(
        s3_client,
        bucket_name=config["s3_bucket"]["name"],
        NotificationConfiguration={
            "TopicConfigurations": [
                {
                    "TopicArn": topic_arn,
                    "Events": config["trigger"]["notification"]["Events"],
                }
            ]
        },
    )


if __name__ == "__main__":
    main()
