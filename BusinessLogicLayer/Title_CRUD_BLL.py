from DataAccessLayer.TitleCrud_DAL import TitleCRUD_DAL_Class

class Title_CRUD_BLL_Class:
    def getTitleList(self):
        TitleCRUD_DAL_Object = TitleCRUD_DAL_Class()
        return TitleCRUD_DAL_Object.getTitleList()

