import json

from .user import User
from .organization import Organization
from .classroom import Classroom
from .activity import Activity
from .user import User, Teacher
from .timeline import Timeline

def import_data_from_file(file_path: str):
    with open(file_path, "r", encoding="UTF-8") as f:
        json_data = json.load(f)
    temp_organization = Organization()
    temp_organization.import_data(json_data)
    return temp_organization

def export_data_to_file(file_path: str, organization: Organization):
    with open(file_path, "w", encoding="UTF-8") as f:
        json.dump(organization.export_data(), f, indent=4, ensure_ascii=False)