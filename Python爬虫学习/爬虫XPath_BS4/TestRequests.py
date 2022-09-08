import requests
import webbrowser  # 自动打开网页

key = input('输入查询内容')

print(key)

url = 'https://www.baidu.com/s?wd=' + key

# 系统信息，浏览器信息
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)

html = response.content.decode('utf-8')

with open('baidu-copy.html', 'w', encoding='utf-8') as file:
    file.write(html)

webbrowser.open('baidu-copy.html')
