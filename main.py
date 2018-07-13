#该程序旨在测试本机和指定IP的连接和请求，探测信息
import socket, os, struct
from tkinter import *
import IPy
#该模块具有检测IP地址的功能
import os
#这个方法使用了系统自带的编码方式，这可能导致了无法正常显示
#解决方法，Pycharm全局Encoding
import sys

#通过StringVar()的get()和set()函数可以读取和输出相应内容
def submit():
    #现在这个函数是用来让第二个输入框也是和第一个相同内容
    Ent2Str.set(Ent1Str.get())

root = Tk()
#现在root相当于实例化的一个窗口
root.title("网络测试工具")
root.geometry('300x200')
frame = Frame(root)
#框架控件；在屏幕上显示一个矩形区域，多用来作为容器
frame.pack(padx=8, pady=8, ipadx=4)
#默认最佳大小
lab1 = Label(frame, text="待检测的IP:")
#标签控件；可以显示文本和位图
lab1.grid(row=0, column=0, padx=5, pady=5, sticky=W)
#默认最佳大小

Ent1Str = StringVar()
#这个函数可以获取一行字符串，这个类带有一个关于get()的函数
ent1 = Entry(frame, textvariable=Ent1Str)
#输入控件；用于显示简单的文本内容，textvariable是一个和UI相关的显示类型 textvariable和StringVar()搭配使用
ent1.grid(row=0, column=1, sticky='ew', columnspan=2)
#默认最佳大小

lab2 = Label(frame, text="Ping状态:")
lab2.grid(row=1, column=0, padx=5, pady=5, sticky=W)

Ent2Str = StringVar()
#这里p已经是一个实例化的类了，它用来表示随时变化的值
ent2 = Entry(frame, textvariable=Ent2Str)
#这里textvariable是随时可能变动的值
ent2.grid(row=1, column=1, sticky='ew', columnspan=2)

button = Button(frame, text="下一步", command=submit, default='active')
button.grid(row=2, column=1)
#这里点击按钮具有触发一个函数的功能，绑定对象

lab3 = Label(frame, text="")
lab3.grid(row=2, column=0, sticky=W)

button2 = Button(frame, text="退出", command=quit)
button2.grid(row=2, column=2, padx=5, pady=5)

#----------------------从这里开始编写是否ping通的功能
IPAddress = Ent1Str
ip = '119.75.217.109'
version = IPy.IP(ip).version()
ConnectionState = 0
backinfo = os.system('ping %s' % ip)  # 实现pingIP地址的功能，-c1指发送报文一次，-w1指等待1秒
if backinfo:
    ConnectionState = 0
    print ('Connect Unsuccess')
else:
    ConnectionState = 1
    print ('Connect Success')
#----------------------是否ping通的功能结束
root.mainloop()





