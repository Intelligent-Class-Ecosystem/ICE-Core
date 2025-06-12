import hashlib
import json

def process_value(value):
    """递归处理值：类实例调用export_data，列表/字典递归处理"""
    # 处理类实例（如果有export_data方法）
    if hasattr(value, 'export_data') and callable(value.export_data):
        return process_value(value.export_data())  # 递归处理导出后的数据
    # 处理列表
    elif isinstance(value, list):
        return [process_value(item) for item in value]
    # 处理字典
    elif isinstance(value, dict):
        return {k: process_value(v) for k, v in value.items()}
    # 其他类型直接返回
    else:
        return value

def generate_id_by_non_id_fields(obj):
    # 收集除了id以外的所有字段
    non_id_fields = {}
    for key, value in obj.__dict__.items():
        if key != "id":
            non_id_fields[key] = process_value(value)
    
    
    # 序列化并排序（确保相同数据生成相同MD5）
    non_id_fields_str = json.dumps(non_id_fields, sort_keys=True, ensure_ascii=False).encode("utf-8")
    
    # 计算MD5并返回
    return hashlib.md5(non_id_fields_str).hexdigest()