#-*-coding:GBK -*- 
# -*- coding: UTF-8 -*-

#�ݹ�ʵ�ֽ׳�

#def Factorial(x):
#    if (x<=1):
#        return x 
#    return Factorial(x-1)*x 

#ret=int(input("������һ��������")) 
#resault=Factorial(ret)
#print("%d�Ľ׳�Ϊ%d"%(ret,resault))

#-----------------------------------------

#ϸ������(쳲���������)(��̬�滮)

#dp=[0,1,1]
#def fib(x):
#    size=len(dp)
#    if size>x : 
#        return dp[x] 
#    else:
#        for i in range(size,x+1):
#            dp.append(dp[len(dp)-1]+dp[len(dp)-2])
#        return dp[x]
#print(fib(12))#144

#------------------------------------------

#��ŵ��
def Hanno(n,x,y,z):#n������������x,y,z�������Ӹ���,��x�ƶ���z
    if(n==1):
        print(x,"->",z)
        return
    else:
        #��n-1�����ӽ���z��x�ƶ���y��
        Hanno(n-1,x,z,y)
        #��x�����һ�����Ӵ�x�ƶ���z
        print(x,"->",z)
        #��y��n-1�����ӽ���x��y�ƶ���z��
        Hanno(n-1,y,x,z)

Hanno(3,'X','Y','Z')