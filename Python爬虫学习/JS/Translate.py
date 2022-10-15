import requests
import time
import hashlib
import random

url = "https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 "
                  "Safari/537.36",
    "Cookie": "OUTFOX_SEARCH_USER_ID=-1946181156@10.105.137.202; OUTFOX_SEARCH_USER_ID_NCOO=1997833077.2695937; "
              "___rl__test__cookies=1661932062388",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Referer": "https://fanyi.youdao.com/"
}

while True:
    word = input("请输入要翻译的词汇：\n")

    trans = hashlib.md5()

    ts = str(int(time.time() * 1000))
    salt = ts + str(random.randint(0, 10))
    trans.update(
        '5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'.encode(
            'utf-8'))
    bv = trans.hexdigest()

    trans = hashlib.md5()  # 清空trans
    trans.update(("fanyideskweb" + word + salt + "Ygy_4c=r#e#4EX^NUGUc5").encode('utf-8'))
    sign = trans.hexdigest()

    data = {
        'i': word,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': salt,
        'sign': sign,
        'lts': ts,
        'bv': bv,
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTlME'
    }

    response = requests.post(url, headers=header, data=data).json()
    print(response)

    translate = response['translateResult'][0][0]
    # print(translate)

    print(f'%s的意思是%s' % (translate['tgt'], translate['src']))
