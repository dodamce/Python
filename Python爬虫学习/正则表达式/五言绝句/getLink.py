from bs4 import BeautifulSoup
import re


# 获取五言绝句代码链接，以列表的形式返回
def _getLink(html):
    html_data = BeautifulSoup(html, 'lxml')
    five_html = str(html_data.find_all('div', class_="typecont")[0])

    ret = re.findall('<span><a href="(.*?)" target="_blank">', five_html)
    return ret
