#-*-coding:GBK -*- 
# -*- coding: UTF-8 -*-

print(list(map(lambda x:x*2,range(10))))

print(list(filter(None,[1,0,False,True])))

#ɸѡ����������
def Odd(x):
    return x%2
Arr=range(10)
print(list(filter(Odd,Arr)))

#lambda���ʽ��ʾ
print(list(filter(lambda x:x%2,range(10))))


##һ��������lambdab���ʽ


#def Line(x):
#    return 2*x+1
#print(Line(3))

#g= lambda x:2*x+1
#print(g(3))

##����������lambda���ʽ
#def Add(x,y):
#    return x+y
#print(Add(1,3))

#g=lambda x,y:x+y
#print(g(1,3))


