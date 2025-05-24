# tests/test_timeline.py
import pytest
from app.models.timeline import Timeline
from app.models.activity import Activity
from app.models.type_group import ActivityTypeGroup

class TestTimelineAddActivity:
    def setup_method(self):
        self.timeline = Timeline()
        self.activity = Activity("Test Activity", "", ActivityTypeGroup.EVENT)

    def test_add_valid_activity(self):
        """测试添加有效活动"""
        self.timeline.add_activity(self.activity, 1000, 2000)
        assert len(self.timeline.activities) == 1
        assert self.timeline.activities[0].start_time == 1000
        assert self.timeline.activities[0].end_time == 2000

    def test_add_overlapping_activity(self):
        """测试添加时间冲突的活动"""
        self.timeline.add_activity(self.activity, 1000, 2000)
        with pytest.raises(ValueError, match="Time conflict"):
            self.timeline.add_activity(self.activity, 1500, 2500)

    def test_add_activity_with_start_after_end(self):
        """测试开始时间大于结束时间"""
        with pytest.raises(ValueError, match="Start time must be before end time"):
            self.timeline.add_activity(self.activity, 2000, 1000)

    def test_add_activity_with_negative_time(self):
        """测试负时间"""
        with pytest.raises(ValueError, match="Time must be positive"):
            self.timeline.add_activity(self.activity, -1000, 2000)
        with pytest.raises(ValueError, match="Time must be positive"):
            self.timeline.add_activity(self.activity, 1000, -2000)

    def test_add_activity_with_same_time(self):
        """测试开始和结束时间相同"""
        with pytest.raises(ValueError, match="Start time and end time must be different"):
            self.timeline.add_activity(self.activity, 1000, 1000)

    def test_add_activity_exceeding_24h(self):
        """测试超过24小时"""
        with pytest.raises(ValueError, match="Time must be less than 24 hours"):
            self.timeline.add_activity(self.activity, 0, 86400)
        with pytest.raises(ValueError, match="Time must be less than 24 hours"):
            self.timeline.add_activity(self.activity, 86400, 90000)

    def test_activities_sorted_by_start_time(self):
        """测试活动按开始时间排序"""
        self.timeline.add_activity(self.activity, 3000, 4000)
        self.timeline.add_activity(self.activity, 1000, 2000)
        assert self.timeline.activities[0].start_time == 1000
        assert self.timeline.activities[1].start_time == 3000

    def test_add_multiple_non_overlapping_activities(self):
        """测试添加多个不冲突的活动"""
        activity2 = Activity("Test Activity 2", "", ActivityTypeGroup.RELAX)
        self.timeline.add_activity(self.activity, 1000, 2000)
        self.timeline.add_activity(activity2, 2000, 3000)
        assert len(self.timeline.activities) == 2