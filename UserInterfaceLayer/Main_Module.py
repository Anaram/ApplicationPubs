from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msg
from Model.UserModel import UserModel_Class

class MainUIClass:
    def mainForm_Load(self, userObject: UserModel_Class):
        mainForm = Tk()
        mainForm.title ('Main Form')
        mainForm.geometry('500x450')
        mainForm.resizable (0,0)
        mainForm.iconbitmap('images/Users.ico')
        lblWelcomeMessage=ttk.Label(mainForm,text= f'Welcome {userObject.FirstName} {userObject.LastName}')
        lblWelcomeMessage.grid(row=0, column=0, padx=10, pady=10)

        x = int(mainForm.winfo_screenwidth() / 2 - 400 / 2)
        y = int(mainForm.winfo_screenheight() / 2 - 440 / 2)
        mainForm.geometry('+{}+{}'.format(x, y))

        def EmployeeFormLoad():
            mainForm.destroy()
            from UserInterfaceLayer.EmployeeCRUD_Module import EmployeeCRUD_UI_Class
            employeeCRUD_UI_Object = EmployeeCRUD_UI_Class(userModelObject=userObject)
            employeeCRUD_UI_Object.EmployeeCRUD_FormLoad()

        def JobFormLoad():
            mainForm.destroy()
            from UserInterfaceLayer.JobCRUD_Module import JobCRUD_UI_Class
            JobCRUD_UI_Object = JobCRUD_UI_Class(userModelObject=userObject)
            JobCRUD_UI_Object.JobCRUD_FormLoad()

        def PublisherFormLoad():
            mainForm.destroy()
            from UserInterfaceLayer.PublisherCRUD_Module import PublisherCRUD_UI_Class
            PublisherCRUD_UI_Object = PublisherCRUD_UI_Class(userModelObject=userObject)
            PublisherCRUD_UI_Object.PublisherCRUD_FormLoad()

        def AuthorFormLoad():
            mainForm.destroy()
            from UserInterfaceLayer.AuthorCRUD_Module import AuthorCRUD_UI_Class
            AuthorCRUD_UI_Object =AuthorCRUD_UI_Class(userModelObject=userObject)
            AuthorCRUD_UI_Object.AuthorCRUD_FormLoad()

        def StoreFormLoad():
            mainForm.destroy()
            from UserInterfaceLayer.StoreCRUD_Module import StoreCRUD_UI_Class
            StoreCRUD_UI_Object =StoreCRUD_UI_Class(userModelObject=userObject)
            StoreCRUD_UI_Object.StoreCRUD_FormLoad()

        def SaleFormLoad():
            mainForm.destroy()
            from UserInterfaceLayer.SaleCRUD_Module import SaleCRUD_UI_Class
            SaleCRUD_UI_Object =SaleCRUD_UI_Class(userModelObject=userObject)
            SaleCRUD_UI_Object.SaleCRUD_FormLoad()

        employeeImage = PhotoImage(file= 'images/EmployeeCRUD.png')
        btnEmployeeCRUD = ttk.Button(mainForm,image= employeeImage ,text='Employee CRUD', command = EmployeeFormLoad, compound=TOP, width =20)
        btnEmployeeCRUD.grid(row=1, column=0, padx=10, pady=10)

        PublisherImage = PhotoImage(file='images/PublisherCRUD.png')
        btnPublisher = ttk.Button(mainForm, image=PublisherImage, text='Publisher CRUD',command = PublisherFormLoad, compound=TOP, width=20)
        btnPublisher.grid(row=1, column=1, padx=10, pady=10)

        AuthorImage = PhotoImage(file='images/AuthorCRUD.png')
        btnAuthor = ttk.Button(mainForm, image=AuthorImage, text='Author CRUD',command = AuthorFormLoad,  compound=TOP, width=20)
        btnAuthor.grid(row=2, column=0, padx=10, pady=10)

        StoreImage = PhotoImage(file='images/StoreCRUD.png')
        btnStore = ttk.Button(mainForm, image=StoreImage, text='Store CRUD', command= StoreFormLoad, compound=TOP, width=20)
        btnStore.grid(row=2, column=1, padx=10, pady=10)

        SaleImage = PhotoImage(file='images/SaleCRUD.png')
        btnSale = ttk.Button(mainForm, image=SaleImage, text='Sale CRUD', command= SaleFormLoad, compound=TOP, width=20)
        btnSale.grid(row=2, column=2, padx=10, pady=10)

        JobImage = PhotoImage(file='images/JobCRUD.png')
        btnJob = ttk.Button(mainForm, image=JobImage, text='Job CRUD', command = JobFormLoad, compound=TOP, width=20)
        btnJob.grid(row=1, column=2, padx=10, pady=10)


        mainForm.mainloop()