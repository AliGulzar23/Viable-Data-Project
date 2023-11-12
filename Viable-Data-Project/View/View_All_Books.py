import tkinter as tk
from Controller.Book_Viewer_Controller import book_View_Controller
from PIL import ImageTk, Image

class view_All_Books(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)


        backButton = tk.Button(self, text = "Log out",
                               command = lambda : self.controller.Show_Frame("book_Menu"))
        backButton.grid(row = 0, column = 0)

        self.controller = controller

        books =book_View_Controller()
        df = books.Show_All_Books()
        rows = []
        columnNames = ["Book_ID","Name","Author","Image","Description","Status"]
        dbNames = ["Book","Author","Image","Description""Rent?"]
        title = []
        for i in range(len(dbNames)):
            e = tk.Label(self,text = dbNames[i])
            e.grid(row = 1, column = i)
            title.append(e)

        addImg = False
        for row in range(2,len(df)+2):
            columns = []
            BookID = ''
            for column in range(1,7):
                rowIndex = row -2
                columnIndex = column -1
                text = df[columnNames[columnIndex]][rowIndex]
                if columnIndex == 0:
                    #book id
                    BookID = text
                    text = ''
                if columnIndex == 3:
                    imagePath = 'Model/Images/' + text +".jpg"
                    img = Image.open(imagePath)
                    img = img.resize((75,75))
                    img = ImageTk.PhotoImage(img)
                    panel= tk.Label(self,image = img)
                    panel.image = img
                    panel.grid(row = row, column = column)
                    columns.append(panel)
                    addImg = True

                if not addImg:
                    entity = tk.Label(self,text = text)
                    entity.grid(row= row, column = column)
                    columns.append(entity)
                addImg = False
            #add rent button
            if df["Status"][rowIndex] == 0:
                e = tk.Button(self, text = "Rent",
                              command = lambda x = BookID: self.Rent_Book(x))
                e.grid(row = row, column = column)
                columns.append(e)
            rows.append(columns)
    def Rent_Book(self,bookID):
        book = book_View_Controller()
        book.Rent_Book(bookID,self.controller.Get_UserID())
