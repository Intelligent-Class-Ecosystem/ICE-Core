from .user import Teacher

class Activity:
    def __init__(self):
        self.id: str = ""
        self.name: str = ""
        self.description: str = ""
        self.teachers: list[Teacher] = []
        
    def import_data(self, json_data: dict, organization_teachers: list[Teacher]):
        
        # 基本信息
        self.id = json_data.get("id", self.id)
        self.name = json_data.get("name", self.name)
        self.description = json_data.get("description", self.description)
        
        # 从组织提供的教师列表中找到该活动需要的教师并添加进去，并在末项已被找到时停止
        for required_teacher_id in list(json_data.get("teachers_id", [])):
            for now_teacher in organization_teachers:
                if required_teacher_id == now_teacher.id:
                    self.teachers.append(now_teacher)
                    if list(json_data.get("teachers_id", []))[-1] == now_teacher.id:
                        break

    def export_data(self):
        return {
            "id": self.id,
            "name": self.name,  
            "description": self.description,
            "teachers_id": [teacher.id for teacher in self.teachers]
        }
