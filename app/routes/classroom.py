from flask import Blueprint, jsonify, request
from app.models import import_data_from_file, export_data_to_file, classroom, ordered_timetable, operation_timetable, timeline
from app.routes.tools import import_config, check_data_requirement

DEFAULT_TIMELINE = timeline("空时间表", [], "空时间表")

classroom_api_bp = Blueprint("teacher_api", __name__)

@classroom_api_bp.route("/api/classroom/get-info", methods = ["GET"])
def get_classroom_info():
    org_path = "data/" + import_config()["organization_path"]
    org = import_data_from_file(org_path)
    classroom_id = request.args.get("id")
    for clsrm in org.classrooms:
        if clsrm.id == classroom_id:
            return jsonify({"status": "success", "data": clsrm.export_data()})
    return jsonify({"status": "error", "message": f"无法找到id为 {classroom_id} 的教室"}), 400

@classroom_api_bp.route("/api/classroom/add-classroom", methods = ["POST"])
def add_classroom():
    org_path = "data/" + import_config()["organization_path"]
    org = import_data_from_file(org_path)
    data = request.json
    if not data: return jsonify({"status": "error", "message": "请求必须包含数据"}), 400
    if "name" in data: pass
    else: return jsonify({"status": "error", "message": "请求必须包含name字段"}), 400
    if "description" in data: clsrm = classroom(data["name"], data["description"])
    else: clsrm = classroom(data["name"])
    org.classrooms.append(clsrm)
    export_data_to_file(org_path, org)
    return jsonify({"status": "success", "message": "组织信息已更新", "data": clsrm.export_data()})

@classroom_api_bp.route("/api/classroom/classroom-list", methods = ["GET"])
def get_classroom_list():
    org_path = "data/" + import_config()["organization_path"]
    org = import_data_from_file(org_path)
    ret = []
    for clsrm in org.classrooms:
        ret_addition = {
            "name": clsrm.name,
            "description": clsrm.description,
            "id": clsrm.id
        }
        ret.append(ret_addition)
    return jsonify({"status": "success", "data": ret})

@classroom_api_bp.route("/api/classroom/timetable-list", methods = ["GET"])
def get_classroom_timetable_list():
    org_path = "data/" + import_config()["organization_path"]
    org = import_data_from_file(org_path)
    classroom_id = request.args.get("id")
    type_tmp = str(request.args.get("type"))
    operation = False
    if type_tmp == "operation":
        operation = True
    for clsrm in org.classrooms:
        if clsrm.id == classroom_id:
            if operation:
                return jsonify({"status": "success", "data": [tmp.export_data() for tmp in clsrm.operation_timetables]})
            else:
                return jsonify({"status": "success", "data": [tmp.export_data() for tmp in clsrm.ordered_timetables]})
    return jsonify({"status": "error", "message": f"无法找到id为 {classroom_id} 的教室."}), 400

@classroom_api_bp.route("/api/classroom/add-ordered-timetable", methods = ["POST"])
def add_ordered_timetable():
    org_path = "data/" + import_config()["organization_path"]
    org = import_data_from_file(org_path)
    data = request.json
    if not data: return jsonify({"status": "error", "message": "请求必须包含数据"}), 400
    check_ret = check_data_requirement(data, [
        "name",
        "description",
        "timeline_id",
        "teachers_id",
        "activities_id",
        "classroom_id",
        "period"
    ])
    if check_ret == False:
        return jsonify({"status": "error", "message": "请检查参数"}), 400
    name = data["name"]
    timeline = DEFAULT_TIMELINE
    teachers = []
    activities = []
    for tmp in org.timelines:
        if tmp.id == data["timeline_id"]: timeline = tmp
    for i, j in list(data["teachers"]), org.teachers:
            if j.id == i: teachers.append(j)
    for i, j in list(data["activities"]), org.activities:
        if j.id == i: activities.append(j)
    description = data["description"]
    period = data["period"]
    if description == None: ott = ordered_timetable(name, timeline, teachers, activities, period)
    else: ott = ordered_timetable(name, timeline, teachers, activities, period, description)
    for tmp in org.classrooms:
        if tmp.id == data["classroom_id"]:
            tmp.ordered_timetables.append(ott)
            return jsonify({"status": "success", "data": ott.export_data()})
    


