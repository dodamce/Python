# 合并视频片段
# 下载
import subprocess

from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED

import requests

import os


def get_m3u8(url, video_id):
    response = requests.get(url)
    # 获取m3u8文件所有视频片段
    data = []
    index = 1
    path = f'E:/PythonCode/m3u8视频获取/delvideo/VideoBuff/{video_id}'
    # 创建新文件夹
    os.mkdir(path)
    file = open(path + "/video_list", 'w')
    for line in response.text.splitlines():
        if '.ts' in line:
            data.append((index, 'https://tx-safety-video.acfun.cn/mediacloud/acfun/acfun_video/' + line))
            # 将输出的视频写到路径文件中
            file.write(f"file 'E:\\PythonCode\\m3u8视频获取\\delvideo\\VideoBuff\\{video_id}\\{index}.mp4'\n\n")
            index += 1

    file.close()
    return data


def _download(name, url, time, video_id):
    with open(f'./delvideo/VideoBuff/{video_id}/{name}.mp4', 'wb') as file:
        file.write(requests.get(url).content)
    print(f"{time}时间发布的 第{name}段视频写入完成")


def download(url, name, video_id):
    # 下载所有的m3u8视频并拼接,直接通过追加方式写入视频文件
    # 为新来的任务创建文件夹
    split = get_m3u8(url, video_id)

    # 使用线程池多线程下载
    pool = ThreadPoolExecutor(10)
    task_list = []
    for item in split:
        task_list.append(pool.submit(lambda fuc: _download(*fuc), (item[0], item[1], name, video_id)))

    # 等待线程池所有的线程结束后组装
    wait(task_list, return_when=ALL_COMPLETED)
    print(f'{name}发布的视频m3u8下载完毕 正在组装视频')
    # 组装视频
    # ffmpeg.exe -f concat -safe 0 -i ./delvideo/VideoBuff/video_list -c copy -y o1.mp4
    cmd = f"D:\\ffmpeg-5.0.1-essentials_build\\ffmpeg-5.0.1-essentials_build\\bin\\ffmpeg.exe -f concat -safe 0 -i " \
          f"./delvideo/VideoBuff/{video_id}/video_list -c copy -y ./video/{name}.mp4 "
    subprocess.run(cmd, shell=True)
