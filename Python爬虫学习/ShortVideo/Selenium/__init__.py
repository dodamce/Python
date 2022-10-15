import requests
import re
from urllib import parse
from selenium import webdriver
import time
import copy

from pprint import pprint

# 2022年 10月15日 生效

# 刘思瑶主页
url = "https://www.douyin.com/user/MS4wLjABAAAAaSfA0HM0mHsoLdNIiwcFfUUYmmD_xGE6IEni35uxzkE"

# https://www.douyin.com/video/7112422293950696745

driver = webdriver.Chrome()

"https://www.douyin.com/note/7041182362499173672"

driver.get(url)

for page in range(0, 200, 5):  # 实现动态网页下拉
    js = 'window.scrollTo(0,%s)' % (page * 100)
    page += 5
    driver.execute_script(js)
    time.sleep(0.3)

data = parse.unquote(driver.page_source)
pprint(data)

urls = re.findall('<a href="(.*?)" class="B3AsdZT9 chmb2GX8" target="_blank" rel="noopener noreferrer">', data,
                  re.S)
print(urls)
print(len(urls))

# 获取有效信息
# data = parse.unquote(re.findall('<script id="RENDER_DATA" type="application/json">(.*?)</script>',
#                                 driver.page_source, re.S)[0])

# pprint(dict_msg)

# 保存视频题目，保存视频内容链接
# video_msg = []
#
# # 获取数据
# # pprint(dict_msg['28']['post']['data'])
# for item in dict_msg['28']['post']['data']:
#     # print(item)
#     # 视频标题
#     # print(item['desc'])
#     # 高清无水印视频
#     pos = item['video']['bitRateList'][0]
#     # print(f"https:{pos['playAddr'][0]['src']}")
#
#     video_msg.append((item['desc'], f"https:{pos['playAddr'][0]['src']}"))
#
# # 保存视频
# for name, videoUrl in video_msg:
#     VideoStream = requests.get(videoUrl, stream=true, headers=headers)
#     # 获取文件大小，做进度条  转化为MB单位
#     fileSize = int(VideoStream.headers['Content-Length']) / 1024 / 1024
#
#     # 记录现在流保存了多少数据
#     target = 0
#     with open(f"{name}.mp4", "wb") as file:
#         for debris in VideoStream.iter_content(chunk_size=1024):  # 分批写入，一次写1024字节
#             target += 1024
#             end = float(target / 1024 / 1024)  # 单位MB
#             percent = (end / fileSize) * 100  # 已经完成的百分比
#             print("\r{}MB/{}MB {:.2f}%[{}>{}]".format(int(fileSize), int(end), percent, int(int(percent) / 5) * '█',
#                                                       int((100 - int(percent)) / 5) * "."), end='')
#             file.write(debris)
#     print(f"{name} 视频已经写入完毕")
#
# '''
# https://v26-web.douyinvod.com/b0f87053b145670990424d2bfce3fe33/634a202d/video/tos/cn/tos-cn-ve-15c001-alinc2/82b5cd0a1ca34cb6b027220680efe2a9/?a=6383&ch=10010&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C3&cv=1&br=1415&bt=1415&cs=0&ds=3&ft=t2zLrtjjM9wUxRIkn~N6~Oi_f3b0rHCfxt~MHzCclEf6p&mime_type=video_mp4&qs=0&rc=aDM5ZmZpNTo1NWlkMzdpO0Bpampqazk6ZnB5ZzMzNGkzM0AzMzEvXjNfXzUxXzYtNmM2YSMubG0ucjRfajBgLS1kLS9zcw%3D%3D&l=202210150951170101351600524F25C48D'},
# https://v3-web.douyinvod.com/87ff9e926eeee52b367102b97ebb1284/634a202d/video/tos/cn/tos-cn-ve-15c001-alinc2/82b5cd0a1ca34cb6b027220680efe2a9/?a=6383&ch=10010&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C3&cv=1&br=1415&bt=1415&cs=0&ds=3&ft=t2zLrtjjM9wUxRIkn~N6~Oi_f3b0rHCfxt~MHzCclEf6p&mime_type=video_mp4&qs=0&rc=aDM5ZmZpNTo1NWlkMzdpO0Bpampqazk6ZnB5ZzMzNGkzM0AzMzEvXjNfXzUxXzYtNmM2YSMubG0ucjRfajBgLS1kLS9zcw%3D%3D&l=202210150951170101351600524F25C48D'}],
# https://www.douyin.com/aweme/v1/play/?video_id=v0200fg10000cd3vmmbc77u61hpgog1g&line=0&file_id=98ff94009abf4282b7b26fac2c46606e&sign=fdc6c0af4a89cd69571ef091e12ff334&is_play_url=1&source=PackSourceEnum_PUBLISH&aid=6383',
# '''
