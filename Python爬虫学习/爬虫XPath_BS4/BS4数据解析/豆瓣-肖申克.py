import requests

from bs4 import BeautifulSoup

url = "https://movie.douban.com/subject/1292052/"

headers = {
    "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 "
        "Safari/537.36 "
}

response = requests.get(url, headers=headers)

# print(response.text)
'''
爬取豆瓣电影详情页数据
1、导演，2、演员，3、类型
4、国家，5、语言，6、上映时间
'''


def WritMsg(_file, iterable):
    for _msg in iterable:
        StrForWrit = _msg.text
        _file.write(f" {StrForWrit} ")


html_data = BeautifulSoup(response.text, 'lxml')

file = open("msg.txt", "w", encoding="utf-8")

# 电影名
file.write("电影名:\n")
file.write(html_data.find('span', property="v:itemreviewed").text)
file.write("\n--------------------------\n")

# print(html_data.find_all('div', id="info"))
html_data = html_data.find_all('div', id="info")[0]

# 导演
write = html_data.find_all('a', rel="v:directedBy")[0].text
file.write(f"导演:\n{write}\n--------------------------\n")
# 演员
file.write("演员:\n")
msg = html_data.find_all('span', class_='attrs')[2]
# 每隔五个人换行
msg = msg.find_all('a')
flag = 0
for name in msg:
    if flag == 5:
        file.write("\n")
        flag = 0
    file.write(f"{name.text}|")
    flag += 1
file.write("\n--------------------------\n")

# 类型
file.write("电影类型:\n")
WritMsg(file, html_data.find_all('span', property="v:genre"))
file.write("\n--------------------------\n")

# 制片国家/地区
dic = {}
write = html_data.text
for cheat in write.split('\n'):
    array = cheat.split(':')
    if len(array) > 1:
        dic[array[0]] = array[1]
file.write(f"制片国家/地区:\n{dic['制片国家/地区']}")
file.write("\n--------------------------\n")

# 语言
file.write(f"语言:\n{dic['语言']}")
file.write("\n--------------------------\n")

# 上映时间
file.write("上映时间:\n")
# print(html_data.find_all('span', property="v:initialReleaseDate")[0].text)
WritMsg(file, html_data.find_all('span', property="v:initialReleaseDate"))
file.write("\n--------------------------\n")

file.close()
