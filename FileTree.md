ICE-Core/
├── app/
│   ├── __init__.py          # Flask应用工厂
│   ├── config.py            # 配置文件
│   ├── models/              # 数据模型
│   │   ├── activity.py      # 活动相关模型
│   │   └── timeline.py      # 时间线模型
│   ├── routes/              # 路由层
│   │   ├── activity.py      # 活动相关路由
│   │   └── timeline.py      # 时间线路由
│   ├── services/           # 业务逻辑
│   │   ├── activity_service.py 
│   │   └── timeline_service.py
│   └── utils/              # 工具类
│       ├── device_monitor.py # 设备监控
├── instance/               # 实例文件夹（Flask推荐）
│   └── config.py           # 本地开发配置
├── tests/                  # 单元测试
├── requirements.txt       # 依赖清单
├── run.py
├── .gitignore
└── README.md              # 你的现有文件
