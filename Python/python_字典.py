#-*-coding:GBK -*- 
# -*- coding: UTF-8 -*-

#����C++�е�Map
name={"С��":123,"С��":124,"С��":125}#������ѧ����������Key:Value
print("С���ѧ��Ϊ��%d"%name["С��"])

#�������ֵ�
dirct={}

#dict���������ֵ�
dirct1=dict((['A',97],['B',98],['C',99]))
print(dirct1['B'])

#=�����ֵ�
dirct2=dict(С��=123,С��=124,С��=124)#ע���ַ�����Ҫ��""
print(dirct2)

#ͨ�����ı�Value
dirct2["С��"]=127
print(dirct2["С��"])
#���û�м�ֵ�����ִ�в������

#�ֵ���ڼ�����
dirct=dirct.fromkeys((1,2,3),"Value")#������ֵ��ValueΪValue
print(dirct)

#�����ֵ䷽��
dirct3={}
dirct3=dirct3.fromkeys(range(32),"Number")
#for i in dirct3.keys():
#    print(i)
#for i in dirct3.values():
#    print(i)
for i in dirct3.items():#��ӡ������
    print(i)

#get�����ֵ��в����ڵ�ֵ������None
print(dirct1.get(32))

#�ж�Ԫ���Ƿ����ֵ���
if 33 in dirct3:
    print("33��diect3��")
else:
    print("33����dirce3��")

#����ֵ�
dirct3.clear()

#�����ֵ��ַ��ͬ
tmp=dirct3.copy()
tmp2=dirct3 #��ַ��ͬ
print("tmp",id(tmp),"tmp2",id(tmp2),"dirct3",id(dirct3))

#����ֵ�Ԫ��
dirct1.update(dirct2)#1�������2
print(dirct1)

