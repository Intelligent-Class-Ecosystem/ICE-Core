import json
# from .organization import Organization
# from .classroom import Classroom

class User:
    def __init__(self):
        self.name = "未命名用户"
        self.id = 0
    
    def import_from_path(self, path: str):
        with open(path, "r", encoding="utf-8") as f:
            json_data: dict = json.load(f)
        self.name = json_data.get("name", self.name)
        self.id = json_data.get("id", self.id)

    def import_from_json(self, json_data: dict):
        self.name = json_data.get("name", self.name)
        self.id = json_data.get("id", self.id)

class Teacher(User):
    def __init__(self):
        super().__init__()
        
class Student(User):
    def __init__(self):
        super().__init__()