#-*-coding:GBK -*- 

import easygui as Box
import os

FilePath=Box.fileopenbox(default="*.txt")
#fileopenbox(msg=None, title=None, default='*', filetypes=None, multiple=False)
#fileopenbox() ���������ṩһ���Ի��򣬷����û�ѡ����ļ�����������·����������û�ѡ�� ��Cancel�� �򷵻� None��
#Ĭ����ʾ����txt�ļ�

with open(FilePath,encoding='gbk',errors='ignore') as File:#with��䣬�Զ��ر��ļ��Ȳ���
    title=os.path.basename(FilePath)#�����ļ���
    msg="�ļ�[%s]����Ϊ��"%title
    text=File.read()
    text_after=Box.textbox(msg,title,text)
#textbox(msg='', title=' ', text='', codebox=False, callback=None, run=True)
#textbox() ����Ĭ�ϻ��Ա������壨���� codebox=True ����Ϊ�ȿ����壩����ʾ�ı����ݣ��Զ����У�����������ʺ�������ʾһ����������֡�

if text !=text_after[:-1]:#b = a[:-1]��ʾ��a�ĵ�һ��Ԫ�ظ��Ƶ����һ��Ԫ��֮ǰ��b
    choice = Box.buttonbox("��⵽�ļ����ݷ����ı䣬��ѡ�����²�����", "����", ("���Ǳ���", "��������", "���Ϊ..."))
    if choice =="���Ǳ���":
        with open(FilePath,'w',encoding='gbk',errors='ignore') as File:
            File.write(text_after[:-1])
    if choice =="��������":
        pass #���㲻���Ҫд������ʱ���Ϳ�����pass��������ӡ�
    if choice =="���Ϊ...":
        NewPath=Box.filesavebox(default=".txt")
#filesavebox(msg=None, title=None, default='', filetypes=None)
#filesavebox() �����ṩһ���Ի���������ѡ���ļ���Ҫ�����·����������·����������û�ѡ�� ��Cancel�� �򷵻� None��
        if os.path.splitext(NewPath)[1]!=".txt":
            NewPath+=".txt"
        with open(NewPath,'w',encoding='gbk',errors='ignore') as NewFile:
            NewFile.write(text_after[:-1])
