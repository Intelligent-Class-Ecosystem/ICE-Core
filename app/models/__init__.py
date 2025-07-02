import json
import time

from .organization_model import Organization
from .classroom_model import Classroom
from .activity_model import Activity
from .user_model import User, Teacher
from .timeline_model import Timeline, Duration
from .timetable_model import TimeTable

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

def duration(start_timestamp: int = -1,
            end_timestamp: int = -1,
            duration_timestamp: int = -1,
            start_time: list[int] = [-1,-1],
            end_time: list[int] = [-1,-1],
            duration_time: list[int] = [-1,-1]):
    d = Duration()
    d.set_duration(start_timestamp,end_timestamp,duration_timestamp,start_time,end_time,duration_time)
    return d

def timeline(name: str,
             durations: list[Duration],
             description: str = default_description("时间线")):
    tl = Timeline()
    tl.name, tl.description = name, description
    tl.durations = durations
    tl.check_id()
    return tl
    
def ordered_timetable(name: str,
                      timeline: Timeline,
                      teachers: list[Teacher],
                      activities: list[Activity],
                      period: int,
                      description: str = default_description("既定时间表")):
    ott = TimeTable()
    ott.operation = False
    ott.name, ott.description = name, description
    ott.timeline, ott.teachers, ott.activities = timeline, teachers, activities
    ott.period = period
    ott.check_id()
    return ott

def operation_timetable(name: str,
                        timeline: Timeline,
                        teachers: list[Teacher],
                        activities: list[Activity],
                        date: list[int],
                        description: str = default_description("既定时间表")):
    ott = TimeTable()
    ott.operation = True
    ott.name, ott.description = name, description
    ott.timeline, ott.teachers, ott.activities = timeline, teachers, activities
    ott.date = date
    ott.check_date()
    ott.check_id()
    return ott

def classroom(name: str,
              description: str = default_description("教室")):
    clsrm = Classroom()
    clsrm.name, clsrm.description = name, description
    clsrm.check_id()
    return clsrm
    
def organization(name: str, description: str = default_description("组织")):
    org = Organization()
    org.name, org.description = name, description
    org.check_id()
    return org
    