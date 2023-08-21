from csv import DictReader


def read_csv(file_path: str) -> list[dict]:
    contents = None
    with open(file_path, encoding="utf8") as file:
        contents = list(DictReader(file, delimiter=","))
    return contents


def read_template(file_path):
    template = None
    with open(file_path, "r", encoding="latin-1") as file:
        template = "".join(file.readlines())
    return template
