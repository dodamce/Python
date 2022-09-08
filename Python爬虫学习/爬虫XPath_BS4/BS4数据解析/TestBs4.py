from bs4 import BeautifulSoup

file = open("模拟登录.html", "r", encoding='utf-8')
response = file.read()
file.close()

html_data = BeautifulSoup(response, 'lxml')
# print(html_data.h1)  # 获取h1标签代码
# print(html_data.h1.attrs)  # 获取h1标签中的属性
# print(html_data.h1['style'])  # 获取h1标签具体属性
#
# print(html_data.title.text)  # 获取title标签下的文字
#
# html_data.find()  # 找最近的满足要求的数据
#
# # 找所有满足要求的数据html_data.find_all('标签','属性')
print(html_data.find_all('body', style="background-size: cover"))
