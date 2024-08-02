from Model.UserModel import UserModel_Class
from DataAccessLayer.JobCRUD_DAL import JobCRUD_DAL_Class
from Model.JobModel import  JobModel_Class

class Job_CRUD_BLL_Class:
    def getJobList(self):
        JobCRUD_DAL_Object = JobCRUD_DAL_Class()
        return JobCRUD_DAL_Object.getJobList()





    def registerJob(self,JobObject:JobModel_Class):
        from DataAccessLayer.JobCRUD_DAL import JobCRUD_Class
        jobCRUD_Object = JobCRUD_Class()
        jobCRUD_Object.registerJob(JobObject)

