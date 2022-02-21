#python 数组
member=["dodamce","小明",1]
for i in member:
    print(i)
member.insert(1,"1.5")
for i in member:
    print(i)
member.append("hello Linux")#尾插
for i in member:
    print(i)
member.extend(["Hello","word"])#尾插列表
for i in member:
    print(i)
#交换数组内的值
print("----------------")
tmp=member[0]
member[0]=member[1];
member[1]=tmp
for i in member:
    print(i)
#删除元素
member.remove("小明")
print("----------------")
for i in member:
    print(i)

del member[1]
print("----------------")
for i in member:
    print(i)
member.pop()#删除最后一个元素，返回最后一个元素‘栈’
member.pop(2)#删除下标为2的元素，并返回
#列表切片
print(member[1:3])#左闭右开,返回数组(列表)
print("----------------")
print(member[:3])#从头开始到结束
print("----------------")
print(member[2:])#从2开始到结束
print("----------------")
print(member[:])#全列表
