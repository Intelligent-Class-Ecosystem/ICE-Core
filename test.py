"""import json
with open("data/organization.json","r",encoding="UTF-8") as f: json_data = json.load(f)
from app.models.organization import Organization
org = Organization()
org.import_data(json_data)
new_json = org.export_data()
with open("data/organization.json","w",encoding="UTF-8") as f: json.dump(new_json, f, indent=4, ensure_ascii=False)
"""
import pprint
import app.models as models
org = models.import_data_from_file("data/organization.json")
pprint.pprint(org.export_data())
