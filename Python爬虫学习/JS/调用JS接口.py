import execjs
import requests

# https://fanyi.baidu.com/v2transapi?from=zh&to=en
url = 'https://fanyi.baidu.com/v2transapi?from=zh&to=en'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
    'Cookie': 'BIDUPSID=754A533E1A4F1B8ACCE56A0F70B49D17; PSTM=1654060281; BAIDUID=754A533E1A4F1B8ADECA83314480BD17:SL=0:NR=10:FG=1; MCITY=-275%3A158%3A; MAWEBCUID=web_ybakUyVDwvPoBAeSTCZRZuIvZfOjluCjSTRNRbtWUArkRoEDwr; BAIDUCUID_BFESS=web_ybakUyVDwvPoBAeSTCZRZuIvZfOjluCjSTRNRbtWUArkRoEDwr; BDUSS=c5VzJjeXhadnJma0E3WH5reFVEREhtNlJYfm9rT2ItMENtZjhLaXFva29-eVpqSVFBQUFBJCQAAAAAAAAAAAEAAADNI-GJa2prNzM0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAChy~2Iocv9ieH; BDUSS_BFESS=c5VzJjeXhadnJma0E3WH5reFVEREhtNlJYfm9rT2ItMENtZjhLaXFva29-eVpqSVFBQUFBJCQAAAAAAAAAAAEAAADNI-GJa2prNzM0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAChy~2Iocv9ieH; APPGUIDE_10_0_2=1; FANYI_WORD_SWITCH=1; REALTIME_TRANS_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; HISTORY_SWITCH=1; BA_HECTOR=0hah01200505a18l818lgf6c1hgouao17; BAIDUID_BFESS=754A533E1A4F1B8ADECA83314480BD17:SL=0:NR=10:FG=1; ZFY=daAReCooaTao5xOe:B1JYq32rLxxSQhJWtk44GLQQ:BQY:C; BDRCVFR[sOxo1TgcNNt]=OjjlczwSj8nXy4Grjf8mvqV; H_PS_PSSID=; delPer=0; PSINO=7; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1661485554,1661778565; ab_sr=1.0.1_MDdlZmI0YTM4YzkwN2Q5ZDM5OWQ4OTdiZTk0ZWE0ODFiNTcwYjM3MTMxMjIzNTE1YTBkODM2M2FlYjBmNzEzNTJlNGVlYThiOTlmODRkOWMyMGE1M2RlNDc3OWRkYWNhNmRjOWEzOGI1ZDJlNGI2Y2JmMGMxOWMyMmM2NmQ4NTZlYmM4MzEyZDBhZjYzZTNjNjRmZDg2YzQ0NmY1Y2IxZjI3MDM5ZmY2NjhhMjI4OWY3ZGUwMzNlOGYwODdiMzcx; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1661778760',
    'Acs-Token': '1661756568966_1661778761719_10zFJU9WnjdYmtJQQGvCunUV5/EN5i5e6AdkEy7fJiDSrcjBJjTojS+14//l8BZ7Ie8vDKj7pCffuFfQEOr5Aaj4IYnQFOiqTXP9tAdtZRgGi6aHOKOCIRkiUjP4rHCXgQ/dV8vceAdKz52Uz5u6uZ9eiOXY6uHBVIAxgvMqyys3Sp3i0lGk0n/EpczIXep/lBEjqlCxvCgKXj39/mHKUnAomoAMtP6j1T6EwwrbeHr/RUPVfuwJFlCitn2gICP//BpNt1g0ve9tQWOgZTQd8j934J3syhKkY+L5uUpqQGnqn+uvS7Hg8cGBWg8krLtklxZLoTX//7UPLGFiVM4YuHjjZlFZsWlKs5eLZvseQZ4=',
    'Referer': 'https://fanyi.baidu.com/?aldtype=16047'
}

file = open('./encode.js', 'r', encoding='utf-8')
js = file.read()
file.close()

while True:
    word = input("输入中文:\n")

    encode = execjs.compile(js)
    sign = encode.call('encode', word)
    # print(sign)

    data = {
        'from': 'zh',
        'to': 'en',
        'query': word,
        'simple_means_flag': '3',
        'sign': sign,
        'token': '9478f6fd7db97e499aceddf91b6048b5',
        'domain': 'common',
    }

    html_data = requests.post(url, data=data, headers=headers)
    # print(html_data.json())
    dict_data = html_data.json()['trans_result']['data'][0]
    print(dict_data['src'])
    print(dict_data['dst'])
