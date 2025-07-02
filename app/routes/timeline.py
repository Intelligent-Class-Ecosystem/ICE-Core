from flask import Blueprint, jsonify, request
from app.models import import_data_from_file, export_data_to_file, timeline, duration, Duration
from tools import import_config

timeline_api_bp = Blueprint("timeline_api", __name__)

# 未完工
@timeline_api_bp("/api/timeline/add-timeline", method = ["POST"])
def add_timeline():
    org_path = "data/" + import_config()["organization_path"]
    org = import_data_from_file(org_path)
    data = request.json
    if not data: return jsonify({"status": "error", "message": "请求必须包含数据"}), 400
    if "name" in data: name = data['name']
    else: return jsonify({"status": "error", "message": "请求必须包含name字段"}), 400
    if "description" in data: description = data["description"]
    if "durations" in data: unformated_durations = data["durations"]
    else: return jsonify({"status": "error", "message": "请求必须包含durations字段"}), 400
    if type(unformated_durations) != list: return jsonify({"status": "error", "message": "durations字段必须为一个列表"}), 400
    formated_durations: list[Duration] = []
    for und in unformated_durations:
        """
        unformated_durations需要是这样的:
        [
        [[8, 0], [8, 45]],      ----    08:00 ~ 08:45
        [[8, 55], [9, 40]],     ----    08:55 ~ 09:40
        ......
        [[17, 5], [17, 50]],    ----    17:05 ~ 17:50
        ]
        """
        formated_durations.append(duration(start_time = und[0], end_time = und[1]))
    tl = timeline()