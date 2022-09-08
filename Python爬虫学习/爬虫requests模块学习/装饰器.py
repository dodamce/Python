import time


#
#
# def funcTest():
#     print("被测试效率函数正在执行")
#     time.sleep(2)
#
#
# # func为可调用对象
# def Test(func):
#     begin = time.time()
#     func()
#     end = time.time()
#     print("函数执行时间为%s" % (end - begin))
#
#
# Test(funcTest)
#
#
# # 装饰器方法
# def TestDemo(func):
#     def inner():
#         begin = time.time()
#         func()
#         end = time.time()
#         print("函数执行时间为%s" % (end - begin))
#
#     return inner

# # 装饰器的使用
# def sum(*args, **kwargs):
#     ret = 0
#     for val in kwargs.values():
#         print(kwargs)
#         ret += val
#     for val in args:
#         ret += val
#     print(ret)
#
#
# sum(1, 10)
def dec1(func):
    print("1111")

    def one():
        print("2222")
        func()
        print("3333")

    return one


def dec2(func):
    print("aaaa")

    def two():
        print("bbbb")
        func()
        print("cccc")

    return two


@dec1
@dec2
def test():
    print("test test")


test()


def Test(func):
    def inner():
        return "Test-" + func() + "-Test"

    return inner


def test(func):
    def inner():
        return "test-" + func() + "-test"

    return inner


@Test
@test
def funcTest():
    return "hello"


print(funcTest())


