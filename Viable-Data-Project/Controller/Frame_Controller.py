import tkinter as tk
from View.Start_Page import start_Page
from View.Create_User import create_User, create_User_Success
from View.Login import login
from View.Book_Menu import book_Menu
from View.View_All_Books import view_All_Books
from View.View_Books import  view_Books
class Frame_Controller(tk.Tk):
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)

        container = tk.Frame(self)
        container.pack()
        self.userID = 0
        self.frames = {}
        self.frameClasses = [start_Page, create_User, login, create_User_Success, book_Menu, view_All_Books, view_Books]
        for frame in self.frameClasses:
            frameName = frame.__name__
            currentFrame = frame(parent=container,controller=self)
            self.frames[frameName] = currentFrame
            currentFrame.grid(row = 0, column = 0, sticky = 'nsew')
        self.Show_Frame("start_Page")

    def Show_Frame(self,frameName):
        frame = self.frames[frameName]
        self.title(frameName)
        frame.tkraise()

    def Set_UserID(self,userID):
        self.userID = userID
    def Get_UserID(self):

        return self.userID