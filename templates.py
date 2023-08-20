from pathlib import Path


def get_html_templates() -> dict:
    base_dir = Path(__file__).parent
    interview_templates_dir = base_dir / "AWSCC_Email_Templates" / "office_interview_acceptance" / "interview"
    templates = {
        "Creatives Office": None,
        "Marketing Office": None,
        "Relations Office": None,
        "Operations Office": None,
    }

    with open(interview_templates_dir / "creatives_interview.html", "r", encoding="latin-1") as file:
        templates["Creatives Office"] = "".join(file.readlines())
    with open(interview_templates_dir / "relations_interview.html", "r") as file:
        templates["Relations Office"] = "".join(file.readlines())
    with open(interview_templates_dir / "marketing_interview.html", "r") as file:
        templates["Marketing Office"] = "".join(file.readlines())
    with open(interview_templates_dir / "operations_interview.html", "r") as file:
        templates["Operations Office"] = "".join(file.readlines())

    return templates
