import pyodbc
from Model.PubModel import PublisherModel_Class
class PubCRUD_DAL_Class:
    def getPubList(self):
        commandText = '[dbo].[GetPubList]'
        connectionString = 'Driver={SQL SERVER};Server={DESKTOP-MQ23T45};Database=Pubs;Trusted_Connection=yes'

        with pyodbc.connect(connectionString) as connection:
            cursor = connection.cursor()
            cursor.execute(commandText, )
            rows = cursor.fetchall()
        return rows




    def registerPublisher(self,publisherObject : PublisherModel_Class):
        commandText = 'EXEC [dbo].[RegisterPublisher] ?,?,?,?,?'
        connectionString = 'Driver={SQL Server}; server=DESKTOP-MQ23T45; Database=Pubs; Trusted_Connection=yes'

        params = (publisherObject.PublisherID, publisherObject.PublisherName,publisherObject.City, publisherObject.State, publisherObject.Country)


        with pyodbc.connect(connectionString) as connection:
                cursor = connection.cursor()
                cursor.execute(commandText, params)
                connection.commit()