import requests

# 确认数据链接状态

url = "	https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png"

header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}

# stream=True 获取到的类似生成器 stream=False 获取到的类似列表,一般是用来读取大量数据的,使用列表内存可能不足
# 下载视频，或者图片时通常会使用这个选项，读取一张照片不需要这个选项

# response = requests.get(url, headers=header, stream=True)
response = requests.get(url, headers=header)  # 图片是二进制数据，二进制数据没有编码

# 字符串切割，找到图片类型
img = url.split('/')[-1]

with open(img, "wb") as file:
    # 写入图片，视频。音乐时需要用字节流的形式写入
    file.write(response.content)
