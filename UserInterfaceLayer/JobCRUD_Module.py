
from tkinter import *
from tkinter import ttk, END
from tkcalendar import DateEntry
from tkinter import messagebox as msg
from Model.JobModel import JobModel_Class
from BusinessLogicLayer.Job_CRUD_BLL import Job_CRUD_BLL_Class
from Model.UserModel import UserModel_Class

class JobCRUD_UI_Class:
    def __init__(self, userModelObject:UserModel_Class):
        self.UserModel = userModelObject


    def JobCRUD_FormLoad(self):
        registerJobForm = Tk()
        registerJobForm.title('Register Your Job')
        registerJobForm.geometry('400x220')
        registerJobForm.resizable(False, False)
        registerJobForm.iconbitmap('images/Star.ico')
        x = int(registerJobForm.winfo_screenwidth() / 2 - 400 / 2)
        y = int(registerJobForm.winfo_screenheight() / 2 - 440 / 2)
        registerJobForm.geometry('+{}+{}'.format(x, y))

        # Define entry variables
        # txtJobDescription = StringVar()
        # txtMinLVL = StringVar()
        # txtMaxLVL = StringVar()

        def resetForm():
            for widget in registerJobForm.winfo_children():
                if isinstance(widget, ttk.Entry):
                    widget.delete(0, END)
                elif isinstance(widget, ttk.Combobox):
                    widget.set('')
                elif isinstance(widget, DateEntry):
                    widget.set_date('')

        def registerJob():
            jobModelObject = JobModel_Class(txtJobDescription.get(), txtMinLVL.get(), txtMaxLVL.get())
            jobCRUD_Object = Job_CRUD_BLL_Class()
            jobCRUD_Object.registerJob(jobModelObject)
            resetForm()
            msg.showinfo('Welcome', 'Register Job successfully')

        def backTomain():
            registerJobForm.destroy()
            from UserInterfaceLayer.Main_Module import MainUIClass
            mainUIObject = MainUIClass()
            mainUIObject.mainForm_Load(self.user)

        lblJobDescription = Label(registerJobForm, text='JobDescription: ')
        lblJobDescription.grid(row=2, column=0, padx=10, pady=10, sticky='w')
        txtJobDescription = StringVar()
        entJobDescription = ttk.Entry(registerJobForm, width=40, textvariable=txtJobDescription)
        entJobDescription.grid(row=2, column=1, padx=10, pady=10)

        lblMinLVL = Label(registerJobForm, text='Min Level: ')
        lblMinLVL.grid(row=3, column=0, padx=10, pady=10, sticky='w')
        txtMinLVL = StringVar()
        entMinLVL = ttk.Entry(registerJobForm, width=40, textvariable=txtMinLVL)
        entMinLVL.grid(row=3, column=1, padx=10, pady=10)

        lblMaxLVL = Label(registerJobForm, text='Max Level: ')
        lblMaxLVL.grid(row=4, column=0, padx=10, pady=10, sticky='w')
        txtMaxLVL = StringVar()
        entMaxLVL = ttk.Entry(registerJobForm, width=40, textvariable=txtMaxLVL)
        entMaxLVL.grid(row=4, column=1, padx=10, pady=10)

        btnBacktoMain = ttk.Button(registerJobForm, width=15, text='Back To Main', command=backTomain)
        btnBacktoMain.grid(row=5, column=0, padx=20, pady=20, sticky='e')

        btnregisterJobs = ttk.Button(registerJobForm, width=18, text='Register Jobs', command=registerJob)
        btnregisterJobs.grid(row=5, column=1, padx=20, pady=20, sticky='w')

        btnresetForm = ttk.Button(registerJobForm, width=15, text='ResetForm', command=resetForm)
        btnresetForm.grid(row=5, column=1, padx=20, pady=20, sticky='e')

        registerJobForm.mainloop()
