# app/models/activity.py
# 存放活动相关的模型定义. 例如: 活动模型, 活动组模型等,
# LastUpdate: 2025-5-25 CooooldWind

from .type_group import ActivityTypeGroup
from typing import Optional

class Activity:
    def __init__(self, title: str, description: Optional[str], type_group: ActivityTypeGroup):
        self.title = title
        self.description = description
        self.type_group = type_group

    def __repr__(self):
        return repr(self())

    def __getitem__(self, key):
        return self()[key]

    def __call__(self):
        return {
            "title": self.title,
            "description": self.description,
            "type_group": self.type_group.__call__()["group_type"]
        }