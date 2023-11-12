import tkinter as tk

class book_Menu(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        viewBooksButton = tk.Button(self, text = "View Books",
                                    command = lambda : self.controller.Show_Frame("view_Books"))
        rentBookButton = tk.Button(self, text = "Rent Book",
                                   command = lambda : self.controller.Show_Frame("view_All_Books"))
        logoutButton = tk.Button(self, text = "Log out",
                                      command = lambda : self.controller.Show_Frame("start_Page"))

        viewBooksButton.pack()
        rentBookButton.pack()
        logoutButton.pack()
