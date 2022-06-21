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
    client.add_permission(FunctionName=lambda_arn, SourceArn=source_arn, **kwargs)


def main():
    with open("config.json", "r") as f:
        config = json.load(f)

    s3_client = client("s3", **config["credentials"], verify=False)
    lambda_client = client("lambda", **config["credentials"], verify=False)

    # create bucket
    create_bucket(s3_client, bucket_name=config["s3_bucket"]["name"])

    # add zipfile for lambda function
    upload_to_bucket(
        s3_client, config["lambda_zipfile"], *config["lambda_func_params"]["Code"].values()
    )

    # create lambda func
    arn_lambda = create_lambda(lambda_client, config["lambda_func_params"])

    lambda_add_permission(
        lambda_client,
        arn_lambda,
        f"arn:aws:s3:::{config['s3_bucket']['name']}",
        **config["trigger"]["permissions"],
    )

    time.sleep(1)

    s3_client.put_bucket_notification_configuration(
        Bucket=config["s3_bucket"]["name"],
        NotificationConfiguration={
            "LambdaFunctionConfigurations": [
                {
                    "LambdaFunctionArn": arn_lambda,
                    "Events": config["trigger"]["notification"]["Events"],
                }
            ]
        },
    )


if __name__ == "__main__":
    main()
