"""import json
with open("data/organization.json","r",encoding="UTF-8") as f: json_data = json.load(f)
from app.models.organization import Organization
org = Organization()
org.import_data(json_data)
new_json = org.export_data()
with open("data/organization.json","w",encoding="UTF-8") as f: json.dump(new_json, f, indent=4, ensure_ascii=False)
"""
from app.models import *
"""
org = import_data_from_file("data/1.json")
t = Teacher()
t.name = "教师3"
t.check_id()
org.update_teacher_data(org.teachers[1], t)
export_data_to_file("data/2.json", org)
"""
t1 = teacher("CooooldWind", "111")
t2 = teacher("BHawa", "222")

a1 = activity(name = "Infomation & Technology", notice_level = 1, teachers = [t1, t2])

tt1 = None
