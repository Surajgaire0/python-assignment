import json
import time

import boto3


def setup_bucket(config):
    """create bucket and add zipfile containing lambda function code"""

    s3_client = boto3.client("s3", **config["credentials"], verify=False)
    s3_client.create_bucket(Bucket=config["lambda_func_params"]["Code"]["S3Bucket"])
    s3_client.upload_file(config["lambda_zipfile"], *config["lambda_func_params"]["Code"].values())
    return s3_client


def create_lambda(config):
    client = boto3.client(
        "lambda",
        **config["credentials"]
        # verify=False,
    )
    lambda_func = client.create_function(**config["lambda_func_params"])
    lambda_arn = lambda_func["FunctionArn"]
    client.add_permission(
        FunctionName=lambda_arn,
        SourceArn=f"arn:aws:s3:::{config['s3_bucket']['name']}",
        **config["trigger"]["permissions"],
    )
    return client, lambda_arn


def main():
    with open("config.json", "r") as f:
        config = json.load(f)

    s3_client = setup_bucket(config)

    _, lambda_arn = create_lambda(config)

    time.sleep(1)

    s3_client.put_bucket_notification_configuration(
        Bucket=config["s3_bucket"]["name"],
        NotificationConfiguration={
            "LambdaFunctionConfigurations": [
                {
                    "LambdaFunctionArn": lambda_arn,
                    "Events": config["trigger"]["notification"]["Events"],
                }
            ]
        },
    )


if __name__ == "__main__":
    main()
