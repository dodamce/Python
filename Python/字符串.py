#-*-coding:GBK -*- 
# -*- coding: UTF-8 -*-

#字符串不可修改，如要修改使用切片

#str1="xiaoxie"
##转首字母大写
#print(str1.capitalize())
#str2="XIAODA"
#print(str2.casefold())
#print(str2.center(15))#保证字符串长度6，不够空格
#print(str2.endswith("DA"))#检测是否是DA结尾
#str3="NUC\tDodamce"
#print("str3=",str3)
#print(str3.expandtabs(16))#将Talbe键转空格
##其他常用接口见博客论坛

##替换参数fomat
#print("{0} Love {1}".format("I","You"))

#print("{a} Love {b}".format(a="I",b="You"))

#print("{{{0}".format("linux"))#用{转义

#print("{0:.1f}.{1}".format(26.384,"GB"))#{}中:代表格式化的开始打印26.4GB

#print("%c"%97)
#print("%c %c %c"%(97,98,99))#有C语言的味道了
#print("I Love %s"%"You")

str="A:abc"
print(str.split(":",4))