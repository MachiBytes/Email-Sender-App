from read_csv import read_csv
from templates import get_html_templates
from send_ses import send_ses, update_template
from database import get_nickname
from time import sleep


def get_office():
    while True:
        print("What office will we be working on?")
        print("\t[C]reatives Office")
        print("\t[M]arketing Office")
        print("\t[R]elations Office")
        print("\t[O]perations Office")
        office = input(">>> ").lower()
        if office in list("cmro"):
            return office
        print()
        print("Incorrect input, please choose from [C/M/R/O]")


if __name__ == "__main__":
    # Offices
    offices = {
        "Operations Office": "operations.csv",
        "Operations Office": "relations.csv",
        "Operations Office": "marketing.csv",
        "Operations Office": "creatives.csv",
    }

    office = get_office()

    # Subjects
    subjects = {
        "Creatives Office": "AWS Cloud Club - PUP Manila | Creatives Office: Get Ready to Shine!",
        "Operations Office": "AWS Cloud Club - PUP Manila | Operations Office: Let's Execute This!",
        "Marketing Office": "AWS Cloud Club - PUP Manila | Marketing Office: Get Ready to Make Waves!",
        "Relations Office": "AWS Cloud Club - PUP Manila | Relations Office: Let's Connect!",
    }

    # Read CSV
    data = read_csv(f"applicants_database/{offices[office]}")

    # Get templates
    templates = get_html_templates()

    # Loop through data
    for index, record in enumerate(data):
        name = record["Full Name"]
        print(f"Processing {name}, please wait...", end=" | ")
        try:
            nickname = get_nickname(name)
        except Exception as e:
            print(name, e)

        template_data = {"NAME": nickname, "TIME": record["Time"], "DATE": record["Date"]}

        update_template(templates[office], subjects[office])

        # Send email
        send_ses(template_data, [record["Personal Email"]])
        print(f"Processing done!")
        sleep(0.1)
