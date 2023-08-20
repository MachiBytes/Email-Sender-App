from csv import DictReader


def read_csv(file_path: str) -> list[dict]:
    contents = None
    with open(file_path, encoding="utf8") as file:
        contents = list(DictReader(file, delimiter=","))
    return contents
