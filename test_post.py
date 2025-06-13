import requests
import json

url = 'http://localhost:28582/api/organization/edit-common-info'
headers = {
    'Content-Type': 'application/json',
    'User-Agent': 'ICE-Core Test Client'
}
data = {
    'name': '测试组织',
    'description': 'POST请求创建的组织描述'
}

try:
    response = requests.post(url, headers=headers, data=json.dumps(data))
    response.raise_for_status()
    print(f"请求成功！状态码: {response.status_code}")
    print("响应内容:", response.json())
except requests.exceptions.HTTPError as errh:
    print(f"HTTP错误: {errh}")
except requests.exceptions.ConnectionError as errc:
    print(f"连接错误: {errc}")
except requests.exceptions.Timeout as errt:
    print(f"超时错误: {errt}")
except requests.exceptions.RequestException as err:
    print(f"请求异常: {err}")