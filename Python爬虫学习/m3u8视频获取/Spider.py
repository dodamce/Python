from pprint import pprint

import requests
import re
import json
import threading

# 用户的主页url
from delvideo.MergeVideo import download

url = 'https://www.acfun.cn/u/1418766'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 '
                  'Safari/537.36 Edg/106.0.1370.52 '
}

response = requests.get(url, headers=headers)

# 获取用户的第一页数据
video = re.findall(
    '<a href="(.*?)" target="_blank" class="ac-space-video weblog-item" data-wbinfo=.*?>', response.text)
video = ['https://www.acfun.cn' + _url for _url in video]

# 分别请求每一个视频，获取每个视频中的m3u8链接
task = []

for item in video:
    ret = requests.get(item, headers=headers)
    dic = re.findall('window.pageInfo = window.videoInfo = (.*?);', ret.text)[0]
    js = json.loads(dic)
    # pprint(js['createTime'])
    time = js['createTime']
    # 通过id创建不同的视频缓冲区，线程池每一个线程都有自己的工作目录，这样每个多线程内部也是多线程的，效率拉满
    video_id = js['currentVideoId']
    js = json.loads(js['currentVideoInfo']['ksPlayJson'])
    m3u8 = js['adaptationSet'][0]['representation'][0]['url']

    # 多线程发布任务
    print(f"INFO:{time}发布的视频正在爬取中....")
    # task.append(pool.submit(lambda fuc: download(*fuc), (m3u8, time, video_id)))
    thread = threading.Thread(target=download, args=(m3u8, time, video_id))
    thread.run()
    task.append(thread)
# 等待线程池退出
print("INFO:用户主页多有视频任务发布完成，请耐心等待爬取完毕")
# 等待线程结束
for i in task:
    i.join()
