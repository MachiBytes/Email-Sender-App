import boto3
import json

ses_client = boto3.client("ses")


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


def send_ses(data: dict, recipient: list[str]) -> None:
    ses_client.send_templated_email(
        Source="awscloudclub.pupmnl@gmail.com",
        Destination={
            "ToAddresses": recipient,
            "BccAddresses": ["markachilesflores2004@gmail.com", "awscloudclub.pupmnl@gmail.com"],
        },
        Template="awscc_template",
        TemplateData=json.dumps(data),
    )
