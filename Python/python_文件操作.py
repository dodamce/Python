#-*-coding:GBK -*- 
# -*- coding: UTF-8 -*-

#open�������ļ���·��
f=open("./����.txt",'w+',encoding='utf-8')

f.write("ϲ����������������")

f.close()#ˢ���ļ�

f=open("./����.txt",'r',encoding='utf-8')

str=f.read()

print(str)

#�ر��ļ�
f.close()