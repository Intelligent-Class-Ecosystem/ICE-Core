from .user import Teacher
from .class_id_calculate_function import generate_id_by_non_id_fields

class Activity:
    def __init__(self):
        self.id: str = ""
        self.name: str = ""
        self.description: str = ""
        self.notice_level: int = 0
        self.teachers: list[Teacher] = []
        
    def import_data(self, json_data: dict, organization_teachers: list[Teacher]):
        
        # 基本信息
        self.id = json_data.get("id", self.id)
        self.name = json_data.get("name", self.name)
        self.description = json_data.get("description", self.description)
        self.notice_level = json_data.get("notice_level", self.notice_level)
        
        # 从组织提供的教师列表中找到该活动需要的教师并添加进去，并在末项已被找到时停止
        for required_teacher_id in list(json_data.get("teachers_id", [])):
            for now_teacher in organization_teachers:
                if required_teacher_id == now_teacher.id:
                    self.teachers.append(now_teacher)
                    if list(json_data.get("teachers_id", []))[-1] == now_teacher.id:
                        break
    
        temp_id = generate_id_by_non_id_fields(self)
        if temp_id != self.id:
            self.id = temp_id

    def check_id(self): self.id = generate_id_by_non_id_fields(self)

    def export_data(self):
        self.check_id()
        return {
            "id": self.id,
            "name": self.name,  
            "description": self.description,
            "notice_level": self.notice_level,
            "teachers_id": [teacher.id for teacher in self.teachers]
        }
