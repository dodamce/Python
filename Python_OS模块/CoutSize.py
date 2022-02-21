import os

all_file=os.listdir(os.curdir)

file_dict=dict()

for each_file in all_file:
    if os.path.isfile(each_file):
        file_size=os.path.getsize(each_file)
        file_dict[each_file]=file_size

for each in file_dict.items():#each是字典里的每个元素
    print("%s[%d Bytes]"%(each[0],each[1]))#each[0]=key each[1]=value
