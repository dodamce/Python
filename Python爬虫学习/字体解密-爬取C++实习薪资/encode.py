import json
from fontTools.ttLib import TTFont
import title_to_code


# Json编码转化数字
def toUnicode(oneStr):
    t = oneStr
    if t[:3] == 'uni': t = t.replace('uni', '\\u')
    if t[:2] == 'uF': t = t.replace('uF', '\\u')
    return json.loads(f'"{t}"')


def get_dict_encode():
    unicode_dict = {}
    dict_TitleToCode = title_to_code.get_dict_TitleToCode()

    ttf = TTFont('file')  # 读取下载后的文件

    m_dict = ttf.getBestCmap()

    # 保存还没有解码的数字，字母编码
    residue = {}
    # 获取汉字编码
    for code, charTitle in m_dict.items():
        try:
            # 原编码写入字典中
            unicode_dict[chr(code)] = toUnicode(charTitle)
            str_data = str(chr(code).encode('unicode_escape'))
            # print(str_data)
            # 转化的汉字编码前有\u需要替换成网页的&#x
            if '\\u' in str_data:
                unicode_dict['&#x' + str_data[5:-1]] = toUnicode(charTitle)
        except:
            residue[charTitle] = chr(code)
            pass

    # 获取数字，字母的编码:
    # 字典排序
    residue = sorted(residue.items(), key=lambda x: x[0], reverse=False)
    STR = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    for index, title in enumerate(residue):
        if dict_TitleToCode.get(title[0]):  # 如果找到的标题中有还剩下的数字字母标题，则添加到字典里
            unicode_dict[dict_TitleToCode[title[0]]] = STR[index]
            # dict_num[dict_TitleToCode[title[1]]] = STR[index]
            # 原编码也写一份
            unicode_dict[title[1]] = STR[index]

    print(unicode_dict)
    return unicode_dict

#
# get_dict_encode()
