import easygui as Box
import os

target=[".c",".cpp",".py",".cc",".java"]

File={}#空索引
Line={}

def PrintResult(Path):
    lines=0
    total=0
    text=""
    for Type in Line:
        lines=Line[Type]
        total+=lines
        text+="[%s]文件%d个，代码%d行\n"%(Type,File[Type],lines)
    title="统计结果"
    msg="一共编写了%d行代码，完成进度:%.2f %%\n离10万行代码还差%d行！"%(total,total/1000,100000-total)
    Box.textbox(msg,title,text)
    
        

def CoutLine(FileName):
    lines=0
    with open(FileName,'r') as File:
        print("正在统计%s文件......"%FileName)
        try:
            for eachLine in File:
                lines+=1
        except UnicodeDecodeError:
                pass #如果遇到了奇怪文件，忽略
    return lines


def SearchFile(Path):
    os.chdir(Path)#更改工作目录
    for eachFile in os.listdir(os.curdir):#目录下所有文件
        Type=os.path.splitext(eachFile)[1]
        if Type in target:
            lines=CoutLine(eachFile)#统计文件内的行数
            #统计文件数
            try:#如果字典中不存，抛出 KeyError，则添加字典键
                File[Type]+=1
            except KeyError:
                File[Type]=1
            #统计代码行数
            try:
                Line[Type]+=lines
            except KeyError:
                Line[Type]=lines
        if os.path.isdir(eachFile):#是文件夹
            SearchFile(eachFile)
            #递归结束后工作目录回到上一级目录
            os.chdir(os.pardir)

#主函数
Box.msgbox("请打开要统计的文件夹!","统计代码量")

Path=Box.diropenbox("请选择要统计的代码库")

SearchFile(Path)

PrintResult(Path)
