import pyodbc

class TitleCRUD_DAL_Class:
    def getTitleList(self):
        commandText = '[dbo].[GetTitleList]'
        connectionString = 'Driver={SQL SERVER};Server={DESKTOP-MQ23T45};Database=Pubs;Trusted_Connection=yes'

        with pyodbc.connect(connectionString) as connection:
            cursor = connection.cursor()
            cursor.execute(commandText, )
            rows = cursor.fetchall()
        return rows

