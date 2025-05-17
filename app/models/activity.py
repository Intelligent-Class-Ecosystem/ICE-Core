# app/models/activity.py
# 存放活动相关的模型定义. 例如: 活动模型, 活动组模型等,
# LastUpdate: 2025-5-18 CooooldWind

from models.type_group import ActivityTypeGroup
from typing import Optional

class Activity:
    def __init__(self, title: str, description: Optional[str], spend_time: int, type_group: ActivityTypeGroup):
        self.title = title
        self.description = description
        self.spend_time = spend_time
        self.type_group = type_group



