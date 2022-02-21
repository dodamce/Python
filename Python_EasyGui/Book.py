#-*-coding:GBK -*- 

import easygui as Box
import os

FilePath=Box.fileopenbox(default="*.txt")
#fileopenbox(msg=None, title=None, default='*', filetypes=None, multiple=False)
#fileopenbox() 函数用于提供一个对话框，返回用户选择的文件名（带完整路径），如果用户选择 “Cancel” 则返回 None。
#默认显示所有txt文件

with open(FilePath,encoding='gbk',errors='ignore') as File:#with语句，自动关闭文件等操作
    title=os.path.basename(FilePath)#返回文件名
    msg="文件[%s]内容为："%title
    text=File.read()
    text_after=Box.textbox(msg,title,text)
#textbox(msg='', title=' ', text='', codebox=False, callback=None, run=True)
#textbox() 函数默认会以比例字体（参数 codebox=True 设置为等宽字体）来显示文本内容（自动换行），这个函数适合用于显示一般的书面文字。

if text !=text_after[:-1]:#b = a[:-1]表示从a的第一个元素复制到最后一个元素之前给b
    choice = Box.buttonbox("检测到文件内容发生改变，请选择以下操作：", "警告", ("覆盖保存", "放弃保存", "另存为..."))
    if choice =="覆盖保存":
        with open(FilePath,'w',encoding='gbk',errors='ignore') as File:
            File.write(text_after[:-1])
    if choice =="放弃保存":
        pass #当你不清楚要写的内容时，就可以用pass来进行填坑。
    if choice =="另存为...":
        NewPath=Box.filesavebox(default=".txt")
#filesavebox(msg=None, title=None, default='', filetypes=None)
#filesavebox() 函数提供一个对话框，让用于选择文件需要保存的路径（带完整路径），如果用户选择 “Cancel” 则返回 None。
        if os.path.splitext(NewPath)[1]!=".txt":
            NewPath+=".txt"
        with open(NewPath,'w',encoding='gbk',errors='ignore') as NewFile:
            NewFile.write(text_after[:-1])
