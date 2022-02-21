#异常捕捉
try:
    sum=1+'1'
    f=open("Test.txt")#不存在的文件
    f.close()
except OSError as reason:
    print("打开文件出错,错误原因为：",str(reason))
except TypeError as reason:
    print(str(reason))

#方法二:
try:
    sum=1+'1'
    f=open("Test.txt")#不存在的文件
    f.close()
except (OSError,TypeError) as reason:
    print("打开文件出错,错误原因为：",str(reason))


#方法三
try:
    f=open("Test.txt")#不存在的文件
except (OSError,TypeError) as reason:
    print("打开文件出错,错误原因为：",str(reason))
finally:
    f.close()#finally代码一定会执行，避免因为异常导致文件未关闭

#引出异常
raise TypeError#类型错误
