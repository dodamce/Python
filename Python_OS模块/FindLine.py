#os.walk 的返回值是一个三元组(root,dirs,files)
#root 指的是当前正在遍历的这个文件夹的本身的地址
#dirs 返回的是一个列表list，表中数据是该文件夹中所有的目录的名称(但不包括子目录名称)
#files 返回的也是一个列表list , 表中数据是该文件夹中所有的文件名称(但不包括子目录名称)

import os

def PrintPos(Key_Pos):
    keys=Key_Pos.keys()
    keys=sorted(keys)#字典键值无序，这里先对键值数组排序
    for each_key in keys:
        print("关键字出现在第%s行，第%s个位置"%(each_key,str(Key_Pos[each_key])))

def PosInLine(line,Key):
    Pos=[]
    begin=line.find(Key)
    while begin!=-1:
        Pos.append(begin+1)#因为起始为0开始计数，用户默认起始从1开始
        begin=line.find(Key,begin+1)#找下一个位置
    return Pos

def SearchTxT(FileName,Key):#在文件中查找是否有关键字
    File=open(FileName,'r',encoding='gbk',errors='ignore')#已带路径
    #避免出现UnicodeDecodeError: 'gbk' codec can't decode byte 0xaa in position 9等错误
    row=0#行数
    Key_Pos=dict()#存放key所在具体行数的映射
    for each_line in File:
        row+=1
        if Key in each_line:
            Pos=PosInLine(each_line,Key)#在这一行的第几个字节
            Key_Pos[row]=Pos
    File.close()
    return Key_Pos

def FindFile(Key,flag):#传入两个参数，一个是要查找的关键字，另一个是是否显示具体位置选项
    Files=os.walk(os.getcwd())
    TxT=[]
    for i in Files:
        for File in i[2]:
            if os.path.splitext(File)[1] ==".txt":
                File=os.path.join(i[0],File)#连接两个或更多的路径名组件
                TxT.append(File)
    for eachTxT in TxT:
        Key_Pos=SearchTxT(eachTxT,Key)
        if Key_Pos:
            print("======================================================")
            print("在文件[%s]中找到关键字(%s)"%(eachTxT,Key))
        if flag in ["YES","Yes","yes"]:#需要打印具体位置
            PrintPos(Key_Pos)

#主函数
print("请将该脚本放入要查找关键字的文件夹中")
Key=input("请输入要查找的关键字：")
flag=input("是否需要打印关键字[%s]在文件的具体位置(Yes/No)："%Key)
FindFile(Key,flag)

Stop=input()#卡一下程序，防止闪退，方便测试
            
        
