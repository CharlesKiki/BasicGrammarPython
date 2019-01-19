import tkinter as tk
from tkinter import messagebox
class verification_window(tk.Frame):
#����ʱ��ʼ��
    def __init__(self):
        global root
        root = tk.Tk()
        # ���ڴ�С����Ϊ150x150
        root.geometry('150x150+885+465')

        root.resizable(0, 0)  # ���ڴ�С�̶�

        super().__init__()
        self.username = tk.StringVar()
        self.password = tk.StringVar()
        self.pack()
        self.main_window()

        root.mainloop()

    # ���ڲ���
    def main_window(self):
        global root
        username_label=tk.Label(root,text='Username:',font=('Arial',12)).place(x=35,y=10)
        username_input = tk.StringVar
        username_entry=tk.Entry(root,textvariable=self.username).place(x=2,y=35)

        password_label=tk.Label(root,text='Password:',font=('Arial',12)).place(x=35,y=58)
        password_input = tk.StringVar
        password_entry=tk.Entry(root,textvariable=self.password,show='*').place(x=2,y=83)

        # �ڰ���CONFIRM��ťʱ������֤����
        conformation_button = tk.Button(root,text='CONFIRM',command=self.verification,fg='white',bg='black', activeforeground='white', activebackground='navy',width=8,height=1)
        conformation_button.place(x=6,y=112)

        quit_button = tk.Button(root, text='QUIT', command=root.quit, fg='white', bg='black', activeforeground='white', activebackground='red', width=8, height=1)
        quit_button.place(x=78,y=112)

    # ��֤����
    def verification(self):
        global root

        # ����û��������� �Ƿ���user_dict�ֵ���
        user_dict = {987654321:112233,123456789:332211}
        if user_dict.get(int(self.username.get())) == int(self.password.get()):
            # �ɹ�����
            messagebox.showinfo(title='Correct', message=f'{int(self.username.get())}, welcome!')

            # ��֤�ɹ����main_gui����
            #root.withdraw()
            #from gui import main_gui
            #main_gui.app()

        else:
            messagebox.showerror(title='Wrong inputs!', message='Please enter correct username or password.')  # ��������

if __name__ == '__main__':
    verification_window()
