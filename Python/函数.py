#-*-coding:GBK -*- 
# -*- coding: UTF-8 -*-

def Add(num1,num2):
    return num1+num2;

print(Add(2,3))

def Printf(Str):
    print("%s���β�"%Str)

print(Printf.__doc__)#����Ĭ������
Printf("Hello ")

#�ؼ��ֲ���
def SaySome(name="****",word="*****"):#Ĭ�ϲ���
    print(name,"->",word)

SaySome(word="word",name="Hello")#�ؼ��ֲ���
SaySome()

#�ռ�����
def Cout(*name):
    print("�����ĸ���Ϊ",len(name))
    if(len(name)>1):
        print("�ڶ�������Ϊ��",name[1])
Cout("hello",1)

#�շ���ֵ����

def Test():
    print("�޷���ֵ����")
tmp=Test()#���ܿշ���ֵ�ĺ���
print(type(tmp))

#�ں�����ʹ��ȫ�ֱ���
cout=10#ȫ��
def Mod():
    #cout=5
    #print(cout)
    global cout
    cout=5#����ʹ���ⲿcout
    print(cout)
Mod()
print(cout)

#��Ƕ����
def Fun1(cout):
    print("Fun1������")
    def Fun2():
        print("Fun2������")
    if(cout>1):
        Fun2()#�������Ĳ���>1�����ڵ���Fun2,�ⲿ�޷�����
Fun1(1)
Fun1(2)

#�����հ�
def BiBao(x):
    def Y(y):
        return x*y
    return Y
i=BiBao(4)
print(i)
print(i(5))
print(BiBao(4)(5))

#�ۺ�
def ZongHe():
    x=[5]
    def Y():
        x[0]*=5
        return x[0]
    return Y
print(ZongHe()())
def ZongHe2():
    x=5
    def Y():
        nonlocal x#����x���Ǿֲ�����
        x*=5
        return x
    return Y()
print(ZongHe2())