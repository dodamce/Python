from lxml import etree

file = open("模拟登录.html", "r", encoding='utf-8')
html_data = file.read()
# print(html_data)

# html节点选择
html = etree.HTML(html_data)

# # //获取标签所有子节点，多个节点名以列表的形式返回
# print(html.xpath('//form'))  # 获取<form>节点
# print(html.xpath('//h1'))  # 获取所有的<h1>节点
#
# # /从根节点出发获取节点
# print(html.xpath('/html'))  # 获取<html>节点
#
# # .从当前路径节点
# print(html.xpath('//body')[0].xpath('./h1'))  # 获取<body>节点下的所有<h1>节点
#
# # 返回上一个节点
# print(html.xpath('//h1')[0].xpath('..'))  # 获取第一个<h1>节点的父节点<body>节点
#
# # @选取属性
# print(html.xpath('//@style'))  # 查找任意节点有class选项的节点，返回属性值的列表
#
# # 路径表达式
# print(html.xpath('/html/body/h1'))  # 获取h1节点
# print(html.xpath('/html/head/title'))  # 获取title节点
#
# print(html.xpath('//body/h1'))  # 获取h1节点

# 谓语
print(html.xpath('//body/h1[1]'))  # 获取h1列表的第一个元素
print(html.xpath('//body/h1[last()]'))  # 获取h1列表最后一个元素，last()-1是倒数第二个
print(html.xpath('//body/h1[position()<3]'))  # 获取h1列表的前两个元素
print(html.xpath('//body[@style="background-size: cover"]'))  # 获取body标签下属性为tyle="background-size: cover"的节点

# 如果想获取标签的文本 text()
print(html.xpath('//body[@style="background-size: cover"][1]/h1/text()'))

print(html.xpath('//body|//h1'))
