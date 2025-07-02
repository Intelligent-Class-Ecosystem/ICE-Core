from flask import Blueprint, jsonify, request
from app.models import import_data_from_file, export_data_to_file, classroom
from app.routes.tools import import_config

classroom_api_bp = Blueprint("teacher_api", __name__)

@classroom_api_bp.route("/api/classroom/get-info", methods = ["GET"])
def get_classroom_info():
    org_path = "data/" + import_config()["organization_path"]
    org = import_data_from_file(org_path)
    classroom_id = request.args.get("id")
    for clsrm in org.classrooms:
        if clsrm.id == classroom_id:
            return jsonify({"status": "success", "data": clsrm.export_data()})
    return jsonify({"status": "error", "message": f"无法找到id为 {classroom_id} 的教室."}), 400

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
