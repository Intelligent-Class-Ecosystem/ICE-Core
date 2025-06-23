from app.models import *

weekday_cn = ["一","二","三","四","五","六","日"]

def create_organization():
    # 创建组织实例
    org = Organization()
    org.name = "示例学校"
    org.description = "一个包含多个教室和教师的学校组织"

    # 创建9个教师
    teachers = [Teacher() for _ in range(21)]
    for i, teacher in enumerate(teachers):
        teacher.id = f"t_{i+1}"
        teacher.name = f"教师{i+1}"
    org.teachers.extend(teachers)

    # 创建3个教室并配置时间表
    for i in range(3):
        classroom = Classroom()
        classroom.name = f"教室{i+1}"
        for d in range(7):
            ac=activity(
                name=f"教室{i+1} 的 周{weekday_cn[d]} 课程",
                description = "上午的课程",
                notice_level = 1,
                teachers = [teachers[i*3+d]]
            )
            org.activities.append(ac)
            duration = Duration()
            duration.set_duration(start_time=[9, 0], end_time=[12, 0])
            tl = timeline(name=f"教室{i+1}时间线", durations=[duration], description="示例时间线")
            tt = ordered_timetable(
                name = f"教室 {i+1} 的 周{weekday_cn[d]} 课程表",
                timeline=tl,
                teachers=[teachers[i*3+d]],
                activities=[ac],
                period=7,
                description="示例周表"
            )
            classroom.ordered_timetables.append(tt)
        org.classrooms.append(classroom)
    return org


if __name__ == "__main__":
    school = create_organization()
    export_data_to_file("data/organization.json", school)
    print(f"创建组织成功：{school.name}，包含{len(school.teachers)}名教师，{len(school.classrooms)}个教室")