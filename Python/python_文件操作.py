#-*-coding:GBK -*- 
# -*- coding: UTF-8 -*-

#open函数打开文件带路径
f=open("./测试.txt",'w+',encoding='utf-8')

f.write("喜欢你软起来的样子")

f.close()#刷新文件

f=open("./测试.txt",'r',encoding='utf-8')

str=f.read()

print(str)

#关闭文件
f.close()