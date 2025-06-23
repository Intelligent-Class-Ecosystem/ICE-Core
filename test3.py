from app.models import *

weekday_cn = ["一","二","三","四","五","六","日"]

def create_organization():
    # 创建组织实例
    org = Organization()
    org.name = "示例学校"
    org.description = "一个包含49个教室和49个教师的学校组织"
    # 空白时间表
    et = TimeTable()
    et.name = "空白时间表"
    et.description = "当你看到这个说明今天没课，好好休息吧~"
    # 时间表（可复用）
    # 上午课程：8:00-12:00，每45分钟一课，15分钟休息
    am_start_times = [[8,0], [9,0], [10,0], [11,0]]  # 4节课
    am_end_times = [[8,45], [9,45], [10,45], [11,45]]
    # 下午课程：14:00-17:00，每45分钟一课，15分钟休息
    pm_start_times = [[14,0], [15,0], [16,0]]  # 3节课
    pm_end_times = [[14,45], [15,45], [16,45]]
    # 合并上下午时间段
    all_start_times = am_start_times + pm_start_times
    all_end_times = am_end_times + pm_end_times
    drs = []
    for i in range(7):
        dr = duration(start_time=all_start_times[i],
                      end_time=all_end_times[i])
        drs.append(dr)
    tl = timeline(name="常规时间表",
                  durations=drs,
                  description="学校常规的上课时间")
    org.timelines.append(tl)

    # 教师
    for i in range(49):
        t = teacher(name=f"教师{i//7+1}-{i%7+1}")
        org.teachers.append(t)
    # 活动
    for i in range(49):
        a = activity(name=f"活动{i//7+1}-{i%7+1}", notice_level=1, teachers=[org.teachers[i]])
        org.activities.append(a)
    for j in range(7): # 7个教室组
        for k in range(7): # 每个教室组有7个教室
            cr = Classroom()
            cr.name = f"教室{j*7+k+1}"
            for wd_index in range(7): # 每周7天
                if wd_index >= 5: # 周末
                    cr.ordered_timetables.append(et)
                else: # 工作日
                    ap_tt = ordered_timetable(
                        name=f"教室{j*7+k+1}的周{weekday_cn[wd_index]}课表",
                        timeline=tl,
                        activities= org.activities[7*j+k:7*j+7]+org.activities[7*j:7*j+k], # 第j个教室组用 7j+1 ~ 7j+7 个活动，并且是从第 7j+k 个开始的
                        teachers=org.teachers[7*j:7*j+7],
                        period=7
                    )
                    cr.ordered_timetables.append(ap_tt)
            org.classrooms.append(cr)
    return org


if __name__ == "__main__":
    school = create_organization()
    export_data_to_file("data/organization3.json", school)
    print(f"创建组织成功：{school.name}，包含{len(school.teachers)}名教师，{len(school.classrooms)}个教室")