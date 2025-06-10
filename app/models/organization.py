import json
from .activity import Activity
from .user import Teacher, Student
from .classroom import Classroom

class Organization:
    def __init__(self):
        self.name = "未命名组织"
        self.id = 0
        self.description = "无"
        self.classrooms: list[Classroom] = []
        self.teachers: list[Teacher] = []
        self.students: list[Student] = []
        self.activities: list[Activity] = []

    def import_from_path(self, path: str):
        with open(path, "r", encoding="utf-8") as f:
            json_data: dict = json.load(f)
        self.name = json_data.get("name", self.name)
        self.description = json_data.get("description", self.description)
        self.classrooms = []
        for i in json_data.get("classrooms", []):
            classroom = Classroom()
            classroom.import_from_path(dict(i).get("path", ""))
            self.classrooms.append(classroom)
        self.teachers = []
        for i in json_data.get("teachers", []):
            teacher = Teacher()
            teacher.import_from_path(dict(i).get("path", ""))
            self.teachers.append(teacher)

    def import_from_json(self, json_data: dict):
        self.name = json_data.get("name", self.name)
        self.description = json_data.get("description", self.description)
        self.classrooms = []
        for i in json_data.get("classrooms", []):
            classroom = Classroom()
            classroom.import_from_path(dict(i).get("path", ""))
            self.classrooms.append(classroom)
        self.teachers = []
        for i in json_data.get("teachers", []):
            teacher = Teacher()
            teacher.import_from_path(dict(i).get("path", ""))
            self.teachers.append(teacher)
    