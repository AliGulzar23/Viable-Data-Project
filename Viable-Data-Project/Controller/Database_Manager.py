import pandas as pd

class database_Manager():
    def __init__(self,dbName):
        self.path = self.Get_Path(dbName)
        self.dataframe = pd.read_csv(self.path)

    def Get_Length(self):
        return len(self.dataframe)
    def Get_Column( self,column):
        return self.dataframe[column].to_numpy()

    def Get_Path(self, dbName):
        path = 'Model/' + dbName + '.csv'
        return path
    def Update_Row(self,id, idColumn, valueColumn, value):
        self.dataframe.loc[self.dataframe[idColumn] == id,valueColumn ] = value
        return self.dataframe

    def Add_Row(self,row):
        #auto increment index
        self.dataframe.loc[self.Get_Length()] = row
        self.dataframe.to_csv(self.path,index = False)
    def Get_Row(self,column,value):
        return self.dataframe.loc[self.dataframe[column] == value]

    def Get_Table_From_Value(self,column,value):
        return self.dataframe[self.dataframe[column] == value]

    def Get_DataFrame(self):
        return self.dataframe

    def Update(self, dataframe):
        self.dataframe = dataframe
        self.dataframe.to_csv(self.path,index= False)
    def Remove_Row(self,column , value):
        self.dataframe = self.dataframe[self.dataframe[column] != value]
        return self.dataframe

