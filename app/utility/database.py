import random
import boto3
from boto3.dynamodb.conditions import Key

session = boto3.Session(profile_name="awscc-backend", region_name="ap-southeast-1")
dynamodb = session.resource("dynamodb")
table = dynamodb.Table("awscc_members")


def get_nickname(email: str) -> str:
    response = table.query(IndexName="email-index", KeyConditionExpression=Key("email").eq(email))
    return random.choice(response["Items"][0]["nicknames"])


if __name__ == "__main__":
    print(get_nickname("markachilesflores2004@gmail.com"))
