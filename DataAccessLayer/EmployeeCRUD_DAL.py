from Model.EmployeeModel import EmployeeModel_Class
import pyodbc

class EmployeeCRUD_Class:
    def registerEmployee(self,employeeObject:EmployeeModel_Class):
        commandText = 'EXEC [dbo].[RegisterEmployee] ?,?,?,?,?,?,?,?'
        connectionString = 'Driver={SQL Server}; server=DESKTOP-MQ23T45; Database=Pubs; Trusted_Connection=yes'

        params = (employeeObject.EmployeeID, employeeObject.FirstName,
                  employeeObject.Minit, employeeObject.LastName, employeeObject.JobID,
                  employeeObject.JobLevel, employeeObject.PubID, employeeObject.HireDate)


        with pyodbc.connect(connectionString) as connection:
                cursor = connection.cursor()
                cursor.execute(commandText, params)
                connection.commit()

class EmployeeCRUD_DAL_Class:
    def getEmployeeList(self):

        commandText = '[dbo].[GetEmployeeList]'
        connectionString = 'Driver={SQL SERVER};Server={DESKTOP-MQ23T45};Database=Pubs;Trusted_Connection=yes'

        with pyodbc.connect(connectionString) as connection:
            cursor = connection.cursor()
            cursor.execute(commandText, )
            rows = cursor.fetchall()
        return rows

