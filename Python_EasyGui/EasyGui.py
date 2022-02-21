import easygui as Box
import random

Box.msgbox("猜数字游戏开始","Dodamce")

secret=random.randint(1,10)#生成1到10随机数

msg="请输入要猜的数字(1-10)："
title="猜数字游戏"
guss=Box.integerbox(msg,title,lowerbound=1,upperbound=10)
#integerbox(msg='', title=' ', default=None, lowerbound=0, upperbound=99, image=None, root=None)
#integerbox() 为用户提供一个简单的输入框，用户只能输入范围内（lowerbound 参数设置最小值，upperbound 参数设置最大值）的整型数值，否则会要求用户重新输入。
#返回值为用户输入的字符串。
while True:
    if guss==secret:
        Box.msgbox("猜对了！")
        break
    else:
        if guss>secret:
            Box.msgbox("猜大了")
        else:
            Box.msgbox("猜小了")
        guss=Box.integerbox(msg,title,lowerbound=1,upperbound=10)

Box.msgbox("退出游戏")
