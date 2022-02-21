#-*-coding:GBK -*- 
# -*- coding: UTF-8 -*-

#类似C++中的Map
name={"小明":123,"小红":124,"小刚":125}#姓名与学号连接起来Key:Value
print("小红的学号为：%d"%name["小红"])

#创建空字典
dirct={}

#dict函数创建字典
dirct1=dict((['A',97],['B',98],['C',99]))
print(dirct1['B'])

#=创建字典
dirct2=dict(小明=123,小红=124,小刚=124)#注意字符串不要用""
print(dirct2)

#通过键改变Value
dirct2["小明"]=127
print(dirct2["小明"])
#如果没有键值，则会执行插入操作

#字典的内件方法
dirct=dirct.fromkeys((1,2,3),"Value")#创建键值，Value为Value
print(dirct)

#访问字典方法
dirct3={}
dirct3=dirct3.fromkeys(range(32),"Number")
#for i in dirct3.keys():
#    print(i)
#for i in dirct3.values():
#    print(i)
for i in dirct3.items():#打印所有项
    print(i)

#get访问字典中不存在的值，返回None
print(dirct1.get(32))

#判断元素是否在字典中
if 33 in dirct3:
    print("33在diect3中")
else:
    print("33不在dirce3中")

#清空字典
dirct3.clear()

#拷贝字典地址不同
tmp=dirct3.copy()
tmp2=dirct3 #地址相同
print("tmp",id(tmp),"tmp2",id(tmp2),"dirct3",id(dirct3))

#添加字典元素
dirct1.update(dirct2)#1中添加了2
print(dirct1)

