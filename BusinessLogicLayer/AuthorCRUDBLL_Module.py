from Model.AuthorModel import  AuthorModel_Class

class AuthorCRUDBLL_CLass:
    def registerAuthor(self,authorObject:AuthorModel_Class):
        from DataAccessLayer.AuthorCRUD_DAL import AuthorCRUD_Class
        authorCRUD_Object = AuthorCRUD_Class()
        authorCRUD_Object.registerAuthor(authorObject)