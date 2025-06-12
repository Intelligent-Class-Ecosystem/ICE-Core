from .user import Teacher
from .activity import Activity
from .timeline import Timeline
from .classroom import Classroom

class Organization:
    def __init__(self):
        self.id = ""
        self.name = ""
        self.description = ""
        self.teachers: list[Teacher] = []
        self.activities: list[Activity] = []
        self.timelines: list[Timeline] = []
        self.classrooms: list[Classroom] = []

    def import_data(self, json_data: dict):

        # 导入基本信息
        self.id = json_data.get("id", self.id)
        self.name = json_data.get("name", self.name)
        self.description = json_data.get("description", self.description)

        # 导入教师
        for teacher_data in list(json_data.get("teachers", [])):
            temp_teacher = Teacher()
            temp_teacher.import_data(teacher_data)
            self.teachers.append(temp_teacher)

        # 导入活动
        for activity_data in list(json_data.get("activities", [])):
            temp_activity = Activity()
            temp_activity.import_data(activity_data, self.teachers)
            self.activities.append(temp_activity)

        # 导入时间线
        for timeline_data in list(json_data.get("timelines", [])):
            temp_timeline = Timeline()
            temp_timeline.import_data(timeline_data)
            self.timelines.append(temp_timeline)
        
        # 导入教室
        for classroom_data in list(json_data.get("classrooms", [])):
            temp_classroom = Classroom()
            temp_classroom.import_data(classroom_data, self.timelines, self.teachers, self.activities)
            self.classrooms.append(temp_classroom)
        
    def export_data(self):
        return {
            "name": self.name,
            "id": self.id,
            "description": self.description,
            "teachers": [teacher.export_data() for teacher in self.teachers],
            "activities": [activity.export_data() for activity in self.activities],
            "timelines": [timeline.export_data() for timeline in self.timelines],
            "classrooms": [classroom.export_data() for classroom in self.classrooms]
        }
