import requests

url = "https://fanyi.baidu.com/v2transapi?from=zh&to=en"

# 请求头
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 "
                  "Safari/537.36",
    # 网站有反扒，只写User-Agent不够，还需要写Cookie信息，最好在加上身份认证或者防盗链
    "Cookie": "BAIDUID=7E863D9F0D3C12DC81B4F580C0AEFF2D:FG=1; BIDUPSID=7E863D9F0D3C12DC81B4F580C0AEFF2D; "
              "PSTM=1658679521; BAIDUID_BFESS=7E863D9F0D3C12DC81B4F580C0AEFF2D:FG=1; "
              "ZFY=yZGrpRy6f2iaROCD8YSCrSATq4Ylnv1Yj6XhnCd:ALlI:C; BAIDU_WISE_UID=wapp_1661562134473_675; "
              "RT=\"z=1&dm=baidu.com&si=b5301f87-48f5-4fa4-80c4-8916a66e1271&ss=l7b76x2p&sl=0&tt=0&bcn=https%3A%2F"
              "%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ul=4o9&nu=j83gp33&cl=4ou&hd=4sf\"; "
              "H_PS_PSSID=36550_36465_36974_36885_37268_36570_36786_37134_26350_22160_37234; "
              "BA_HECTOR=05a12k0kag248h00al8gdp3m1hgtd6l17; BDRCVFR[S4-dAuiWMmn]=FZ_Jfs2436CUAqWmykCULPYrWm1n1fz; "
              "delPer=0; PSINO=2; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1661910807; APPGUIDE_10_0_2=1; "
              "REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; "
              "SOUND_PREFER_SWITCH=1; "
              "ab_sr=1.0"
              ".1_MDRhYmJmMGZhNTE2NjM3MGU3OGQyZDQ5NjRjNjU5OTY0MGY3Y2M2YTFlNjlkOTkzZTUyNjdh"
              "NGE2NjQ0NWY1ZTUxZGMzZjk0MTVjMmNkOGY4ZTM2MjJlMzIzOWY4NDdhOWJmNjQxNTJmM2YxNGE1MTIwNTY1ZTZ"
              "mOTdiMzE5NGM3ZTJjOTY4MDNiNTgyMjA2NjU4NjJiNTI0YWEwMzY4ZA==; "
              "Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1661910848 ",

    "Acs-Token": "1661842972316_1661910848422_JiK0+leUgCidRZ/X7OH+W8tCn5h1rbnpGWWOAbFznEDSh6"
                 "+TEgDLhXbQpnh4QztBZQA81rSBz8jXyV6XSBK9bC4EV9dNoLRW1ZTWGvBvxSatuWSrWDA+HYcLDwKGIFABCXKToxRxkVSFLy6ey"
                 "+Blfb3G6RgyAnpoYHGbB1wRJiYLI0OSQWMAnSuDCI1q7MzvBS2Gvvy/YACTUb69YhuvCaZPeIaWWeUGhUQ3p+OgJ2"
                 "/hMTaOPdNhmXdBAiIB1/XOaq5XQA7zYLHi2UoeTeT3y7m9kHzUdTULp9JAMf"
                 "//ov92SamqtZYRf9kyvcvd8KdZkzSnvHuEQtVIwB6rX6rFCw== "
}

# post发送的参数
data = {
    'from': 'zh',
    'to': 'en',
    'query': '激情',
    'simple_means_flag': '3',
    'sign': '452271.132510',
    'token': 'e591e15853907257b6ce6ba4cac02f5a',
    'domain': 'common'
}

response = requests.post(url, headers=header, data=data)

# 二次请求的数据是属于json数据（嵌套的字典）
# print(response.json()['trans_result']['data'][0]['dst'])
data = response.json()['trans_result']['data'][0]

# print(data)
print(data['dst'], end="翻译为")
print(data['src'])
