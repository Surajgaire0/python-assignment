import json
import time

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


def lambda_add_permission(client, lambda_arn, source_arn, **kwargs):
    client.add_permission(
        FunctionName=lambda_arn,
        SourceArn=source_arn,
        **kwargs,
    )


def setup_rule(client, Name, ScheduleExpression, State, Targets):
    """create eventbridge rule and add target"""
    client.put_rule(Name=Name, ScheduleExpression=ScheduleExpression, State=State)
    client.put_targets(Rule=Name, Targets=Targets)


def main():
    with open("config.json", "r") as f:
        config = json.load(f)

    s3_client = client("s3", **config["credentials"], verify=False)
    lambda_client = client("lambda", **config["credentials"], verify=False)
    event_client = client("events", **config["credentials"], verify=False)

    # create bucket
    create_bucket(s3_client, bucket_name=config["s3_bucket"]["name"])

    # add zipfile for lambda function 1
    upload_to_bucket(
        s3_client, config["lambda_1_zipfile"], *config["lambda_func_1_params"]["Code"].values()
    )

    # add zipfile for lambda function 2
    upload_to_bucket(
        s3_client, config["lambda_2_zipfile"], *config["lambda_func_2_params"]["Code"].values()
    )

    # create lambda func 1 (to send to sqs)
    arn_lambda_send = create_lambda(lambda_client, config["lambda_func_1_params"])

    # create lambda function to poll
    arn_lambda_receive = create_lambda(lambda_client, config["lambda_func_2_params"])

    lambda_add_permission(
        lambda_client,
        arn_lambda_send,
        f"arn:aws:s3:::{config['s3_bucket']['name']}",
        **config["trigger"]["permissions_sendfunc"],
    )

    # setup events rule
    setup_rule(
        event_client,
        Targets=[{"Arn": arn_lambda_receive, "Id": "1"}],
        **config["event_rule"],
    )

    lambda_add_permission(
        lambda_client,
        arn_lambda_receive,
        f"arn:aws:events:{config['credentials']['region_name']}:{config['iam_user_id']}:rule/{config['event_rule']['Name']}",  # sourceArn
        **config["trigger"]["permissions_pollfunc"],
    )

    time.sleep(1)

    s3_client.put_bucket_notification_configuration(
        Bucket=config["s3_bucket"]["name"],
        NotificationConfiguration={
            "LambdaFunctionConfigurations": [
                {
                    "LambdaFunctionArn": arn_lambda_send,
                    "Events": config["trigger"]["notification"]["Events"],
                }
            ]
        },
    )


if __name__ == "__main__":
    main()
