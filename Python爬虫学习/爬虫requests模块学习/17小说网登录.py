import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 "
                  "Safari/537.36 "
}

data = {
    'loginName': '18935253930',
    'password': '123abc...'
}

session = requests.Session()

# 登录
response = session.post("https://passport.17k.com/ck/user/login", headers=headers, data=data)

# <a href="//www.17k.com/book/3421307.html" target="_blank" title="不灭造化决">不灭造化决</a>

if response.status_code == 200:
    print('登录成功，获取我的搜藏网页')
    url = "https://user.17k.com/www/bookshelf/index.html"
    ret = session.get(url, headers=headers)
    if ret.status_code == 200:
        print(ret.content.decode('utf-8'))
    else:
        print('获取我的搜藏网页失败')
