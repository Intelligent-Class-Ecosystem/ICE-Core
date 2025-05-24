# app/models/timeline.py
# LastUpdate: 2025-5-25 CooooldWind

from .activity import Activity
from typing import Optional, List
from.type_group import ActivityTypeGroup

class TimelineActivity(Activity):
    def __init__(self, activity: Activity, start_time: int, end_time: int):
        # 传入一个活动类变量
        super().__init__(activity.title, activity.description, activity.type_group)
        self.start_time: int = start_time
        self.end_time: int = end_time

class Timeline:
    def __init__(self):
        self.activities:List[TimelineActivity] = []

    def add_activity(self, activity: Activity, start_time: int, end_time: int):
        # 检查时间是否被占用
        for a in self.activities:
            if start_time < a.end_time and end_time > a.start_time:
                raise ValueError("Time conflict")
        if start_time < 0 or end_time < 0:
            raise ValueError("Time must be positive")
        if start_time > end_time:
            raise ValueError("Start time must be before end time")
        if start_time == end_time:
            raise ValueError("Start time and end time must be different")
        if start_time >= 86400 or end_time >= 86400:
            raise ValueError("Time must be less than 24 hours")
        self.activities.append(TimelineActivity(activity, start_time, end_time))
        # 按开始时间排序
        self.activities.sort(key=lambda x: x.start_time)
    def __call__(self):
        return [activity() for activity in self.activities]

# 既定时间表 
class OrderedTimeline(Timeline):
    def __init__(self):
        super().__init__()