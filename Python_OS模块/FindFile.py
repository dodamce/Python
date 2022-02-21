import os

def FindFile(Findir,target):#函数传入搜索路径，要查找的文件名
    os.chdir(Findir)
    #修改当前工作路径 如果修改的工作目录不存在，Python 解释器会报错

    for each_file in os.listdir(os.curdir):#当前目录下所有文件
        if each_file ==target:
            #打印文件路径
            print(os.getcwd()+os.sep+each_file)
            #os.sep根据你所处的平台，自动采用相应的分隔符号。
        elif os.path.isdir(each_file):
            #进入文件夹递归调用
            FindFile(each_file,target)
            #递归结束后返回原来的目录
            os.chdir(os.pardir)


Findir=input("请输入查找目录:")
target=input("请输入要查找的目标文件:")
FindFile(Findir,target)
