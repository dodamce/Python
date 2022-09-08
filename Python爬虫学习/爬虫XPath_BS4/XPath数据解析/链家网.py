import requests

from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 '
                  'Safari/537.36 '
}

# 需要爬取的数据
# //*[@id="content"]/div[1]/ul/li[1]/div[1]
# 标题: print(html.xpath('//*[@id="content"]/div[1]/ul/li/div[1]/div[1]/a/text()'))
# 位置:
# pos_first = html.xpath('//*[@id="content"]/div[1]/ul/li/div[1]/div[2]/div/a[1]/text()')
# pos_sec = html.xpath('//*[@id="content"]/div[1]/ul/li/div[1]/div[2]/div/a[2]/text()')
# 价格: //*[@id="content"]/div[1]/ul/li[1]/div[1]/div[6]
# print(html.xpath('//*[@id="content"]/div[1]/ul/li/div[1]/div[6]/div[1]/span/text()'))
# 每平米多少元
# print(html.xpath('//*[@id="content"]/div[1]/ul/li/div[1]/div[6]/div[2]/span/text()'))

# 爬取4页数据
file = open('data.csv', 'w+', encoding='gbk')
file.write("标题,区域,位置,价格,一平米多少元\n")
for page in range(1, 5):
    print(f'正在爬取第{page}页数据')
    url = f'https://ty.lianjia.com/ershoufang/pg{page}/'
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print('网页请求失败')
    else:
        html = etree.HTML(response.text)
        title = html.xpath('//*[@id="content"]/div[1]/ul/li/div[1]/div[1]/a/text()')
        pos_first = html.xpath('//*[@id="content"]/div[1]/ul/li/div[1]/div[2]/div/a[1]/text()')
        pos_sec = html.xpath('//*[@id="content"]/div[1]/ul/li/div[1]/div[2]/div/a[2]/text()')
        prise = html.xpath('//*[@id="content"]/div[1]/ul/li/div[1]/div[6]/div[1]/span/text()')
        per_prise = html.xpath('//*[@id="content"]/div[1]/ul/li/div[1]/div[6]/div[2]/span/text()')
        msg = zip(title, pos_first, pos_sec, prise, per_prise)
        print('正在写入中')
        for _title, _pos_first, _pos_sec, _prise, _per_prise in msg:
            file.write(f'{_title},{_pos_first},{_pos_sec},{_prise}万,{_per_prise}\n')
print('4页数据爬取完毕')
file.close()
