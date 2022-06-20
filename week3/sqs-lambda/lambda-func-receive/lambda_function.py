import boto3

from env import QueueUrl

sqs_client = boto3.client("sqs")


def lambda_handler(event, context):
    messages = sqs_client.receive_message(
        QueueUrl=QueueUrl,
        MaxNumberOfMessages=10,
    )

    for message in messages["Messages"]:
        print(f"Id={message['MessageId']} Body={message['Body']}")

    return {"status": 200, "body": "message polled successfully"}
