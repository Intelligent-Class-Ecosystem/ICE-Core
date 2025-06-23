from app.models import *

weekday_cn = ["一","二","三","四","五","六","日"]

def create_organization():
    # 创建组织实例
    org = Organization()
    org.name = "示例学校"
    org.description = "一个包含50个教室和足够教师的学校组织"

    # 创建足够多的教师（假设每个教室每天每节课需要不同教师，按最大需求计算）
    total_teachers_needed = 50 * 5 * (4 + 3)  # 50教室 * 5天 * 7节课
    teachers = [Teacher() for _ in range(total_teachers_needed)]
    for i, teacher in enumerate(teachers):
        teacher.id = f"t_{i+1}"
        teacher.name = f"教师{i+1}"
    org.teachers.extend(teachers)

    # 创建50个教室并配置时间表
    for classroom_idx in range(50):
        classroom = Classroom()
        classroom.name = f"教室{classroom_idx+1}"

        # 为所有7天（周一到周日）创建课程表
        for week_day in range(7):

            # 上午课程：8:00-12:00，每45分钟一课，15分钟休息
            am_start_times = [[8,0], [9,0], [10,0], [11,0]]  # 4节课
            am_end_times = [[8,45], [9,45], [10,45], [11,45]]

            # 下午课程：14:00-17:00，每45分钟一课，15分钟休息
            pm_start_times = [[14,0], [15,0], [16,0]]  # 3节课
            pm_end_times = [[14,45], [15,45], [16,45]]

            # 合并上下午时间段
            all_start_times = am_start_times + pm_start_times
            all_end_times = am_end_times + pm_end_times

            # 为每个时间段创建活动和课程表
            daily_activities = []
            daily_durations = []
            daily_teachers = []

            # 收集当天所有时间段的活动和时间信息
            for period_idx in range(len(all_start_times)):
                # 计算教师索引（教室号+星期+时间段唯一确定）
                teacher_idx = classroom_idx * 5 * 7 + week_day * 7 + period_idx
                if teacher_idx >= len(teachers):
                    teacher_idx = teacher_idx % len(teachers)  # 超出则循环
                current_teacher = teachers[teacher_idx]

                # 周一到周五创建活动，周末不创建
                if week_day < 5:
                    ac = activity(
                        name=f"教室{classroom_idx+1} 周{weekday_cn[week_day]} 第{period_idx+1}节课程",
                        description="45分钟课程+15分钟休息",
                        notice_level=1,
                        teachers=[current_teacher]
                    )
                    org.activities.append(ac)
                    daily_activities.append(ac)
                    daily_teachers.append(current_teacher)
                
                # 创建时间段
                duration = Duration()
                duration.set_duration(start_time=all_start_times[period_idx], end_time=all_end_times[period_idx])
                daily_durations.append(duration)

            # 创建当天统一的课程表（周末活动列表为空）
            if week_day < 5:
                tl = timeline(
                    name=f"教室{classroom_idx+1}周{weekday_cn[week_day]}时间线",
                    durations=daily_durations,
                    description="全天分节课程时间线"
                )
                tt = ordered_timetable(
                    name=f"教室{classroom_idx+1} 周{weekday_cn[week_day]} 全天课程表",
                    timeline=tl,
                    teachers=daily_teachers,
                    activities=daily_activities,
                    period=7,
                    description="全天分节课程表"
                )
                classroom.ordered_timetables.append(tt)

        org.classrooms.append(classroom)
    return org


if __name__ == "__main__":
    school = create_organization()
    export_data_to_file("data/organization2.json", school)
    print(f"创建组织成功：{school.name}，包含{len(school.teachers)}名教师，{len(school.classrooms)}个教室")