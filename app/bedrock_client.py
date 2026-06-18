import boto3
from botocore.exceptions import ClientError

MODEL_ID = "amazon.nova-lite-v1:0"
REGION = "us-west-2"


def ask_bedrock(user_message):
    try:
        client = boto3.client("bedrock-runtime", region_name=REGION)

        response = client.converse(
            modelId=MODEL_ID,
            messages=[
                {
                    "role": "user",
                    "content": [{"text": user_message}]
                }
            ],
            inferenceConfig={
                "maxTokens": 300,
                "temperature": 0.5
            }
        )

        return response["output"]["message"]["content"][0]["text"]

    except ClientError as error:
        return f"Bedrock error: {error.response['Error']['Message']}"