#-*-coding:GBK -*- 
# -*- coding: UTF-8 -*-

#递归实现阶乘

#def Factorial(x):
#    if (x<=1):
#        return x 
#    return Factorial(x-1)*x 

#ret=int(input("请输入一个正整数")) 
#resault=Factorial(ret)
#print("%d的阶乘为%d"%(ret,resault))

#-----------------------------------------

#细胞分裂(斐波那契数列)(动态规划)

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

#汉诺塔
def Hanno(n,x,y,z):#n代表盘子数，x,y,z代表柱子个数,从x移动到z
    if(n==1):
        print(x,"->",z)
        return
    else:
        #将n-1个盘子借助z从x移动到y上
        Hanno(n-1,x,z,y)
        #将x下最后一个盘子从x移动到z
        print(x,"->",z)
        #将y上n-1个盘子借助x从y移动到z上
        Hanno(n-1,y,x,z)

Hanno(3,'X','Y','Z')