from .timetable_model import TimeTable
from .user_model import Teacher
from .timeline_model import Timeline
from .activity_model import Activity
from .class_id_calculate_function import generate_id_by_non_id_fields


class Classroom:
    def __init__(self):
        self.id = ""
        self.name = "未命名教室"
        self.description = ""
        self.ordered_timetables: list[TimeTable] = []
        self.operation_timetables: list[TimeTable] = []

    def import_data(self,
                    json_data: dict,
                    organization_timelines: list[Timeline],
                    organization_teachers: list[Teacher],
                    organization_activities: list[Activity]):

        # 基本信息
        self.name = json_data.get("name", self.name)
        self.id = json_data.get("id", self.id)
        self.description = json_data.get("description", self.description)

        # 时间表
        for timetable_dict in list(json_data.get("ordered_timetables", [])):
            temp_timetable = TimeTable()
            # 真正需要的老师存在timetable_dict里面，后面几个参数只是提供可选的而已
            temp_timetable.import_data(timetable_dict, organization_timelines, organization_teachers, organization_activities)
            self.ordered_timetables.append(temp_timetable)
        for timetable_dict in list(json_data.get("operation_timetables", [])):
            temp_timetable = TimeTable()
            # 真正需要的老师存在timetable_dict里面，后面几个参数只是提供可选的而已
            temp_timetable.import_data(timetable_dict, organization_timelines, organization_teachers, organization_activities)
            self.operation_timetables.append(temp_timetable)

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
            "ordered_timetables": [timetable.export_data() for timetable in self.ordered_timetables],
            "operation_timetables": [timetable.export_data() for timetable in self.operation_timetables]
        }
        


    