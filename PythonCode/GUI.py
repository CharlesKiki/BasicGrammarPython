from tkinter import *

 class LabelDemo(Frame):
     def __init__(self):
         Frame.__init__(self)
         self.master.title("Label Demo")
         self.grid()
         self._label = Label(self , text = "Hello world!")
         self._label.grid()
def main():
    LabelDemo().mainloop()
main()