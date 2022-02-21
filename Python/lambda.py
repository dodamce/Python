#-*-coding:GBK -*- 
# -*- coding: UTF-8 -*-

print(list(map(lambda x:x*2,range(10))))

print(list(filter(None,[1,0,False,True])))

#筛选奇数过滤器
def Odd(x):
    return x%2
Arr=range(10)
print(list(filter(Odd,Arr)))

#lambda表达式表示
print(list(filter(lambda x:x%2,range(10))))


##一个参数的lambdab表达式


#def Line(x):
#    return 2*x+1
#print(Line(3))

#g= lambda x:2*x+1
#print(g(3))

##两个参数的lambda表达式
#def Add(x,y):
#    return x+y
#print(Add(1,3))

#g=lambda x,y:x+y
#print(g(1,3))


