import boto3
import json
from .. import settings

ses_client = boto3.client("ses", aws_access_key_id=settings.ACCESS_KEY, aws_secret_access_key=settings.SECRET_KEY)


def create_template(template: str) -> None:
    ses_client.create_template(
        Template={
            "TemplateName": "awscc_template",
            "SubjectPart": "Starting Subject",
            "TextPart": "",
            "HtmlPart": template,
        }
    )


def update_template(template: str, subject: str) -> None:
    ses_client.update_template(
        Template={
            "TemplateName": "awscc_template",
            "SubjectPart": subject,
            "TextPart": "",
            "HtmlPart": template,
        }
    )


def send_ses(data: dict) -> None:
    ses_client.send_templated_email(
        Source=settings.EMAIL,
        Destination={
            "ToAddresses": [data["EMAIL"]],  # data["EMAIL"]
            "BccAddresses": [settings.EMAIL],
        },
        Template="awscc_template",
        TemplateData=json.dumps(data),
    )
