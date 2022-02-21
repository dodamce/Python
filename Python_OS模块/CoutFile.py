import os #导入os模块

all_file=os.listdir(os.curdir)#当前路径下所有文件

type_dict=dict()#创建字典

for each_file in all_file:
    if os.path.isdir(each_file):#判断是否是文件夹，是返回True
        type_dict.setdefault("文件夹",0)#插入字典
        type_dict["文件夹"]+=1
    else:
        type_name=os.path.splitext(each_file)[1]#返回文件名以及后缀，选择后缀
        type_dict.setdefault(type_name,0)
        type_dict[type_name]+=1

for each_type in type_dict.keys():
    print("该文件夹下文件类型为[%s]的文件有 %d个"%(each_type,type_dict[each_type]))
        
