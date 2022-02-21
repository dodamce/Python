#-*-coding:GBK -*- 
# -*- coding: UTF-8 -*-

num={1,2,3,4,2,3,1,4}#去掉列表中的重复元素

num=list(set(num))#集合中会自动去重

print(num)

#访问集合元素，不支持[]
tmp=[]
for each in num:
    if each not in tmp:
        tmp.append(each)

#添加集合元素
num=set(num)
num.add(5)
print(num)

#remove移除集合元素

#不可变集合无法添加或修改元素
num2=frozenset([1,2,3,4,5])
print(num2)