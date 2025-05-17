# app/models/activity_group.py
# LastUpdate: 2025-5-18 CooooldWind

# GROUP_TYPES = ("lecture", "relax", "event", "other")

class ActivityTypeGroup:
    def __init__(self, group_type: str = "other"):
        self.group_type = group_type
        self.notice_level = 0
        self.motions = []

class LectureGroup(ActivityTypeGroup):
    def __init__(self):
        super().__init__("lecture")
        self.notice_level = 2
        self.motions = []

class RelaxGroup(ActivityTypeGroup):
    def __init__(self):
        super().__init__("relax")
        self.notice_level = 1
        self.motions = []

class EventGroup(ActivityTypeGroup):
    def __init__(self):
        super().__init__("event")
        self.notice_level = 1
        self.motions = []


