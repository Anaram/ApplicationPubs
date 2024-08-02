

from DataAccessLayer.LoginDAL_Module import LoginDAL_Class

class LoginBLL_Class:

    def loginCheck(self, userName: str, password: str):
        loginDAL_Object = LoginDAL_Class()
        return loginDAL_Object.loginCheck(userName, password)
