import hashlib
import json

# 通用函数：为任意对象实例排除id属性，计算其他属性的MD5并设置为id
def generate_id_by_non_id_fields(obj):
    # 收集实例中除id外的所有数据属性（过滤方法/特殊属性）
    non_id_fields = {}
    for key, value in obj.__dict__.items():
        if key != "id" and not callable(value) and not key.startswith("__"):
            non_id_fields[key] = value
    
    # 序列化并排序（确保相同数据生成相同MD5）
    sorted_fields_str = json.dumps(non_id_fields, sort_keys=True, ensure_ascii=False).encode("utf-8")
    
    # 计算MD5并赋值给实例的id属性
    return hashlib.md5(sorted_fields_str).hexdigest()
