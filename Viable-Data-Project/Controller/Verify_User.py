from Controller.Database_Manager import database_Manager
import bcrypt

class verify_User():
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.detailsCorrect = True
        self.databaseManager = database_Manager("Users")
        self.id = 0
    def Verify_Login(self):
        name = self.databaseManager.Get_Column("Username")
        if self.username not in name:
           self.detailsCorrect = False
           return self.detailsCorrect
        #username doesn not exist

        #useername should exist at this point
        row = self.databaseManager.Get_Row("Username", self.username)
        password = row["Password"].to_numpy()
        password = password[0]
        password = password.split("'")[1]
        isPassCorrect = bcrypt.checkpw(self.password.encode('utf8'),password.encode('utf8'))
        if not isPassCorrect:
            self.detailsCorrect = False
            return self.detailsCorrect

        #both usernanme and password works
        #login successful
        self.id = row['User_ID'].to_numpy()[0]

        return True
    def Get_ID(self):
        return self.id