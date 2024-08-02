from Model.StoreModel import  StoreModel_Class
from DataAccessLayer.StoreCRUD_DAL import StoreCRUD_DAL_Class


class StoreCRUDBLL_CLass:
    def registerStore(self,storeObject:StoreModel_Class):
        from DataAccessLayer.StoreCRUD_DAL import StoreCRUD_Class
        storeCRUD_Object = StoreCRUD_Class()
        storeCRUD_Object.registerStore(storeObject)

    def getStoreList(self):
        StoreCRUD_DAL_Object = StoreCRUD_DAL_Class()
        return StoreCRUD_DAL_Object.getStoreList()