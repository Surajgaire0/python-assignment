import urllib.parse

import boto3

from env import QueueUrl

s3_client = boto3.client("s3")

sqs_client = boto3.client("sqs")


def lambda_handler(event, context):
    bucket = event["Records"][0]["s3"]["bucket"]["name"]
    key = urllib.parse.unquote_plus(event["Records"][0]["s3"]["object"]["key"], encoding="utf-8")

    sqs_client.send_message(
        QueueUrl=QueueUrl, MessageBody=f"File {key} uplaoded to bucket {bucket}"
    )

    print(QueueUrl)
    print(f"File {key} uplaoded to bucket {bucket}")

    return {"success": 1}
