from creat_xml import get_xml
import re


def get_dict_TitleToCode():
    dictTitleToCode = {}
    xml = get_xml()

    for data in xml.splitlines():
        if '<map' in data:
            pair = re.findall('<map code="(.*?)" name="(.*?)"/>', data)
            dictTitleToCode[pair[0][1]] = '&#x' + pair[0][0][2:]  # [2:]跳过代表16进制的0x,同时添加上这个网页用来分割字符的&#x
    return dictTitleToCode
