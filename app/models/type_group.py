# app/models/activity_group.py
# LastUpdate: 2025-5-18 CooooldWind

# GROUP_TYPES = ("lecture", "relax", "event", "other")

from typing import Dict

class ActivityTypeGroup:
    # 添加类常量
    LECTURE: 'LectureGroup'
    EVENT: 'EventGroup'
    RELAX: 'RelaxGroup'
    OTHER: 'ActivityTypeGroup'

    def __init__(self, group_type: str = "other"):
        self.group_type = group_type
        self.notice_level = 0
        self.motions = []

    # 初始化类属性
    @classmethod
    def _init_class_constants(cls):
        cls.LECTURE = LectureGroup()
        cls.RELAX = RelaxGroup()
        cls.EVENT = EventGroup()
        cls.OTHER = cls("other")

    def __repr__(self):
        return repr(self())
    
    def __getitem__(self, key):
        return self()[key]

    def __call__(self):
        return {
            "group_type": self.group_type,
            "notice_level": self.notice_level,
            "motions": self.motions
        }


# 将子类定义移到 ActivityTypeGroup 类之后
class LectureGroup(ActivityTypeGroup):
    def __init__(self):
        super().__init__("lecture")
        self.notice_level = 2

class RelaxGroup(ActivityTypeGroup):
    def __init__(self):
        super().__init__("relax")
        self.notice_level = 1

class EventGroup(ActivityTypeGroup):
    def __init__(self):
        super().__init__("event")
        self.notice_level = 1

# 最后执行初始化
ActivityTypeGroup._init_class_constants()

    

