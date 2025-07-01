from flask import Blueprint, jsonify, request
from app.models import import_data_from_file, export_data_to_file, teacher
import os
import json

# 从数据库文件夹读取配置文件，若没有则创建文件夹/配置文件
def import_config() -> dict:
    if os.path.exists("data/") == False:
        os.mkdir("data/")
    if os.path.exists("data/config.json") == False:
        with open("data/config.json", "w", encoding = "UTF-8") as f:
            json.dump({"organization_path": "organization.json"}, f, ensure_ascii = False)
    with open("data/config.json", "r", encoding = "UTF-8") as f:
        d = json.load(f)
    path = "data/" + d["organization_path"]
    if os.path.exists(path) == False:
        with open(path, encoding = "UTF-8") as f:
            json.dump({}, f, ensure_ascii = False)
    with open("data/config.json", "r", encoding = "UTF-8") as f:
        return json.load(f)

api_bp = Blueprint("api", __name__)

@api_bp.route("/api/get-organization-data", methods = ["GET"])
def get_organization():
    org_path = "data/" + import_config()["organization_path"]
    org = import_data_from_file(org_path)
    return jsonify(org.export_data())

@api_bp.route("/api/edit-organization-info", methods = ["POST"])
def update_organization():
    org_path = "data/" + import_config()["organization_path"]
    org = import_data_from_file(org_path)
    data = request.json
    if not data: return jsonify({"status": "error", "message": "请求必须包含数据"}), 400
    if "name" in data: org.name = data['name']
    elif "description" in data: org.description = data['description']
    else: return jsonify({"status": "error", "message": "请求必须包含name或description字段"}), 400
    export_data_to_file(org_path, org)
    return jsonify({"status": "success", "message": "组织信息已更新", "data": org.export_data()})

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

@api_bp.route("/api/get-classroom-info/<classroom_id>", methods = ["GET"])
def get_classroom_info(classroom_id):
    org_path = "data/" + import_config()["organization_path"]
    org = import_data_from_file(org_path)
    for clsrm in org.classrooms:
        if clsrm.id == classroom_id:
            return clsrm.export_data()
    return f"Can't find the classroom with the id {classroom_id} ."