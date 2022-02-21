#-*-coding:GBK -*- 
# -*- coding: UTF-8 -*-
#python元组
#元组之间的数据不能修改（const）
tuple1=(1,2,3,4,5,6,7,8)
for i in tuple1:
    print(i)
tuple2=()#空元组
tuple3=1,#一个元素的元组
#更新元组
tuple4=('小明','小刚','小红')
print(tuple4)
tuple4=tuple4[:1]+('小静',)+tuple4[1:]#覆盖tuple4，原元组被回收
print(tuple4)
