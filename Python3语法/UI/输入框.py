from tkinter import *
#通过StringVar()的get()和set()函数可以读取和输出相应内容
def submit():
   p.set(u.get())

root = Tk()
#现在root相当于实例化的一个窗口
root.title("测试")
root.geometry('300x200')
frame = Frame(root)
#框架控件；在屏幕上显示一个矩形区域，多用来作为容器
frame.pack(padx=8, pady=8, ipadx=4)
#默认最佳大小
lab1 = Label(frame, text="获取:")
#标签控件；可以显示文本和位图
lab1.grid(row=0, column=0, padx=5, pady=5, sticky=W)
#默认最佳大小

u = StringVar()
#这个函数可以获取一行字符串，这个类带有一个关于get()的函数
ent1 = Entry(frame, textvariable=u)
#输入控件；用于显示简单的文本内容，textvariable是一个和UI相关的显示类型 textvariable和StringVar()搭配使用
ent1.grid(row=0, column=1, sticky='ew', columnspan=2)
#默认最佳大小

lab2 = Label(frame, text="显示:")
lab2.grid(row=1, column=0, padx=5, pady=5, sticky=W)

p = StringVar()
#这里p已经是一个实例化的类了，它用来表示随时变化的值
ent2 = Entry(frame, textvariable=p)
#这里textvariable是随时可能变动的值
ent2.grid(row=1, column=1, sticky='ew', columnspan=2)

button = Button(frame, text="登录", command=submit, default='active')
button.grid(row=2, column=1)
#这里点击按钮具有触发一个函数的功能，绑定对象

lab3 = Label(frame, text="")
lab3.grid(row=2, column=0, sticky=W)

button2 = Button(frame, text="退出", command=quit)
button2.grid(row=2, column=2, padx=5, pady=5)

#以下代码居中显示窗口

#root.update_idletasks()
#x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
#y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
#root.geometry("+%d+%d" % (x, y))
root.mainloop()