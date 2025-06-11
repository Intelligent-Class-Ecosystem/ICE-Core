class User:
    def __init__(self):
        self.name = "未命名用户"
        self.id = ""
        self.description = ""
        
    def import_data(self, json_data: dict):
        self.name = json_data.get("name", self.name)
        self.id = json_data.get("id", self.id)
        self.description = json_data.get("description", self.description)

    def export_data(self):
        return {
            "name": self.name,
            "id": self.id,
            "description": self.description,
        }
    
class Teacher(User):
    def __init__(self):
        super().__init__()