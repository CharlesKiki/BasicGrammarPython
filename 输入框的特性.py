from tkinter import *

top = Tk()
Tk().title('Entry特性')
Tk().geometry('200x200')
#控制窗口大小
text = Entry(top, background = 'red')

text2 = Entry(top, state = 'normal')  #可操作
text3 = Entry(top, state = 'disabled')  #不可操作
#text.pack()

mainloop()