from .class_id_calculate_function import generate_id_by_non_id_fields

class User:
    def __init__(self):
        self.name = "未命名用户"
        self.id = ""
        self.description = ""
        
    def import_data(self, json_data: dict):
        self.name = json_data.get("name", self.name)
        self.id = json_data.get("id", self.id)
        self.description = json_data.get("description", self.description)
        
        temp_id = generate_id_by_non_id_fields(self)
        if temp_id != self.id:
            self.id = temp_id

    def check_id(self): self.id = generate_id_by_non_id_fields(self)

    def export_data(self):
        self.check_id()
        return {
            "name": self.name,
            "id": self.id,
            "description": self.description,
        }
    
class Teacher(User):
    def __init__(self):
        super().__init__()