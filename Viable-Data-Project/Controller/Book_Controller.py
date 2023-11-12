from Controller.Database_Manager import database_Manager
import pandas as pd
import numpy as np
import datetime

class book_Controller:
    def __init__(self, userID):
        self.userID = userID
        self.dataFrame = database_Manager("Book_Manager")

    def Get_Books_From_ID(self,column):
        return self.dataFrame.Get_Table_From_Value(column,self.userID)

    def Return_Book(self,bookID):
        self.Book = database_Manager("Books")
        df = self.Book.Update_Row(bookID,"Book_ID","Status",0)

        self.Book.Update(df)
    def Delete_Book(self,bookID):
        self.Book = database_Manager("Book_Manager")
        df = self.Book.Remove_Row("Book_ID",bookID)
        self.Book.Update(df)
