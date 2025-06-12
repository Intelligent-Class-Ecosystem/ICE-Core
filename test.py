import json
with open("data/organization.json","r",encoding="UTF-8") as f: json_data = json.load(f)
from app.models.organization import Organization
org = Organization()
org.import_data(json_data)