import pyodbc



class LoginDAL_Class:

    def loginCheck(self,userName:str,password:str):
        connectionString = 'Driver={SQL Server}; Server=DESKTOP-MQ23T45; Database=pubs; Trusted_Connection= yes'
        commandText = 'EXEC	[dbo].[CheckLogin] ?,?'
        params=(userName,password)

        with pyodbc.connect(connectionString) as sqlConnection:
            cursor = sqlConnection.cursor()
            cursor.execute(commandText,params)
            rows = cursor.fetchall()
        return rows
