from database import get_nickname


def check_inputs(data: list[dict]) -> None:
    for record in data:
        name = record["Full Name"]
        try:
            get_nickname(name)
        except Exception as e:
            print(name, e)
