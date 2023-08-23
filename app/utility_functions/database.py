import random
from pymongo import MongoClient


def get_nickname(name: str) -> str:
    # Start a connection with mongodb
    client = MongoClient("localhost", 27017)

    # Get cursor to the 'awscc' database and 'members' collection
    db = client.awscc
    members = db.members

    # Query the name from the database and return their corresponding nickname/s
    results: list[dict] = list(members.find({"fullName": name}, {"_id": False, "nickname": True}))
    nicknames: list[str] = results[0].get("nickname", ["applicant"])

    return random.choice(nicknames)


if __name__ == "__main__":
    print(get_nickname("Flores Jr., Mark Achiles G."))
