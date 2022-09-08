import requests

url = "https://img.alicdn.com/imgextra/i1/6000000005886/O1CN01eFZshV1tLq17L2m5X_!!6000000005886-0-octopus.jpg"

header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=header)

# 获取图片类型
img_name = url.split('/')[-1]

with open(img_name, 'wb') as file:
    file.write(response.content)
