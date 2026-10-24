import os

from botocore.exceptions import (
    BotoCoreError,
    LoginTokenLoadError,
)
from dotenv import load_dotenv
from strands import Agent, tool
from strands.models import BedrockModel


def aws_connection_test():
    try:
        import boto3
        sts = boto3.client("sts", region_name="us-east-1")
        identity = sts.get_caller_identity()
        print("Connected to AWS")
        print("Account:", identity["Account"])
        print("Identity:", identity["Arn"])
    except BotoCoreError as error:
        print("AWS SDK or connection error:", error)
        raise
    except LoginTokenLoadError as error:
        print(error)
        raise
    except Exception as e:
        print(e)
        raise

def run_strands_agent():
    try: 
        load_dotenv()
        
        @tool
        def count_words(text: str) -> int:
            """Count whitespace-separated words in the provided text."""
            return len(text.split())


        model = BedrockModel(
            model_id=os.environ["BEDROCK_MODEL_ID"],
            region_name=os.environ["AWS_REGION"],
        )

        agent = Agent(
            model=model,
            system_prompt=(
                "You are a helpful assistant. "
                "Use the count_words tool when asked to count words."
            ),
            tools=[count_words],
        )

        agent('How many words are in this text: "Strands makes building agents easy"?')

    except KeyError as e:
        print(e)


def main():
    try:
        aws_connection_test()
        print("Hello from strands-bedrock-starter!")
        run_strands_agent()
    except Exception as e:
        print(e)
        raise

if __name__ == "__main__":
    main()
