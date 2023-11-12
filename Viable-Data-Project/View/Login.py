import tkinter as tk
from Controller.Verify_User import verify_User

class login(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        self.controller = controller
        usernameLabel = tk.Label(self, text = "Username")
        self.username = tk.Entry(self, width = 40)
        usernameLabel.pack()

        self.username.pack()

        passwordLabel = tk.Label(self, text = "Password")
        passwordLabel.pack()
        self.password = tk.Entry(self, width = 40,show='*')
        self.password.pack()
        self.errorMessage = tk.Label(self, text = '')

        submitButton = tk.Button(self, text = "Login",
                                 command =  lambda : self.Verify_User())
        submitButton.pack()
        backButton = tk.Button(self, text = "Back",
                               command = lambda : self.Back_To_Start())
        backButton.pack()


    def Verify_User(self):
        verify = verify_User(self.username.get(),self.password.get())

        if(verify.Verify_Login()):
            #load book menu page
            self.controller.Set_UserID(verify.Get_ID())
            self.userID = verify.Get_ID()
            self.controller.Show_Frame("book_Menu")

        else:
            self.errorMessage.config(text = "Username or Password is incorrect")


    def Back_To_Start(self):
        self.Clear_Form()
        self.controller.Show_Frame("start_Page")
    def Clear_Form(self):
        self.username.delete(0,'end')
        self.password.delete(0,'end')
