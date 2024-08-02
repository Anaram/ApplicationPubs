from Model.EmployeeModel import  EmployeeModel_Class
from DataAccessLayer.EmployeeCRUD_DAL import EmployeeCRUD_DAL_Class
from Model.EmployeeModel import  EmployeeModel_Class
class EmployeeCRUDBLL_CLass:
    def registerEmployee(self,employeeObject:EmployeeModel_Class):
        from DataAccessLayer.EmployeeCRUD_DAL import EmployeeCRUD_Class
        employeeCRUD_Object = EmployeeCRUD_Class()
        employeeCRUD_Object.registerEmployee(employeeObject)

class EmployeeCRUD_BLL_CLass:
    def getEmployeeList(self):
        EmployeeCRUD_DAL_Object = EmployeeCRUD_DAL_Class()
        return EmployeeCRUD_DAL_Object.getEmployeeList()