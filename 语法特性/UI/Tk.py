from tkinter import *
MainWindow = Tk()
#TK is a UI interface
MainWindow.title("Ping Tools")
MainWindow.geometry('300x200')
MainFrame = Frame(MainWindow)
MainFrame.pack(padx=8, pady=8, ipadx=4)
lab1 = Label(MainFrame, text="Scaning IP:")
lab1.grid(row=0, column=0, padx=5, pady=5, sticky=W)

Ent1Str = StringVar()
ent1 = Entry(MainFrame, textvariable=Ent1Str)
ent1.grid(row=0, column=1, sticky='ew', columnspan=2)

lab2 = Label(MainFrame, text="PingStatus:")
lab2.grid(row=1, column=0, padx=5, pady=5, sticky=W)

Ent2Str = StringVar()
ent2 = Entry(MainFrame, textvariable=Ent2Str)
ent2.grid(row=1, column=1, sticky='ew', columnspan=2)

button = Button(MainFrame, text="Next",  default='active')
button.grid(row=2, column=1)


lab3 = Label(MainFrame, text="")
lab3.grid(row=2, column=0, sticky=W)

button2 = Button(MainFrame, text="Exit", command=quit)
button2.grid(row=2, column=2, padx=5, pady=5)

MainWindow.mainloop()