# 正式通过爬虫获取数据
import requests
import re
from pprint import pprint
import subprocess
import time
import os

from concurrent.futures import ThreadPoolExecutor

# 爬取的视频保存路径
videoPath = "./videos"
# 爬取视频的缓存文件夹
buffPath = "./videos/buff"

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 '
                  'Safari/537.36 ',
    'referer': 'https://www.bilibili.com/'
}


def MergeData(music_url, video_url, output_url):
    cmd = f"ffmpeg.exe -i {music_url} -i {video_url} -acodec copy -vcodec copy {output_url} -loglevel quiet"
    subprocess.run(cmd, shell=True)


# 消费者线程，执行下载任务
poolDel = ThreadPoolExecutor(10)


def download(music_url, move_url, music_path, move_path, output_path):
    # 采用流的方式传输数据
    MusicStream = requests.get(music_url, stream=True, headers=headers)
    with open(music_path, 'wb') as file:
        for debris in MusicStream.iter_content(chunk_size=1024):
            file.write(debris)
    print("INFO:音频数据下载完成 " + music_path)
    VideoStream = requests.get(move_url, stream=True, headers=headers)
    with open(move_path, 'wb') as file:
        for debris in VideoStream.iter_content(chunk_size=1024):
            file.write(debris)
    print("INFO:视频数据下载完成" + move_path)

    # 组装数据
    MergeData(music_path, move_path, output_path)
    print("INFO:数据组装完成，数据组装路径:" + output_path)


def GetVideo(title, videoUrl):
    # 根据url提取视频信息
    resp = requests.get(videoUrl, headers=headers)
    js = re.findall('<script>window.__playinfo__=(.*?)</script>', resp.text)
    # 将js数据转化为字典
    null = None  # eval函数需要定义null
    # 获取音频信息
    musicUrl = eval(js[0])['data']['dash']['audio'][0]['backupUrl'][0]
    print('音频数据链接:' + musicUrl)
    musicSavePath = buffPath + f"/{title}.mp3"
    # 视频链接
    moveUrl = eval(js[0])['data']['dash']['video'][0]['backupUrl'][0]
    print('视频数据链接:' + moveUrl)
    moveSavePath = buffPath + f"/{title}.mp4"

    # 最后视频保存位置
    outSavePath = videoPath + f"/{title}.mp4"
    # 下载数据
    # lambda cxp:test(*cxp),(j ,k)
    poolDel.submit(lambda fuc: download(*fuc), (musicUrl, moveUrl, musicSavePath, moveSavePath, outSavePath))
    # download(musicUrl, moveUrl, musicSavePath, moveSavePath, outSavePath)


if __name__ == '__main__':
    up = '487939159'
    page = 1

    while True:
        upMsgUrl = f'https://api.bilibili.com/x/space/arc/search?mid={up}&pn={page}&ps=30&index=1'
        response = requests.get(upMsgUrl, headers=headers)
        if response.status_code == 200:
            page += 1
            # print(response.json())
            json = response.json()
            UpList = json['data']['list']['vlist']  # 为空跳出
            if UpList:
                for item in UpList:
                    # 获取视频BV号链接
                    print('INFO:get video url success title: ' + item['title'])

                    # 重复的视频不需要下载
                    files = os.listdir(videoPath)
                    if item['title'] + ".mp4" not in files:
                        # 获取视频链接和视频名称
                        GetVideo(item['title'], f"https://www.bilibili.com/video/{item['bvid']}")
                    else:
                        print(f"INFO:{item['title']}视频已经下载完毕，请删除后再下载\n--------------------")

            else:
                print("\n-----------------\nINFO:这个Up的所有视频全部爬取完毕！\n")
                break
            time.sleep(1)
        else:
            print('网页请求失败' + response.text)
            break
