import json
import time
from .user_model import Teacher
from .activity_model import Activity
from .timeline_model import Timeline
from .classroom_model import Classroom
from .class_id_calculate_function import generate_id_by_non_id_fields

class Organization:
    def __init__(self):
        self.id = ""
        self.name = ""
        self.description = ""
        self.teachers: list[Teacher] = []
        self.activities: list[Activity] = []
        self.timelines: list[Timeline] = []
        self.classrooms: list[Classroom] = []
        self.last_update_time: int = 0

    def import_data(self, json_data: dict):

        # 导入基本信息
        self.id = json_data.get("id", self.id)
        self.name = json_data.get("name", self.name)
        self.description = json_data.get("description", self.description)
        self.last_update_time = json_data.get("last_update_time", self.last_update_time)

        # 导入教师
        for teacher_data in list(json_data.get("teachers", [])):
            temp_teacher = Teacher()
            temp_teacher.import_data(teacher_data)
            self.teachers.append(temp_teacher)
        self.teachers = list(tuple(self.teachers))

        # 导入活动
        for activity_data in list(json_data.get("activities", [])):
            temp_activity = Activity()
            temp_activity.import_data(activity_data, self.teachers)
            self.activities.append(temp_activity)
        self.activities = list(tuple(self.activities))

        # 导入时间线
        for timeline_data in list(json_data.get("timelines", [])):
            temp_timeline = Timeline()
            temp_timeline.import_data(timeline_data)
            self.timelines.append(temp_timeline)
        self.timelines = list(tuple(self.timelines))
        
        # 导入教室
        for classroom_data in list(json_data.get("classrooms", [])):
            temp_classroom = Classroom()
            temp_classroom.import_data(classroom_data, self.timelines, self.teachers, self.activities)
            self.classrooms.append(temp_classroom)
        self.classrooms = list(tuple(self.classrooms))
        
        # 计算并更新组织的ID
        temp_id = generate_id_by_non_id_fields(self)
        if temp_id != self.id:
            self.id = temp_id

    def check_id(self): 
        self.id = generate_id_by_non_id_fields(self)
        
    def export_data(self):
        update_time = int(time.time() / 1.00)
        self.last_update_time = update_time
        self.check_id()
        return {
            "name": self.name,
            "id": self.id,
            "description": self.description,
            "teachers": tuple([teacher.export_data() for teacher in self.teachers]),
            "activities": tuple([activity.export_data() for activity in self.activities]),
            "timelines": tuple([timeline.export_data() for timeline in self.timelines]),
            "classrooms": tuple([classroom.export_data() for classroom in self.classrooms]),
            "last_update_time": self.last_update_time
        }
    
    # 把某个老师的信息更新
    def update_teacher_data(self, old_teacher: Teacher, new_teacher: Teacher):
        # 其实我是不是只要获取旧的json文件然后把旧的都改掉就好了？
        old_teacher_id = old_teacher.id
        self.teachers.remove(old_teacher)
        self.teachers.append(new_teacher)
        str_data = json.dumps(self.export_data())
        str_data = str_data.replace(old_teacher_id, new_teacher.id)
        # 然后再导入
        self.activities.clear()
        self.classrooms.clear()
        self.timelines.clear()
        self.teachers.clear()
        print(json.loads(str_data))
        self.import_data(json.loads(str_data))
        
        
        
