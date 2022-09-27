from fontTools.ttLib import TTFont
from bs4 import BeautifulSoup


def get_xml():
    ttf = TTFont('file')
    ttf.saveXML('code.xml')

    xml_file = open('code.xml', 'r')
    xml = xml_file.read()
    xml_file.close()

    find = BeautifulSoup(xml, 'xml')

    # 返回这个标签的值
    return str(find.cmap_format_4)
