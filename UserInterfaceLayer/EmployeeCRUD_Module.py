from tkinter import *
from tkinter import ttk, END, font
from tkcalendar import DateEntry
from tkinter import messagebox as msg
from Model.EmployeeModel import EmployeeModel_Class
from BusinessLogicLayer.EmployeeCRUDBLL_Module import EmployeeCRUDBLL_CLass
from Model.UserModel import UserModel_Class
class EmployeeCRUD_UI_Class:
    def __init__(self, userModelObject : UserModel_Class):
        self.UserModel = userModelObject
    def EmployeeCRUD_FormLoad (self):
        registerEmployeeForm = Tk()
        registerEmployeeForm.title('Register Employee')
        registerEmployeeForm.geometry('400x400')
        registerEmployeeForm.resizable(False, False)
        registerEmployeeForm.iconbitmap('images/Users.ico')

        x = int(registerEmployeeForm.winfo_screenwidth() / 2 - 400 / 2)
        y = int(registerEmployeeForm.winfo_screenheight() / 2 - 440 / 2)
        registerEmployeeForm.geometry('+{}+{}'.format(x, y))

        EmployeeDict = {}
        EmployeeList = []
        JobDict = {}
        JobList = []
        PubDict = {}
        PubList = []

        def resetForm():
            for widget in registerEmployeeForm.winfo_children():
                if isinstance(widget, ttk.Entry):
                    widget.delete(0, END)
                elif isinstance(widget, ttk.Combobox):
                    widget.set('')
                elif isinstance(widget, DateEntry):
                    widget.set_date('')


        def registerEmployee():
            employeeModelObject = EmployeeModel_Class(EmployeeDict[txtEmployeeID.get()].get(),txtFirstName.get(),txtMinit.get(),txtLastName.get(),
                                                      JobDict[txtJob.get()],txtJobLevel.get(), PubDict[txtPub.get()],txtHireDate.get(),)
            #employeeModelObject.EmployeeID = txtEmployeeID.get()
            #employeeModelObject.FirstName = txtFirstName.get()
            #employeeModelObject.Minit = txtMinit.get()
            #employeeModelObject.LastName = txtLastName.get()
            #employeeModelObject.JobID = JobDict[txtJob.get()]
            #employeeModelObject.JobLevel = txtJobLevel.get()
            #employeeModelObject.PubID = PubDict[txtPub.get()]
            #employeeModelObject.HireDate = txtHireDate.get()
            employeeCRUD_Object = EmployeeCRUDBLL_CLass()
            employeeCRUD_Object.registerEmployee(employeeModelObject)
            resetForm()
            msg.showinfo('Welcome', 'Register Employee successfully')

        def getEmployeeList():
            from BusinessLogicLayer.EmployeeCRUDBLL_Module import EmployeeCRUD_BLL_CLass
            Employee_CRUD_BLL_Object = EmployeeCRUD_BLL_CLass()
            rows = Employee_CRUD_BLL_Object.getEmployeeList()
            for row in rows:
                if row[1] not in EmployeeDict:
                    EmployeeDict[row[1]] = row[0]
            for Employee in EmployeeDict.keys():
                EmployeeList.append(Employee)


        def getJobList():
                from BusinessLogicLayer.Job_CRUD_BLL import Job_CRUD_BLL_Class
                Job_CRUD_BLL_Object = Job_CRUD_BLL_Class()
                rows = Job_CRUD_BLL_Object.getJobList()
                for row in rows:
                    if row[1] not in JobDict:
                        JobDict[row[1]] = row[0]
                for Job in JobDict.keys():
                    JobList.append(Job)

        def getPubList():
                from BusinessLogicLayer.Pub_CRUD_BLL import Pub_CRUD_BLL_Class
                Pub_CRUD_BLL_Object = Pub_CRUD_BLL_Class()
                rows = Pub_CRUD_BLL_Object.getPubList()
                for row in rows:
                    if row[1] not in PubDict:
                        PubDict[row[1]] = row[0]
                for Pub in PubDict.keys():
                    PubList.append(Pub)

        def backTomain():
            registerEmployeeForm.destroy()
            from UserInterfaceLayer.Main_Module import MainUIClass
            mainUIObject = MainUIClass()
            mainUIObject.mainForm_Load(self.UserModel)

        lblEmployeeID = Label(registerEmployeeForm, text='Employee Name: ')
        lblEmployeeID.grid(row=0, column=0, padx=10, pady=10, sticky='w')
        txtEmployeeID = StringVar()
        getEmployeeList()
        cmbEmployeeID = ttk.Combobox(registerEmployeeForm, width=37, textvariable=txtEmployeeID, values=EmployeeList)
        cmbEmployeeID.grid(row=0, column=1, padx=10, pady=10)

        lblFirstName = Label(registerEmployeeForm, text='First Name: ', font='Tahoma 10 bold')
        lblFirstName.grid(row=1, column=0, padx=10, pady=10, sticky='w')
        txtFirstName = StringVar()
        entFirstName = ttk.Entry(registerEmployeeForm, width=40, textvariable=txtFirstName)
        entFirstName.grid(row=1, column=1, padx=10, pady=10)


        lblMinit = Label(registerEmployeeForm, text='Middle Initial: ', font='Tahoma 10 bold')
        lblMinit.grid(row=2, column=0, padx=10, pady=10, sticky='w')
        txtMinit = StringVar()
        entMinit = ttk.Entry(registerEmployeeForm, width=40, textvariable=txtMinit)
        entMinit.grid(row=2, column=1, padx=10, pady=10)

        lblLastName = Label(registerEmployeeForm, text='Last Name: ', font='Tahoma 10 bold')
        lblLastName.grid(row=3, column=0, padx=10, pady=10, sticky='w')
        txtLastName = StringVar()
        entLastName = ttk.Entry(registerEmployeeForm, width=40, textvariable=txtLastName)
        entLastName.grid(row=3, column=1, padx=10, pady=10)

        lblJobID = Label(registerEmployeeForm, text='Job Name: ', font='Tahoma 10 bold')
        lblJobID.grid(row=4, column=0, padx=10, pady=10, sticky='w')
        txtJob = StringVar()
        getJobList()
        #JobList = ['1-New Hire - Job not specified', '2-Chief Executive Officer', '3-Business Operations Manager',
                    # '4-Chief Financial Officer', '5-Publisher', '6-Managing Editor', '7-Marketing Manager', '8-Public Relations Manager',
                   #  '9-Acquisitions Manager', '10-Productions Manager', '11-Operations Manager', '12-Editor', '13-Sales Representative',
                    # '14-Designer']
        cmbJobID = ttk.Combobox(registerEmployeeForm, width=36, textvariable=txtJob, values=JobList)
        cmbJobID.grid(row=4, column=1, padx=10, pady=10)


        lblJobLevel = Label(registerEmployeeForm, text='Job Level: ', font='Tahoma 10 bold')
        lblJobLevel.grid(row=5, column=0, padx=10, pady=10, sticky='w')
        txtJobLevel = StringVar()
        entJobLevel = ttk.Entry(registerEmployeeForm, width=40, textvariable=txtJobLevel)
        entJobLevel.grid(row=5, column=1, padx=10, pady=10)


        lblPubID = Label(registerEmployeeForm, text='Publisher Name: ',font='Tahoma 10 bold')
        lblPubID.grid(row=6, column=0, padx=10, pady=10, sticky='w')
        txtPub = StringVar()
        getPubList()
        #PubList = ['0736-New Moon Books', '0877-Binnet & Hardley', '1389-Algodata Infosystems', '1622-Five Lakes Publishing', '1756-Ramona Publishers','9901-GGG&G', '9952-Scootney Books', '9999-Lucerne Publishing']
        cmbPubID = ttk.Combobox(registerEmployeeForm, width=36, textvariable=txtPub, values=PubList)
        cmbPubID.grid(row=6, column=1, padx=10, pady=10)


        lblHireDate = Label(registerEmployeeForm, text='Hire Date: ',font='Tahoma 10 bold')
        lblHireDate.grid(row=7, column=0, padx=10, pady=10, sticky='w')
        txtHireDate = StringVar()
        deHireDate = DateEntry(registerEmployeeForm, textvariable=txtHireDate, width=36)
        deHireDate.grid(row=7, column=1, padx=10, pady=10)

        btnBacktoMain = ttk.Button(registerEmployeeForm, width=15, text='Back To Main', command=backTomain)
        btnBacktoMain.grid(row=8, column=0, padx=20, pady=20, sticky='e')

        btnRegisterEmployee = ttk.Button(registerEmployeeForm, width=18, text='Register Employee', command=registerEmployee)
        btnRegisterEmployee.grid(row=8, column=1, padx=20, pady=20, sticky='w')

        btnResetForm = ttk.Button(registerEmployeeForm, width=15, text='Reset Form', command=resetForm)
        btnResetForm.grid(row=8, column=1, padx=20, pady=20, sticky='e')

        registerEmployeeForm.mainloop()
