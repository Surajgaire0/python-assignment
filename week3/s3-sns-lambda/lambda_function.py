import json

import boto3


def lambda_handler(event, context):
    message = json.loads(event["Records"][0]["Sns"]["Message"])
    key = message["Records"][0]["s3"]["object"]["key"]
    bucket = message["Records"][0]["s3"]["bucket"]["name"]

    print(f"{key} is uploaded to {bucket}")

    return {"success": 1}
