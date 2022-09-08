import time

import requests
import parsel  # 数据提取库

url = "https://www.777zw.net/book/63/d735313443/"

header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=header)

# 打印响应内容的文本数据
data = response.text.encode('iso-8859-1').decode('utf-8')
print(data)

# 查找所需要信息
# 初始化解析库，把网页文本解析，进行css定位
selector = parsel.Selector(data)
name = selector.css('body > div.container > div.row.row-section > div > h2').get()
title = selector.css('body > div.container > div.row.row-section > div > div > ul > li:nth-child(1) > a').get()

print(name)
print(title)

x = [1, 2, 3, 4, 0]

print(sorted(x, reverse=True) == list(reversed(x)))

y = {1, 2, 3, 4, 1}
print(y)

