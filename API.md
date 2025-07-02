# ICE(Intelligent Class Ecosystem) 冰核智慧课堂生态系统内核 (后端) 文档

## 调用API之前, 你首先需要
1. 在电脑 (不限制系统) 上下载并安装 Python (推荐尽量最新版), 注意在启动安装程序时勾选 "Add ... th PATH", 且安装后重启电脑
2. clone 本仓库, 或者下载本仓库的压缩包并解压
3. 在仓库所属的文件夹 (里面应当包含 `run.py`) 内打开命令行, 运行 `pip install -r requirements.txt`
4. 继续运行 `python run.py`
5. 开始享用!

## API文档
### 组织
1. `IP:28582/api/organization/get-info`: 获取组织的json文档, GET请求, 返回格式: json
2. `IP:28582/api/organization/edit-info`: 修改组织的基础信息, POST请求, 需传入 `name` 或 `description` 字段, 返回格式: json
3. 锐意开发中...

### 教室
1. `IP:28582/api/classroom/get-info?id=[classroom_id]`: 获取某个教室的json文档, GET请求, 需将 `[classroom_id]` 修改为一个有效的教室id, 返回格式: json
2. `IP:28582/api/classroom/add-classroom`: 新建一个教室, POST请求, 需传入 `name` 字段, 可选择传入 `description` 字段, 返回格式: json
3. 锐意开发中...
