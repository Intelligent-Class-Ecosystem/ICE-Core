import json
import time

from .user import User
from .organization import Organization
from .classroom import Classroom
from .activity import Activity
from .user import User, Teacher
from .timeline import Timeline
from .timetable import TimeTable

def import_data_from_file(file_path: str):
    with open(file_path, "r", encoding="UTF-8") as f:
        json_data = json.load(f)
    temp_organization = Organization()
    temp_organization.import_data(json_data)
    return temp_organization

def export_data_to_file(file_path: str, organization: Organization):
    with open(file_path, "w", encoding="UTF-8") as f:
        json.dump(organization.export_data(), f, indent=4, ensure_ascii=False)

def default_description(creating_type: str) -> str:
    now_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    return "用户在 " + now_str + " 创建的" + creating_type

def teacher(name: str,
            description: str = default_description("教师")):
    teacher = Teacher()
    teacher.name = name
    teacher.description = description
    teacher.check_id()
    return teacher

def activity(name: str,
             notice_level: int, 
             teachers: list[Teacher],
             description: str = default_description("活动")
             ):
    activity = Activity()
    activity.name = name
    activity.description = description
    activity.notice_level = notice_level
    activity.teachers = teachers
    activity.check_id()
    return activity

def organization(name: str, description: str = default_description("组织")):
    org = Organization()
    org.name, org.description = name, description
    return org
    