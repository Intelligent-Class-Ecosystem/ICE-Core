class Duration:
    def __init__(self, start: int, end: int):
        self.start = 0
        self.end = 0

class Timeline:
    def __init__(self):
        self.name = "未命名时间线"
        self.id = ""
        self.description = ""
        self.durations: list[Duration] = []
    
    def import_data(self, json_data: dict):
        self.name = json_data.get("name", self.name)
        self.id = json_data.get("id", self.id)
        self.description = json_data.get("description", self.description)
        self.durations = [Duration(duration["start"], duration["end"]) for duration in json_data.get("durations", [])]

    def export_data(self):
        return {
            "name": self.name,
            "id": self.id,
            "description": self.description,
            "durations": [{"start": duration.start, "end": duration.end} for duration in self.durations]
        }