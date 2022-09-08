import requests

url = "https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 "
                  "Safari/537.36",
    "Cookie": "OUTFOX_SEARCH_USER_ID=-1946181156@10.105.137.202; OUTFOX_SEARCH_USER_ID_NCOO=1997833077.2695937; "
              "___rl__test__cookies=1661932062388",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Referer": "https://fanyi.youdao.com/"
}

data = {
    'i': '激情',
    'from': 'zh-CHS',
    'to': 'en',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'salt': '16619320623954',
    'sign': 'e0c54e9d51998ff92b84acd4b98421ae',
    'lts': '1661932062395',
    'bv': '50b61ff102560ebc7bb0148b22d7715c',
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_REALTlME'
}

response = requests.post(url, headers=header, data=data).json()
print(response)

translate = response['translateResult'][0][0]
# print(translate)

print(f'单词%s的意思是%s' % (translate['tgt'], translate['src']))
