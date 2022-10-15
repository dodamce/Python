import requests
import re
from urllib import parse

from pprint import pprint

# 2022年 10月15日 生效

# 刘思瑶主页
url = "https://www.douyin.com/user/MS4wLjABAAAAaSfA0HM0mHsoLdNIiwcFfUUYmmD_xGE6IEni35uxzkE"

# driver = webdriver.Chrome()
#
# driver.get(url)
#
# page = 0
# front = ""
# this = ""
# while True:  # 实现动态网页下拉
#     front = copy.deepcopy(this)
#     js = 'window.scrollTo(0,%s)' % (page * 100)
#     page += 5
#     driver.execute_script(js)
#     time.sleep(0.3)
#     this = driver.page_source
#     if front == this:
#         break

# 失效更新cookie
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 '
                  'Safari/537.36 Edg/106.0.1370.42 ',
    'cookie': 'douyin.com; __ac_referer=__ac_blank; __ac_signature=_02B4Z6wo00f01p-N7bwAAIDCH48X.yJvmXKfrekAAMS1c9; '
              'ttwid=1%7C7x6Dn4p_51RoMixhOgjVOa3QqERscAwckokNuJVmlSc%7C1665794572'
              '%7C5d99b2168152ffa7ed69147495c92c56182ac8a3a62b0e1cfd97303faf78d72f; douyin.com; '
              'strategyABtestKey=1665794574.688; s_v_web_id=verify_l9972wid_cG5g3uoF_EVfU_4aAD_8IMc_MjSDaITxEYuC; '
              'passport_csrf_token=9f74ec7632cd12c538c1655b56d140bc; '
              'passport_csrf_token_default=9f74ec7632cd12c538c1655b56d140bc; '
              'ttcid=84b14853cf114dd0a5280d1c6385bf7292; SEARCH_RESULT_LIST_TYPE=%22single%22; '
              'home_can_add_dy_2_desktop=%221%22; '
              'tt_scid=-lKrMKyU88ObyghPekic1UuHsI7YgsSMyHJ7Hg3IqbY00KICh93FcCet1IsCzRmQ94d9; '
              'download_guide=%223%2F20221015%22; __ac_nonce=0634a0c6700173e3e6830; '
              'msToken=f9ZR09OikaIblw4AiFEpoqf8NARIYTzDQDikk2_VcX4Iyyt6PmC2vEtAZJm52ruLE6QRM2L5QfwlAvNbpCecgpujsbQiXaeMxMChdzYnVAYJfd1RXPTkFWHKlNZODw==; msToken=T_SjfNU0YPQ0lTwsKDv5r9UNCbz2M7TA9RuajUwYwFjGd_4XbmyUXUiNzDs78pCNo4lJTNfdjNFIIcAK0dxOYOoMLU9nSSJDu6D4WbQHH-Fwqm4XeDO1Gl6f4lnJ1Q==; _tea_utm_cache_2018=undefined '
}

response = requests.get(url=url, headers=headers)

# pprint(parse.unquote(driver.page_source))

# 获取有效信息
data = parse.unquote(re.findall('<script id="RENDER_DATA" type="application/json">(.*?)</script>',
                                response.text, re.S)[0])

# data是json字符串，将json转化为字符串,eval方法
# eval内部需要定义false true null这三个变量
false = False
true = True
null = None
dict_msg = eval(data)

# pprint(dict_msg)

# input()

# 保存视频题目，保存视频内容链接
video_msg = []

# 获取数据
# pprint(dict_msg['28']['post']['data'])
for item in dict_msg['28']['post']['data']:
    # print(item)
    # 视频标题
    # print(item['desc'])
    # 高清无水印视频
    pos = item['video']['bitRateList'][0]
    # print(f"https:{pos['playAddr'][0]['src']}")

    video_msg.append((item['desc'], f"https:{pos['playAddr'][0]['src']}"))

# 保存视频
for name, videoUrl in video_msg:
    VideoStream = requests.get(videoUrl, stream=true, headers=headers)
    # 获取文件大小，做进度条  转化为MB单位
    fileSize = int(VideoStream.headers['Content-Length']) / 1024 / 1024

    # 记录现在流保存了多少数据
    target = 0
    with open(f"{name}.mp4", "wb") as file:
        for debris in VideoStream.iter_content(chunk_size=1024):  # 分批写入，一次写1024字节
            target += 1024
            end = float(target / 1024 / 1024)  # 单位MB
            percent = (end / fileSize) * 100  # 已经完成的百分比
            print("\r{}MB/{}MB {:.2f}%[{}>{}]".format(int(fileSize), int(end), percent, int(int(percent) / 5) * '█',
                                                      int((100 - int(percent)) / 5) * "."), end='')
            file.write(debris)
    print(f"{name} 视频已经写入完毕")

'''
https://v26-web.douyinvod.com/b0f87053b145670990424d2bfce3fe33/634a202d/video/tos/cn/tos-cn-ve-15c001-alinc2/82b5cd0a1ca34cb6b027220680efe2a9/?a=6383&ch=10010&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C3&cv=1&br=1415&bt=1415&cs=0&ds=3&ft=t2zLrtjjM9wUxRIkn~N6~Oi_f3b0rHCfxt~MHzCclEf6p&mime_type=video_mp4&qs=0&rc=aDM5ZmZpNTo1NWlkMzdpO0Bpampqazk6ZnB5ZzMzNGkzM0AzMzEvXjNfXzUxXzYtNmM2YSMubG0ucjRfajBgLS1kLS9zcw%3D%3D&l=202210150951170101351600524F25C48D'},
https://v3-web.douyinvod.com/87ff9e926eeee52b367102b97ebb1284/634a202d/video/tos/cn/tos-cn-ve-15c001-alinc2/82b5cd0a1ca34cb6b027220680efe2a9/?a=6383&ch=10010&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C3&cv=1&br=1415&bt=1415&cs=0&ds=3&ft=t2zLrtjjM9wUxRIkn~N6~Oi_f3b0rHCfxt~MHzCclEf6p&mime_type=video_mp4&qs=0&rc=aDM5ZmZpNTo1NWlkMzdpO0Bpampqazk6ZnB5ZzMzNGkzM0AzMzEvXjNfXzUxXzYtNmM2YSMubG0ucjRfajBgLS1kLS9zcw%3D%3D&l=202210150951170101351600524F25C48D'}],
https://www.douyin.com/aweme/v1/play/?video_id=v0200fg10000cd3vmmbc77u61hpgog1g&line=0&file_id=98ff94009abf4282b7b26fac2c46606e&sign=fdc6c0af4a89cd69571ef091e12ff334&is_play_url=1&source=PackSourceEnum_PUBLISH&aid=6383',
'''
