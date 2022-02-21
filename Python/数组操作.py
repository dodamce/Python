#python数组操作
list1=[123,345]
list2=[123,567]
list3=list1+list2#列变+列变
print(list3)
print(list1>list2)
list4=[123,567]
print(list1<list2 and list2==list4)
#比较大小，先比较第一个，如果相同在比较第二个
list5=[[123,345],[345,678]]
print(list5)
for i in list5:
    for j in i:
        print(j)
print(list5[1][1])
#打印列标(数组)内置函数
#dir(list)
list1*=3
print(list1.count(123))#打印数字出现几次
print(list1.index(123))#找第一次出现123的位置
print(list1.index(123,4))#从4位置开始找123数字
list1.reverse();#字符串翻转
print(list1)
list1.sort();#排序,从小到大
print(list1);
#从大到小排序
print("--------------------")
list1.sort(reverse=True)
print(list1)
list6=list1#list1的引用
list7=list1[:]#list1的拷贝
print("-------------------")
list1.sort()
print(list6,'\n',list7)
