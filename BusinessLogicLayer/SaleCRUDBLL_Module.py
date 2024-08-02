from Model.SaleModel import  SaleModel_Class

class SaleCRUDBLL_CLass:
    def registerSale(self,saleObject:SaleModel_Class):
        from DataAccessLayer.SaleCRUD_DAL import SaleCRUD_Class
        saleCRUD_Object = SaleCRUD_Class()
        saleCRUD_Object.registerSale(saleObject)