#-*-coding:GBK -*- 
# -*- coding: UTF-8 -*-

num={1,2,3,4,2,3,1,4}#ȥ���б��е��ظ�Ԫ��

num=list(set(num))#�����л��Զ�ȥ��

print(num)

#���ʼ���Ԫ�أ���֧��[]
tmp=[]
for each in num:
    if each not in tmp:
        tmp.append(each)

#��Ӽ���Ԫ��
num=set(num)
num.add(5)
print(num)

#remove�Ƴ�����Ԫ��

#���ɱ伯���޷���ӻ��޸�Ԫ��
num2=frozenset([1,2,3,4,5])
print(num2)