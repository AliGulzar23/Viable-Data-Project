import tkinter as tk
from Controller.Verify_Create_User import verify_Crate_User
class create_User(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        # name
        firstNameLabel = tk.Label(self, text="First name")
        firstNameLabel.pack()
        self.firstName = tk.Entry(self, width=50)
        self.firstName.pack()
        self.firstName.focus_set()

        lastNameLabel = tk.Label(self, text="Last Name")
        lastNameLabel.pack()
        self.lastName = tk.Entry(self, width=50)
        self.lastName.pack()
        self.lastName.focus_set()

        usernameLabel = tk.Label(self, text="Username")
        usernameLabel.pack()
        self.username = tk.Entry(self, width=50)
        self.username.pack()
        self.username.focus_set()

        passwordLabel1 = tk.Label(self, text="Password")
        passwordLabel1.pack()
        self.password1 = tk.Entry(self, width=50, show="*")
        self.password1.pack()
        self.password1.focus_set()

        passwordLabel2 = tk.Label(self, text=" Reenter Password")
        passwordLabel2.pack()
        self.password2 = tk.Entry(self, width=50,show="*")
        self.password2.pack()
        self.password2.focus_set()

        emailLabel = tk.Label(self, text="Email")
        emailLabel.pack()
        self.email = tk.Entry(self, width=50)
        self.email.pack()
        self.email.focus_set()

        submitButton = tk.Button(self, text="Submit",
                                 command=lambda: self.Verify_User())
        submitButton.pack()
        backButton = tk.Button(self, text = "Back",
                               command = lambda: self.controller.Show_Frame("start_Page"))
        backButton.pack()
        self.errorLabel = tk.Label(self,text = '')


    def Verify_User(self):

        verify = verify_Crate_User(self.firstName.get(),self.lastName.get(),self.username.get(),
                               self.email.get(),self.password1.get(),self.password2.get())

        isVerified = verify.Verify_User()
        errorMessage = verify.Get_Error_Message()
        if isVerified:
            self.Delete_Form()
            self.controller.Show_Frame("create_User_Success")
        else:
            self.errorLabel.config(text=errorMessage)
            self.errorLabel.pack()





    def Delete_Form(self):
        self.firstName.delete(0, 'end')
        self.lastName.delete(0, 'end')
        self.username.delete(0, 'end')
        self.password1.delete(0, 'end')
        self.password2.delete(0, 'end')
        self.email.delete(0, 'end')


class create_User_Success(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        lable = tk.Label(self,text = "User sucessfully created")
        lable.pack()
        backButton = tk.Button(self,text = "Back",
                               command = lambda  : self.controller.Show_Frame("start_Page"))
        backButton.pack()

        loginButton = tk.Button(self, text = "Login",
                                command = lambda : self.controller.Show_Frame("login"))
        loginButton.pack()
