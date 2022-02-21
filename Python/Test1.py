def Save(A,B,cout):
    #文件保存
    Name_A="A"+str(cout)+".txt"
    Name_B="B"+str(cout)+".txt"
    Af=open(Name_A,'w')
    Bf=open(Name_B,'w')
    Af.writelines(A)
    Bf.writelines(B)
    #写入后关闭
    Af.close()
    Bf.close()


f=open("./read.txt",'r',encoding='UTF-8')
A=[]
B=[]
cout=1#计数器
for each_line in f:
    if each_line[:6]!="======":#判断前6个字是不是===
        #字符串分割
        (role,line_spoken)=each_line.split("：",1)#字符串分割
        if role=="A":
            A.append(line_spoken)
        elif role=="B":
            B.append(line_spoken)
    else:
        Save(A,B,cout)
        #清空A B列表
        A=[]
        B=[]
        cout+=1
#将最后一段保存起来
Save(A,B,cout)
f.close()
