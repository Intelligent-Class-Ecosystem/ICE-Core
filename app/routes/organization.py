from flask import Blueprint, jsonify, request
from app.models import import_data_from_file, export_data_to_file
import os

org_bp = Blueprint("organization", __name__)

@org_bp.route("/api/organization/get-organization-data", methods=["GET"])
def get_organization():
    org = import_data_from_file("data/organization.json")
    return jsonify(org.export_data())

@org_bp.route("/api/organization/edit-common-info", methods=["POST"])
def update_organization():
    data = request.json
    if not data:
        return jsonify({"status": "error", "message": "请求必须包含数据"}), 400
    org = import_data_from_file("data/organization.json")
    if "name" in data: org.name = data['name']
    elif "description" in data: org.description = data['description']
    else: return jsonify({"status": "error", "message": "请求必须包含name或description字段"}), 400
    export_data_to_file("data/organization.json", org)
    return jsonify({"status": "success", "message": "组织信息已更新"})