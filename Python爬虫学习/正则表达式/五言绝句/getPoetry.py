from lxml import etree


# 合并列表中所有字符串
def GetMsg(iterable):
    ret = ""
    for i in iterable:
        ret += i
    return ret


# 获取古诗题目，作者
def _getPoetryTitle(data):
    html = etree.HTML(data)
    title = GetMsg(html.xpath('//*[@id="sonsyuanwen"]/div[1]/h1/text()'))
    msg = GetMsg(html.xpath('//*[@id="sonsyuanwen"]/div[1]/p/a/text()'))
    return title + " " + msg


# 获取古诗正文
def _getPoetryText(data):
    html = etree.HTML(data)
    # //*[@id = "sonsyuanwen"]/div[1]/div[2]
    msg = GetMsg(html.xpath('//*[@id ="sonsyuanwen"]/div[1]/div[2]/text()'))
    return msg
