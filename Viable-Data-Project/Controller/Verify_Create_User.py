import pandas as pd
import numpy as np
import re
import bcrypt
from Controller.Database_Manager import database_Manager


class verify_Crate_User():
    def __init__(self, firstname, lastname, username, email, pass1, pass2):
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.pass1 = pass1
        self.pass2 = pass2
        self.email = email
        self.errorMessage = ''
        self.dbName = "Users"
        self.database = database_Manager("Users")

    def Verify_User(self):
        if self.firstname == "silver":
            # FOR DEBUGGING PURPOSES ONLY, DELETE THIS AND ALL ENTRIES MADE
            row = [self.database.Get_Length(), 'fn', 'ln', 'Un', 'p1', 'email']
            self.database.Add_Row(row)
            return True
        self.Verify_Username()
        self.Verify_Password()
        self.Verify_Names()
        self.Verify_Email()
        if self.errorMessage == '':
            self.Add_User()
            return True
        return False

    def Verify_Username(self):
        name = self.username
        column = self.database.Get_Column("Username")
        if (self.username == ''):
            error = "Username not filled in"
            self.Add_Error(error)
            return
        if name in column:
            # username exist
            error = "Username already exists"
            self.Add_Error(error)

    def Verify_Password(self):
        if (self.pass2 != self.pass1):
            error = "Passwords not matching"
            self.Add_Error(error)
            return
        if (self.pass2 == '' or self.pass1 == ''):
            error = "Password(s) is not filled in"
            self.Add_Error(error)
            return

        specialCharacters = ['!', '#', '$', '%', '^', '&', '*', '(', ')', '/','_','-','=','+']
        # at this point the passwords must match therefore only 1 needs to be checked

        if (len(self.pass1) < 10):
            error = "Password is too short use a password 10 characters or more"
            self.Add_Error(error)
            return

        if (re.search('[0-9]', self.pass1) is None):
            error = "Password needs a number"
            self.Add_Error(error)
        elif (re.search('[A-Z]', self.pass1) is None):
            error = "Password needs a captial letter"
            self.Add_Error(error)
        elif not any(c in specialCharacters for c in self.pass1):
            err = ''
            for c in specialCharacters:
                err = err + c
            error = "Password needs a special character use some of these \n" + err
            self.Add_Error(error)

    def Verify_Names(self):
        if self.firstname == '' or self.lastname == '':
            error = "First/Last name is blank"
            self.Add_Error(error)

    def Verify_Email(self):
        if len(self.email) == 0:
            error = "Email is not filled in"
            self.Add_Error(error)
            return
        name = self.database.Get_Column("Email")
        if self.email in name:
            error = "Email already exists"
            self.Add_Error(error)

        if '@' in self.email:
            if '.' in self.email.split('@')[1]:
                return
            # email must contain an @ and a .
        error = "enter a valid email address"
        self.Add_Error(error)

    def Get_Error_Message(self):
        return self.errorMessage
    def Add_Error(self, error):
        self.errorMessage = self.errorMessage + error + '\n'
    def Add_User(self):
        #hash password
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(self.pass1.encode('utf8'),salt)
        row = [self.database.Get_Length(),self.firstname,self.lastname,self.username,
               hashed,self.email]
        self.database.Add_Row(row)