import tkinter as tk
from Controller.Book_Controller import book_Controller
from PIL import ImageTk, Image
from Controller.Database_Manager import database_Manager
from datetime import datetime
class view_Books(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        showButton = tk.Button(self, text ="show books",
                      command = lambda : self.Show_Table())
        showButton.grid(row = 0, column = 0)

        backButton = tk.Button(self, text = "Back",
                                 command = lambda : self.controller.Show_Frame("book_Menu"))
        backButton.grid(row = 0, column = 1)
    def Show_Table(self):
        books = book_Controller(self.controller.Get_UserID())
        print(books.Get_Books_From_ID("User_ID"))
        database = books.Get_Books_From_ID("User_ID")
        # img = Image.open('Model/Images/1 KmJbC8bdTxvCSQdyxGtxaA.jpg')
        # img = img.resize((50,50))
        # img = ImageTk.PhotoImage(img)
        # panel = tk.Label(self,image = img)
        # panel.image = img
        # panel.grid(row = 1, column = 0)
        rows =[]
        columnNames = ['Book_ID','User_ID','Loaned_Date','Return_Date','Days_Left','Overdue']
        dbNames = ["Book", "Owner","Loaned on ","return date","daysLeft","image"," "]
        title = []
        for i in range(len(dbNames)):
            e = tk.Label(self,text = dbNames[i])
            e.grid(row =1 , column = i+1)
            title.append(e)
        addImag = False
        addButton = False
        for row in range(2,len(database)+2):
            columns = []
            BookID = ''
            for column in range(1,7):
                rowIndex = row -2
                columnIndex = column-1
                text = database[columnNames[columnIndex]][rowIndex]

                if(columnIndex == 0):
                    book = database_Manager("Books")
                    BookID  = text
                    bookName = book.Get_Row("Book_ID",text)
                    text = bookName["Name"].to_numpy()[0]

                if(columnIndex ==1):
                    users = database_Manager("Users")
                    username = users.Get_Row("User_ID",text)
                    text = username["Username"].to_numpy()[0]
                if(columnIndex == 4):
                    book = database_Manager("Book_Manager")
                    bookName = book.Get_Row("Book_ID",database["Book_ID"][rowIndex])
                    startDate = bookName["Loaned_Date"].to_numpy()[0]
                    endDate = bookName["Return_Date"].to_numpy()[0]
                    startDate = datetime.today().date()

                    endDate = datetime.strptime(endDate,'%Y-%m-%d').date()
                    daysLeft = endDate - startDate
                    daysLeft = daysLeft.days

                    if(startDate>endDate):
                        text = "OVERDUE"
                    else:
                        text = daysLeft
                if(columnIndex ==5):
                    #gen image
                    book = database_Manager("Books")
                    imagePath = book.Get_Row("Book_ID",database["Book_ID"][BookID])
                    imagePath = imagePath["Image"].to_numpy()[0]
                    img = Image.open('Model/Images/'+imagePath+'.jpg')
                    img = img.resize((75,75))
                    img = ImageTk.PhotoImage(img)
                    panel = tk.Label(self,image = img)
                    panel.image = img
                    panel.grid(row = row,column = column)
                    columns.append(panel)
                    addImag = True

                if(not addImag):
                    entity = tk.Label(self,text = text)
                    entity.grid(row = row, column = column)
                    columns.append(entity)
                addImag = False

            #add return button
            e = tk.Button(self, text = "Return" ,
                          command= lambda x = BookID: self.Return_book(x))
            e.grid(row = row, column = 7 )
            columns.append(e)
            rows.append(columns)


    def Return_book(self,bookId):
        book = book_Controller(self.controller.Get_UserID())
        book.Return_Book(bookId)
        book.Delete_Book(bookId)
        self.controller.Show_Frame("view_Books")
