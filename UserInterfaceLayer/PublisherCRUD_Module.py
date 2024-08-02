from tkinter import *
from tkinter import ttk, END
from tkcalendar import DateEntry
from tkinter import messagebox as msg
from Model.PubModel import PublisherModel_Class
from BusinessLogicLayer.Pub_CRUD_BLL import Pub_CRUD_BLL_Class
from Model.UserModel import UserModel_Class


class PublisherCRUD_UI_Class:
    def __init__(self, userModelObject : UserModel_Class):
        self.UserModel = userModelObject


    def PublisherCRUD_FormLoad (self):
        registerPublisherForm = Tk()
        registerPublisherForm.title('Register Employee')
        registerPublisherForm.geometry('400x300')
        registerPublisherForm.resizable(False, False)
        registerPublisherForm.iconbitmap('images/Users.ico')

        x = int(registerPublisherForm.winfo_screenwidth() / 2 - 400 / 2)
        y = int(registerPublisherForm.winfo_screenheight() / 2 - 440 / 2)
        registerPublisherForm.geometry('+{}+{}'.format(x, y))


        def resetForm():
            for widget in registerPublisherForm.winfo_children():
                if isinstance(widget, ttk.Entry):
                    widget.delete(0, END)
                elif isinstance(widget, ttk.Combobox):
                    widget.set('')
                elif isinstance(widget, DateEntry):
                    widget.set_date('')


        def registerPublisher():
            publisherModelObject = PublisherModel_Class(txtPublisherID.get(), txtPublisherName.get(), txtCity.get(),txtState.get(),txtCountry.get())

            publisherCRUD_Object = Pub_CRUD_BLL_Class()
            publisherCRUD_Object.registerPublisher(publisherModelObject)
            resetForm()
            msg.showinfo('Welcome', 'Register Publisher successfully')


        def backTomain():
            registerPublisherForm.destroy()
            from UserInterfaceLayer.Main_Module import MainUIClass
            mainUIObject = MainUIClass()
            mainUIObject.mainForm_Load(self.UserModel)


        lblPublisherID = Label(registerPublisherForm, text='Publisher ID: ')
        lblPublisherID.grid(row=0, column=0, padx=10, pady=10, sticky='w')
        txtPublisherID = StringVar()
        entPublisherID = ttk.Entry(registerPublisherForm, width=40, textvariable=txtPublisherID)
        entPublisherID.grid(row=0, column=1, padx=10, pady=10)

        lblPublisherName = Label(registerPublisherForm, text='Publisher Name: ')
        lblPublisherName.grid(row=1, column=0, padx=10, pady=10, sticky='w')
        txtPublisherName = StringVar()
        entPublisherName = ttk.Entry(registerPublisherForm, width=40, textvariable=txtPublisherName)
        entPublisherName.grid(row=1, column=1, padx=10, pady=10)

        lblCity = Label(registerPublisherForm, text='City: ')
        lblCity.grid(row=2, column=0, padx=10, pady=10, sticky='w')
        txtCity = StringVar()
        entCity = ttk.Entry(registerPublisherForm, width=40, textvariable=txtCity)
        entCity.grid(row=2, column=1, padx=10, pady=10)

        lblState = Label(registerPublisherForm, text='State: ')
        lblState.grid(row=3, column=0, padx=10, pady=10, sticky='w')
        txtState = StringVar()
        StateList = ['CA', 'IN', 'KS', 'MD', 'MI', 'OR', 'TN', 'UT']
        cmbState = ttk.Combobox(registerPublisherForm, width=36, textvariable=txtState, values=StateList)
        cmbState.grid(row=3, column=1, padx=10, pady=10)

        lblCountry = Label(registerPublisherForm, text='Country: ')
        lblCountry.grid(row=4, column=0, padx=10, pady=10, sticky='w')
        txtCountry = StringVar()
        CountryList = ['France', 'Germany', 'USA']
        cmbCountry = ttk.Combobox(registerPublisherForm, width=36, textvariable=txtCountry, values=CountryList)
        cmbCountry.grid(row=4, column=1, padx=10, pady=10)


        btnBacktoMain = ttk.Button(registerPublisherForm, width=15, text='Back To Main', command=backTomain)
        btnBacktoMain.grid(row=5, column=0, padx=20, pady=20, sticky='e')

        btnRegisterPublisher = ttk.Button(registerPublisherForm, width=18, text='Register Publisher',command=registerPublisher)
        btnRegisterPublisher.grid(row=5, column=1, padx=20, pady=20, sticky='w')

        btnResetForm = ttk.Button(registerPublisherForm, width=15, text='Reset Form', command=resetForm)
        btnResetForm.grid(row=5, column=1, padx=20, pady=20, sticky='e')

        registerPublisherForm.mainloop()
