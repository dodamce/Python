"""
爬虫流程：
1. 获取url。
2. 向url发送请求，并且获取相应。
3. 从相应中获取url，并且持续获取相应。
4. 从响应中提取数据并保存。
"""

import requests

# 获取url
url = 'https://www.baidu.com/'

# 向url发送HTTP请求
response = requests.get(url)

# 从响应中提取数据并保存。
print(response)  # <Response [200]>
# print(response.text) 出现乱码
print(response.content.decode())  # 解决乱码,decode默认utf-8编码

