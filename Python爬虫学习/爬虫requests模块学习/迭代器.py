# 闭包
#
# def func():
#     name = 'test'
#
#     def func1():
#         print(name)
#
#     func1()
#     # 检测闭包
#     print(func1.__closure__)
#     return func1
#
#
# l = [1, 2, 3]
#
# pos = l.__iter__()
#
# while True:
#     try:
#         num = pos.__next__()
#         print(num)
#     except StopIteration:
#         break

'''生成器'''


#
# def fun2():
#     print('test')
#     yield 1
#     print('程序中断后')
#     yield
#
#
# a = fun2()  # 返回生成器
# print(a.__next__())  # 调用生成器
# print(a.__next__())

# def fun():
#     for i in range(1, 10000):
#         A = yield 'testA' + str(i)
#         print(A)
#         B = yield 'testB'
#         print(B)
#
#
# ob = fun()
#
# # for循环遍历生成器
# for i in ob:
#     print(i)

