import pyodbc
from Model.JobModel import JobModel_Class
class JobCRUD_DAL_Class:
    def getJobList(self):
        commandText = '[dbo].[GetJobList]'
        connectionString = 'Driver={SQL SERVER};Server={DESKTOP-MQ23T45};Database=Pubs;Trusted_Connection=yes'

        with pyodbc.connect(connectionString) as connection:
            cursor = connection.cursor()
            cursor.execute(commandText, )
            rows = cursor.fetchall()
        return rows



class JobCRUD_Class:
    def registerJob(self,JobObject:JobModel_Class):
        commandText = 'EXEC [dbo].[RegisterJobs] ?,?,?'
        connectionString = 'Driver={SQL Server}; server=DESKTOP-MQ23T45; Database=Pubs; Trusted_Connection=yes'

        params = (JobObject.JobDescription, JobObject.MinLVL, JobObject.MaxLVL)


        with pyodbc.connect(connectionString) as connection:
                cursor = connection.cursor()
                cursor.execute(commandText, params)
                connection.commit()