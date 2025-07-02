from flask import Blueprint, jsonify, request
from app.models import import_data_from_file, export_data_to_file
from app.routes.tools import import_config

organization_api_bp = Blueprint("organization_api", __name__)

@organization_api_bp.route("/api/organization/get-info", methods = ["GET"])
def get_organization():
    org_path = "data/" + import_config()["organization_path"]
    org = import_data_from_file(org_path)
    return jsonify({"status": "success", "data": org.export_data()})

@organization_api_bp.route("/api/organization/edit-info", methods = ["POST"])
def update_organization():
    org_path = "data/" + import_config()["organization_path"]
    org = import_data_from_file(org_path)
    data = request.json
    if not data: return jsonify({"status": "error", "message": "请求必须包含数据"}), 400
    if "name" in data: org.name = data["name"]
    elif "description" in data: org.description = data['description']
    else: return jsonify({"status": "error", "message": "请求必须包含name或description字段"}), 400
    export_data_to_file(org_path, org)
    return jsonify({"status": "success", "message": "组织信息已更新", "data": org.export_data()})

"""
@api_bp.route("/api/add-teacher", methods = ["POST"])
def add_teacher():
    org_path = "data/" + import_config()["organization_path"]
    org = import_data_from_file(org_path)
    data = request.json
    if not data: return jsonify({"status": "error", "message": "请求必须包含数据"}), 400
    description = ""
    if "name" not in data: return jsonify({"status": "error", "message": "请求必须包含name字段"}), 400
    else: name = data["name"]
    if "description" in data: description = data["description"]
    t = teacher(name) if description == "" else teacher(name, description)
    org.teachers.append(t)
    export_data_to_file(org_path, org)
    return jsonify({"status": "success", "message": "组织信息已更新", "data": t.export_data()})
"""
