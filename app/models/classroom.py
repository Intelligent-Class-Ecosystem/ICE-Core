from .user import Teacher
from .timeline import Timeline
from .activity import Activity
from .class_id_calculate_function import generate_id_by_non_id_fields


class TimeTable:
    def __init__(self):
        self.id = ""
        self.name = "未命名时间表"
        self.description = ""
        self.timeline: Timeline = Timeline()
        self.teachers: list[Teacher] = []
        self.activities: list[Activity] = []

    def import_data(self,
                    json_data: dict,
                    organization_timelines: list[Timeline],
                    organization_teachers: list[Teacher],
                    organization_activities: list[Activity]):

        # 基本信息
        self.name = json_data.get("name", self.name)
        self.id = json_data.get("id", self.id)
        self.description = json_data.get("description", self.description)

        # 时间线
        for now_timeline in organization_timelines:
            if json_data.get("timeline_id", "") == now_timeline.id:
                self.timeline = now_timeline
                break
        
        # 从组织提供的教师列表中找到该活动需要的教师并添加进去，并在末项已被找到时停止
        for required_teacher_id in list(json_data.get("teachers_id", [])):
            for now_teacher in organization_teachers:
                if required_teacher_id == now_teacher.id:
                    self.teachers.append(now_teacher)
                    if list(json_data.get("teachers_id", []))[-1] == now_teacher.id:
                        break
        
        # 从组织提供的活动列表找到需要的活动并添加，并在末项找到时停止
        for required_activity_id in list(json_data.get("activities_id", [])):
            for now_activity in organization_activities:
                if required_activity_id == now_activity.id:
                    self.activities.append(now_activity)
                    if list(json_data.get("activities_id", []))[-1] == now_activity.id:
                        break
        
        temp_id = generate_id_by_non_id_fields(self)
        if temp_id != self.id:
            self.id = temp_id

    def export_data(self):
        return {
            "name": self.name,
            "id": self.id,
            "description": self.description,
            "timeline_id": self.timeline.id,
            "activities_id": [activity.id for activity in self.activities],
            "teachers_id": [teacher.id for teacher in self.teachers]
        }

class Classroom:
    def __init__(self):
        self.id = ""
        self.name = "未命名教室"
        self.description = ""
        self.timetables: list[TimeTable] = []

    def import_data(self,
                    json_data: dict,
                    organization_timelines: list[Timeline],
                    organization_teachers: list[Teacher],
                    organization_activities: list[Activity]):

        # 基本信息
        self.name = json_data.get("name", self.name)
        self.id = json_data.get("id", self.id)
        self.description = json_data.get("description", self.description)

        # 时间表
        for timetable_dict in list(json_data.get("timetables", [])):
            temp_timetable = TimeTable()
            temp_timetable.import_data(timetable_dict, organization_timelines, organization_teachers, organization_activities)
            self.timetables.append(temp_timetable)

        temp_id = generate_id_by_non_id_fields(self)
        if temp_id != self.id:
            self.id = temp_id

    def export_data(self):
        return {
            "name": self.name,
            "id": self.id,
            "description": self.description,
            "timetables": [timetable.export_data() for timetable in self.timetables]
        }
        


    