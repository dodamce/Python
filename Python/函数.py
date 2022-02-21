#-*-coding:GBK -*- 
# -*- coding: UTF-8 -*-

def Add(num1,num2):
    return num1+num2;

print(Add(2,3))

def Printf(Str):
    print("%s是形参"%Str)

print(Printf.__doc__)#函数默认属性
Printf("Hello ")

#关键字参数
def SaySome(name="****",word="*****"):#默认参数
    print(name,"->",word)

SaySome(word="word",name="Hello")#关键字参数
SaySome()

#收集参数
def Cout(*name):
    print("参数的个数为",len(name))
    if(len(name)>1):
        print("第二个参数为：",name[1])
Cout("hello",1)

#空返回值函数

def Test():
    print("无返回值函数")
tmp=Test()#接受空返回值的函数
print(type(tmp))

#在函数内使用全局变量
cout=10#全局
def Mod():
    #cout=5
    #print(cout)
    global cout
    cout=5#声明使用外部cout
    print(cout)
Mod()
print(cout)

#内嵌函数
def Fun1(cout):
    print("Fun1调用中")
    def Fun2():
        print("Fun2调用中")
    if(cout>1):
        Fun2()#如果传入的参数>1函数内调用Fun2,外部无法访问
Fun1(1)
Fun1(2)

#函数闭包
def BiBao(x):
    def Y(y):
        return x*y
    return Y
i=BiBao(4)
print(i)
print(i(5))
print(BiBao(4)(5))

#综合
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
        nonlocal x#声明x不是局部变量
        x*=5
        return x
    return Y()
print(ZongHe2())