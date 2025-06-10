import json
# from .organization import Organization
from .user import User, Teacher, Student

class Classroom:
    def __init__(self):
        self.name = "未命名教室"
        self.id = 0
        self.teachers = []

    def import_from_path(self, path: str):
        with open(path, "r", encoding="utf-8") as f:
            json_data: dict = json.load(f)
        self.name = json_data.get("name", self.name)
        self.id = json_data.get("id", self.id)
        self.teachers = []  # 确保每次导入时清空教师列表
        for i in list(json_data.get("teachers", [])):
            teacher = Teacher()  # 创建教师实例并传入组织
            teacher.import_from_path(dict(i).get("path", ""))  # 导入教师信息
            self.teachers.append(teacher)  # 将教师添加到教室的教师列表中

    def import_from_json(self, json_data: dict):
        self.name = json_data.get("name", self.name)
        self.id = json_data.get("id", self.id)
        self.teachers = []  # 确保每次导入时清空教师列表
        for i in list(json_data.get("teachers", [])):
            teacher = Teacher()  # 创建教师实例并传入组织
            teacher.import_from_path(dict(i).get("path", ""))  # 导入教师信息
            self.teachers.append(teacher)  # 将教师添加到教室的教师列表中