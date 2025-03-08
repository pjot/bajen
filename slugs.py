import json


DATA_FILE = "data/slugs.json"


def get() -> list[str]:
    try:
        with open(DATA_FILE) as f:
            slugs = json.load(f)
            return slugs
    except:
        return []


def store(slugs: list[str]):
    with open(DATA_FILE, "w") as f:
        json.dump(slugs, f, indent=4)
