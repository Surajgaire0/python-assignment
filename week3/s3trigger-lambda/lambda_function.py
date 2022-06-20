import datetime
import urllib.parse

import boto3

s3_client = boto3.client("s3")


def lambda_handler(event, context):
    bucket = event["Records"][0]["s3"]["bucket"]["name"]
    key = urllib.parse.unquote_plus(event["Records"][0]["s3"]["object"]["key"], encoding="utf-8")

    if not key.startswith("destination/"):
        file = s3_client.get_object(Bucket=bucket, Key=key)
        lines = file["Body"].read().decode("utf-8").split("\n")

        s3_client.put_object(
            Body="\n".join(
                [datetime.datetime.now().isoformat() + "," + line for line in lines if line]
            ),
            Bucket=bucket,
            Key="destination/" + key,
        )

    return {"success": 1}
