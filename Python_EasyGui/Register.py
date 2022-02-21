import easygui as Box

msg="请填写下列信息"
title="账号中心"

DateName=["*用户名","*真实姓名","*电话"," 固定电话"," QQ","*邮箱"]

DateValue=Box.multenterbox(msg,title,DateName)
#multenterbox(msg='Fill in values for the fields.', title=' ', fields=[], values=[], callback=None, run=True)
#multenterbox() 为用户提供多个简单的输入框，要注意以下几点：
#如果用户输入的值比选项少的话，则返回列表中的值用空字符串填充用户为输入的选项。
#如果用户输入的值比选项多的话，则返回的列表中的值将截断为选项的数量。
#如果用户取消操作，则返回域中的列表的值或者 None 值。

while True:
    if DateValue ==None:
        break
    TxTMsg=""
    for i in range(len(DateName)):#访问每一个标题
        option=DateName[i].strip()#strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。
        if DateValue[i].strip()=="" and option[0]=="*":
            TxTMsg+=("[%s]为必填项。\n\n"%DateName[i])
    if TxTMsg=="":#说明所有的必填项都有了数据
        break
    #用之前的值再画一个窗口
    DateValue=Box.multenterbox(TxTMsg,title,DateName,DateValue)

print("用户资料为：%s"%str(DateValue))
