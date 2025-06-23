import time

from .user_model import Teacher
from .timeline_model import Timeline
from .activity_model import Activity
from .class_id_calculate_function import generate_id_by_non_id_fields


class TimeTable:
    def __init__(self):
        self.id = ""
        self.name = "未命名时间表"
        self.description = ""
        self.timeline: Timeline = Timeline()
        self.teachers: list[Teacher] = []
        self.activities: list[Activity] = []
        self.operation: bool = False
        self.period: int = 7    # 单位是天
        self.date: list[int] = [1900,1,1]

    def check_date(self):
        if len(self.date) != 3:
            raise ValueError("日期必须是一个3位数组。")
        dt = time.localtime()
        current_year, current_month, current_day = dt.tm_year + 1900, dt.tm_mon + 1, dt.tm_mday
        if self.date[0] < current_year:
            raise ValueError(f"无法设置一个今天 ({current_year}/{current_month}/{current_day}) 以前的日期。")
        if self.date[0] == current_year and self.date[1] < current_month:
            raise ValueError(f"无法设置一个今天 ({current_year}/{current_month}/{current_day}) 以前的日期。")
        if self.date[0] == current_year and self.date[1] == current_month and self.date[2] < current_day:
            raise ValueError(f"无法设置一个今天 ({current_year}/{current_month}/{current_day}) 以前的日期。")
        if (self.date[0] % 4 == 0 and self.date[0] % 100 != 0) or (self.date[0] % 100 == 0 and self.date[0] % 400 == 0):
            if self.date[1] == 2:
                if self.date[2] > 29:
                    raise ValueError("不存在的日期。")
        else:
            if self.date[1] == 2:
                if self.date[2] > 28:
                    raise ValueError("不存在的日期。")
        cd = [0, 31, 30, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if cd[self.date[1]] < self.date[2]: raise ValueError("不存在的日期。")   

    def import_data(self, json_data: dict,
                    organization_timelines: list[Timeline],
                    organization_teachers: list[Teacher],
                    organization_activities: list[Activity]):
        # 基本信息
        self.name = json_data.get("name", self.name)
        self.id = json_data.get("id", self.id)
        self.description = json_data.get("description", self.description)
        self.operation = json_data.get("operation", False)
        if self.operation == False:
            self.period = json_data.get("period", 7)
        else:
            self.date = list(json_data.get("date", self.date))
            self.check_date()
        # 时间线
        for now_timeline in organization_timelines:
            if json_data.get("timeline_id", "") == now_timeline.id:
                self.timeline = now_timeline; break
        # 从组织提供的教师列表中找到该活动需要的教师并添加进去，并在末项已被找到时停止
        for required_teacher_id in list(json_data.get("teachers_id", [])):
            for now_teacher in organization_teachers:
                if required_teacher_id == now_teacher.id:
                    self.teachers.append(now_teacher)
                    if list(json_data.get("teachers_id", []))[-1] == now_teacher.id: break
        # 从组织提供的活动列表找到需要的活动并添加，并在末项找到时停止
        for required_activity_id in list(json_data.get("activities_id", [])):
            for now_activity in organization_activities:
                if required_activity_id == now_activity.id:
                    self.activities.append(now_activity)
                    if list(json_data.get("activities_id", []))[-1] == now_activity.id: break
        temp_id = generate_id_by_non_id_fields(self)
        if temp_id != self.id: self.id = temp_id

    def check_id(self): self.id = generate_id_by_non_id_fields(self)

    def export_data(self):
        self.check_id()
        ret = {
            "name": self.name,
            "id": self.id,
            "description": self.description,
            "timeline_id": self.timeline.id,
            "activities_id": [activity.id for activity in self.activities],
            "teachers_id": [teacher.id for teacher in self.teachers],
            "operation": self.operation
        }
        ret.update(
            {
                "period": self.period
            } if self.operation == False else {
                "date": self.date
            }
        )
        return ret