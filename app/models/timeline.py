VALUE_ERROR_LIST = ["the list's length is invalid.",
                    "time's hour number is invalid.",
                    "time's minute number is invalid."
                    ]

from .class_id_calculate_function import generate_id_by_non_id_fields

def valid_timestamp(timestamp: int):
    if timestamp >= 0 and timestamp <= 86400: return True
    else: raise ValueError("Timestamp error.")

def valid_time(time: list[int]) -> int:
    if len(time) != 2:
        return 0
    elif not(time[0] >= 0 and time[0] <= 23):
        return 1
    elif not(time[1] >= 0 and time[1] <= 59):
        return 2
    else: return -1

class Duration:
    def __init__(self, start: int, end: int):
        self.start = 0
        self.end = 0

    def set_duration(self,
                     start_timestamp: int = -1,
                     end_timestamp: int = -1,
                     duration_timestamp: int = -1,
                     start_time: list[int] = [-1,-1],
                     end_time: list[int] = [-1,-1],
                     duration_time: list[int] = [-1,-1]
                     ):
        temp_start_timestamp, temp_end_timestamp, temp_duration_timestamp = -1, -1, -1

        # 用户填写 start_time/end_time/duration_time 字段
        if start_time != [-1,-1]:
            if valid_time(start_time) != -1:
                raise ValueError("Start time value invalid: " + VALUE_ERROR_LIST[valid_time(start_time)])
            else: temp_start_timestamp = start_time[0] * 3600 + start_time[1] * 60
        if end_time != [-1,-1]:
            if valid_time(end_time) != -1:
                raise ValueError("End time value invalid: " + VALUE_ERROR_LIST[valid_time(end_time)])
            else: temp_end_timestamp = end_time[0] * 3600 + end_time[1] * 60
        if duration_time != [-1,-1]:
            if valid_time(duration_time) != -1:
                raise ValueError("Duration time value invalid: " + VALUE_ERROR_LIST[valid_time(duration_time)])
            else: temp_duration_timestamp = duration_time[0] * 3600 + duration_time[1] * 60
        
        # 填写了 duration_timestamp
        if duration_timestamp != -1: temp_duration_timestamp = duration_timestamp       
        if start_timestamp != -1 and valid_timestamp(start_timestamp): temp_start_timestamp = start_timestamp
        if end_timestamp != -1 and valid_timestamp(end_timestamp): temp_end_timestamp = end_timestamp

        # 填写了 duration_timestamp/duration_time
        if temp_duration_timestamp != -1 and valid_timestamp(temp_start_timestamp + temp_duration_timestamp):
            temp_end_timestamp = temp_start_timestamp + temp_duration_timestamp

        # 检验
        if temp_end_timestamp > temp_start_timestamp:
            self.start, self.end = temp_start_timestamp, temp_end_timestamp

    def export_data(self): return {"start": self.start, "end": self.end}
            
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
        self.durations.sort(key = lambda x:x.start)
        for i in range(0, len(self.durations) - 1):
            if self.durations[i].end > self.durations[i + 1].start: 
                raise ValueError("Front duration's end time should earlier than Back duration's start time.")
            
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
            "durations": [{"start": duration.start, "end": duration.end} for duration in self.durations]
        }