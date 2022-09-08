import requests

from getLink import _getLink
from getPoetry import _getPoetryText, _getPoetryTitle

url_root = "https://so.gushiwen.cn"

main_page = "/gushi/tangshi.aspx"

headers = {
    'user-agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 '
        'Safari/537.36 '
}

if __name__ == '__main__':
    response = requests.get(url_root + main_page, headers=headers)

    file = open("五言绝句.txt", 'w', encoding='utf-8')

    if response.status_code != 200:
        print('获取主页面失败，程序退出')
        exit(-1)
    html = response.text

    # _getLink获取所有要请求的链接
    link = _getLink(html)

    # 请求每一个链接
    for _url in link:
        _response = requests.get(url_root + _url, headers=headers)
        if response.status_code != 200:
            print('获取子页面失败，程序退出')
            exit(-1)
        data = _response.text
        if file is None:
            exit(-1)
        print(f'{_getPoetryTitle(data)}爬取开始')
        file.write(f"                              {_getPoetryTitle(data)}\n")
        # 写入取诗歌内容
        file.write(_getPoetryText(data))
        file.write("====================================================\n")
        print(f'{_getPoetryTitle(data)}爬取结束')

    # 写入完成后关闭文件
    file.close()
