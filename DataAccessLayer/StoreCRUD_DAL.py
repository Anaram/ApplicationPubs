from Model.StoreModel import StoreModel_Class
import pyodbc

class StoreCRUD_Class:
    def registerStore(self,storeObject:StoreModel_Class):
        commandText = 'EXEC [dbo].[RegisterStores] ?,?,?,?,?,?'
        connectionString = 'Driver={SQL Server}; server=DESKTOP-MQ23T45; Database=Pubs; Trusted_Connection=yes'

        params = (storeObject.StoreID, storeObject.StoreName,
                  storeObject.StoreAddress, storeObject.City, storeObject.State,
                  storeObject.Zip)


        with pyodbc.connect(connectionString) as connection:
                cursor = connection.cursor()
                cursor.execute(commandText, params)
                connection.commit()


class StoreCRUD_DAL_Class:
    def getStoreList(self):
        commandText = '[dbo].[GetStoreList]'
        connectionString = 'Driver={SQL SERVER};Server={DESKTOP-MQ23T45};Database=Pubs;Trusted_Connection=yes'

        with pyodbc.connect(connectionString) as connection:
            cursor = connection.cursor()
            cursor.execute(commandText, )
            rows = cursor.fetchall()
        return rows
