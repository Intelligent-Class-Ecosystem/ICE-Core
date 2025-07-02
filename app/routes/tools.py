import os
import json

def import_config() -> dict:
    if os.path.exists("data/") == False:
        os.mkdir("data/")
    if os.path.exists("data/config.json") == False:
        with open("data/config.json", "w", encoding = "UTF-8") as f:
            json.dump({"organization_path": "organization.json"}, f, ensure_ascii = False)
    with open("data/config.json", "r", encoding = "UTF-8") as f:
        d = json.load(f)
    path = "data/" + d["organization_path"]
    if os.path.exists(path) == False:
        with open(path, encoding = "UTF-8") as f:
            json.dump({}, f, ensure_ascii = False)
    with open("data/config.json", "r", encoding = "UTF-8") as f:
        return json.load(f)