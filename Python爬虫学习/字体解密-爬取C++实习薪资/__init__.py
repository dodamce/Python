import requests
import re
from encode import get_dict_encode
from lxml import etree
import wget
import os
from mySQL import MySQL

url = "https://www.shixiseng.com/interns?page=1&type=intern&keyword=C%2B%2B&area&months&days&degree&official&enterprise" \
      "&salary=-0&publishTime&sortType&city=%E5%85%A8%E5%9B%BD&internExtend "

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 '
                  'Safari/537.36 '
}

response = requests.get(url, headers=headers)

if response.status_code != 200:
    exit(-1)

html = response.text
findHand = etree.HTML(html)
# 获取实习类型
typeName = re.findall('<a href=".*?" title=".*?" target="_blank" class="title ellipsis font" data-v-2d75efc8>(.*?)</a>',
                      html)

# 获取实习薪资
money = re.findall('<span class="day font" data-v-2d75efc8>(.*?)</span>', html)

# 网站的file文件会变化，动态获取一下
# @font-face {    font-family: myFont;    src: url(/interns/iconfonts/file?rand=0.6389010343293982);}
root = "https://www.shixiseng.com"
filepath = root + re.findall('@font-fac.*?src: url(.*?);}', html)[0][1:-2]  # 跳过路径前后的()
print(filepath)
wget.download(filepath, "./file")

encode_dict = get_dict_encode()

# 删除file文件缓存
os.remove('./file')


# 解密函数
def decode(Str):
    for code in encode_dict.keys():
        if code in Str:
            Str = str(Str).replace(code, encode_dict[code])
    return Str


# 解密实习类型
name_decode = []
for name in typeName:
    name_decode.append(decode(name))

# 解密薪资
money_decode = []
for item in money:
    money_decode.append(decode(item))

# 获取公司名称
title = re.findall('<a title=".*?" href="javascript:;" class="title ellipsis" data-v-2d75efc8>(.*?)</a>', html)

# 获取上班地点，时间
work_msg = []
data = findHand.xpath('//*[@id="__layout"]/div/div[2]/div[2]/div[1]/div[1]/div[1]/div/div[1]/div[1]/p[2]/span/text()')
# print(data, len(data))

# 5个5个组合
for pos in range(0, len(data), 5):
    work_msg.append((data[pos] + data[pos + 1] + decode(data[pos + 2]) + data[pos + 3] + decode(data[pos + 4])))

# 获取额外信息
msg = []
#                      //*[@id="__layout"]/div/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]
for time in range(1, 21):
    msg.append(
        findHand.xpath(
            f'//*[@id="__layout"]/div/div[2]/div[2]/div[1]/div[1]/div[1]/div[{time}]/div[2]/div[1]/span/text()'))

# 将数据保存到数据库中
mysql = MySQL(_user='root', _passwd='000000', _database='python_sql')

# 创建表
sql = '''
create table if not exists msg(name varchar(40),work_type varchar(40),money varchar(40),time varchar(40),help varchar(40))charset='utf8'
'''
mysql.CreateDatabase(sql)

for work_title, work_type, work_money, work_time, work_help in zip(title, name_decode, money_decode, work_msg, msg):
    print(f"INF0:{work_title, work_type, work_money, work_time, work_help}正在写入")
    msg_tmp = ""
    for i in work_help:
        msg_tmp += str(i + ' ')
    mysql.InsertSQL("insert into msg(name,work_type,money,time,help) value('%s','%s','%s','%s','%s');" % (
        str(work_title), str(work_type), str(work_money), str(work_time), msg_tmp))

mysql.Close()
