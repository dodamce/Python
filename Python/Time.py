import time as t

class MyTime():

    def __init__(self):
        self.unit=["年","月","天","小时","分钟","秒"]
        self.title="未开始计时"
        self.borrow = [0, 12, 31, 24, 60, 60]
        self.lasted=[]
        self.begin=0
        self.end=0

    def __str__(self):
        return self.title

    __repr__=__str__
    
    #开始计时
    def start(self):
        self.begin=t.localtime()
        print("开始计时")

    #停止计时
    def stop(self):
        if not self.begin:
            print("请先调用start计时")
        else:
            self.end=t.localtime()
            self._calc()
            print("计时结束")


    #计算时间
    def _calc(self):
        self.lasted=[]
        self.title="总共运行了"
        for pos in range(6):
            tmp=self.end[pos]-self.begin[pos]
            ## 低位不够减，需向高位借位
            if tmp<0:
                i=1
                while self.lasted[pos-i]<1:
                    self.lasted[pos-i]+=self.borrow[pos-i]-1
                    self.lasted[pos-i-1]-=1
                    i+=1
                self.lasted.append(self.borrow[index]+tmp)
                self.lasted[pos-1]-=1
            else:
                self.lasted.append(tmp)
            # 由于高位随时会被借位，所以打印要放在最后
        for pos in range(6):
            if self.lasted[pos]:
                    self.title+=str(self.lasted[pos])+self.unit[pos]
                    
        #清空计时单位
        self.begin=0
        self.end=0

    #  +运算符重载
    def __add__(self,other):
        title="总共运行了"
        resault=[]
        for pos in range(6):
            resault.append(self.lasted[pos]+other.lasted[pos])
            if resault[pos]:
                title+=str(resault[pos])+self.unit[pos]
        return title

#主函数
T=MyTime()
print(T)
print(T.stop())
T.start()
input("输入任意按键停止计时")
T.stop()
print(T)
print("--------------------")
T2=MyTime()
T2.start()
input("输入任意按键停止计时")
T2.stop()
print(T2)
print("----------------------")
print(T+T2)


    
