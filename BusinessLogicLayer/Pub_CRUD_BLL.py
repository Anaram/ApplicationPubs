from Model.UserModel import UserModel_Class
from DataAccessLayer.PubCRUD_DAL import PubCRUD_DAL_Class
class Pub_CRUD_BLL_Class:
    def getPubList(self):
        PubCRUD_DAL_Object = PubCRUD_DAL_Class()
        return PubCRUD_DAL_Object.getPubList()

    from Model.EmployeeModel import EmployeeModel_Class


    def registerPublisher(self, publisherObject: PubCRUD_DAL_Class):
        from DataAccessLayer.PubCRUD_DAL import PubCRUD_DAL_Class
        publisherCRUD_Object = PubCRUD_DAL_Class()
        publisherCRUD_Object.registerPublisher(publisherObject)