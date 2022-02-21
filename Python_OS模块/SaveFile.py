import os

FileList=[]#全局列表储存要写入到文件的内容

def FindFile(StartDir,target):#传入目标路径以及要查找的列表
    os.chdir(StartDir)

    for eachFile in os.listdir(os.curdir):
        Type=os.path.splitext(eachFile)[1]#文件后缀

        if Type in target:
            FileList.append(os.getcwd()+os.sep+eachFile+os.linesep)
            #os.linesep字符串给出当前平台使用的行终止符。例如，Windows使用’\r\n’
        elif os.path.isdir(eachFile):
            FindFile(eachFile,target)
            #递归结束返回原来路径
            os.chdir(os.pardir)

StartDir=input("输入要查找的起始路径:")

SaveDir=os.getcwd()#获取要保存的文件路径

target=[".py",".txt"]

FindFile(StartDir,target)

File=open(SaveDir+os.sep+"py.txt",'w')#带路径以写方式创建文件，没有文件时创建
File.writelines(FileList)#将列表所有元素写入文件中
File.close()
