import random
import requests


def get_id(email: str) -> str:
    api = f"https://fe80kk63kd.execute-api.ap-southeast-1.amazonaws.com/get_id/{email}"
    request = requests.get(url=api)
    clubId = request.json()["member"]

    if clubId == "None":
        print(f"{email} is not registered in the database.")

    return clubId


def get_nickname(email: str) -> str:
    clubId = get_id(email)
    if clubId == "None":
        return "AWStronaut"

    api = f"https://fe80kk63kd.execute-api.ap-southeast-1.amazonaws.com/members/{clubId}"
    request = requests.get(url=api)
    member = request.json()["member"]
    nickname = random.choice(member["nicknames"])
    return nickname


if __name__ == "__main__":
    print(get_nickname("machibytes@gmail.com"))
