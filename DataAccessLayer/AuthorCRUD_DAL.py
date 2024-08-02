from Model.AuthorModel import AuthorModel_Class
import pyodbc

class AuthorCRUD_Class:
    def registerAuthor(self,authorObject:AuthorModel_Class):
        commandText = 'EXEC [dbo].[RegisterAuthor] ?,?,?,?,?,?,?,?,?'
        connectionString = 'Driver={SQL Server}; server=DESKTOP-MQ23T45; Database=Pubs; Trusted_Connection=yes'

        params = (authorObject.AuthorID, authorObject.AuthorLastName,
                  authorObject.AuthorFirstName, authorObject.Phone, authorObject.Address,
                  authorObject.City, authorObject.State, authorObject.Zip, authorObject.Contract)


        with pyodbc.connect(connectionString) as connection:
                cursor = connection.cursor()
                cursor.execute(commandText, params)
                connection.commit()