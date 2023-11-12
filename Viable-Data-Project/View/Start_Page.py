import tkinter as tk


class start_Page(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        self.controller = controller


        loginButton = tk.Button(self, text = "Login",
                           command = lambda : controller.Show_Frame("login"))
        loginButton.pack()

        createUserButton = tk.Button(self, text = "Create User",
                                     command = lambda : controller.Show_Frame("create_User"))
        createUserButton.pack()