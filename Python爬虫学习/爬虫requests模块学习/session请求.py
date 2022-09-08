import requests

url = 'https://www.yaozh.com/login'

header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}

data = {
    'type': '0',
    'username': '****',
    'pwd': '****',
    'country': '86_zh-CN',
    'formhash': '222C1F1A26',
    'backurl': '%2F%2Fwww.yaozh.com'
}

session = requests.Session()
response = session.post(url, headers=header, data=data)
# print(response)

# session中会保存session_id，可以访问个人主页
user_msg = session.get("https://www.yaozh.com/member/", headers=header)
if user_msg.status_code == 200:
    print('获取用户主页完成')

with open('药智网登录页面.html', "w", encoding='utf-8') as file:
    # 写入图片，视频。音乐时需要用字节流的形式写入
    file.write(user_msg.text)
