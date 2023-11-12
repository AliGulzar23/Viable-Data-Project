from Controller.Database_Manager import database_Manager
from datetime import datetime, timedelta


class book_View_Controller:
    def __init__(self):
        self.dataFrame = database_Manager("Books")

    def Show_All_Books(self):
        return self.dataFrame.dataframe

    def Rent_Book(self, bookID, userID):
        book = database_Manager("Books")
        df = book.Update_Row(bookID, "Book_ID", "Status", 1)
        book.Update(df)

        bookMan = database_Manager("Book_Manager")
        row = [bookID, userID, datetime.today().date(), datetime.today().date() + timedelta(14), 14, 0]
        bookMan.Add_Row(row)
