from tkinter import *
from tkinter import ttk, END
from tkinter import messagebox as msg
from Model.AuthorModel import AuthorModel_Class
from BusinessLogicLayer.AuthorCRUDBLL_Module import AuthorCRUDBLL_CLass
from Model.UserModel import UserModel_Class


class AuthorCRUD_UI_Class:
    def __init__(self, userModelObject: UserModel_Class):
        self.UserModel = userModelObject

    def AuthorCRUD_FormLoad(self):
        registerAuthorForm = Tk()
        registerAuthorForm.title('Register Author')
        registerAuthorForm.geometry('400x440')
        registerAuthorForm.resizable(False, False)
        registerAuthorForm.iconbitmap('images/User.ico')

        x = int(registerAuthorForm.winfo_screenwidth() / 2 - 400 / 2)
        y = int(registerAuthorForm.winfo_screenheight() / 2 - 440 / 2)
        registerAuthorForm.geometry('+{}+{}'.format(x, y))

        def resetForm():
            for widget in registerAuthorForm.winfo_children():
                if isinstance(widget, ttk.Entry):
                    widget.delete(0, END)
                elif isinstance(widget, ttk.Combobox):
                    widget.set('')
                elif isinstance(widget, ttk.Radiobutton):
                    intContract.set(1)  # Reset to 'Yes' as default

        def registerAuthor():
            authorModelObject = AuthorModel_Class(
                txtAuthorID.get(), txtLastName.get(), txtFirstName.get(),
                txtPhone.get(), txtAddress.get(), txtCity.get(),
                txtState.get(), txtZip.get(), intContract.get()
            )

            authorCRUD_Object = AuthorCRUDBLL_CLass()
            authorCRUD_Object.registerAuthor(authorModelObject)
            resetForm()
            msg.showinfo('Success', 'Register Author successfully')

        def backTomain():
            registerAuthorForm.destroy()
            from UserInterfaceLayer.Main_Module import MainUIClass
            mainUIObject = MainUIClass()
            mainUIObject.mainForm_Load(self.UserModel)

        lblAuthorID = Label(registerAuthorForm, text='Author ID: ')
        lblAuthorID.grid(row=0, column=0, padx=10, pady=10, sticky='w')
        txtAuthorID = StringVar()
        entAuthorID = ttk.Entry(registerAuthorForm, width=40, textvariable=txtAuthorID)
        entAuthorID.grid(row=0, column=1, padx=10, pady=10)

        lblLastName = Label(registerAuthorForm, text='Last Name: ')
        lblLastName.grid(row=1, column=0, padx=10, pady=10, sticky='w')
        txtLastName = StringVar()
        entLastName = ttk.Entry(registerAuthorForm, width=40, textvariable=txtLastName)
        entLastName.grid(row=1, column=1, padx=10, pady=10)

        lblFirstName = Label(registerAuthorForm, text='First Name: ')
        lblFirstName.grid(row=2, column=0, padx=10, pady=10, sticky='w')
        txtFirstName = StringVar()
        entFirstName = ttk.Entry(registerAuthorForm, width=40, textvariable=txtFirstName)
        entFirstName.grid(row=2, column=1, padx=10, pady=10)

        lblPhone = Label(registerAuthorForm, text='Phone: ')
        lblPhone.grid(row=3, column=0, padx=10, pady=10, sticky='w')
        txtPhone = StringVar()
        entPhone = ttk.Entry(registerAuthorForm, width=40, textvariable=txtPhone)
        entPhone.grid(row=3, column=1, padx=10, pady=10)

        lblAddress = Label(registerAuthorForm, text='Address: ')
        lblAddress.grid(row=4, column=0, padx=10, pady=10, sticky='w')
        txtAddress = StringVar()
        entAddress = ttk.Entry(registerAuthorForm, width=40, textvariable=txtAddress)
        entAddress.grid(row=4, column=1, padx=10, pady=10)

        lblCity = Label(registerAuthorForm, text='City: ')
        lblCity.grid(row=5, column=0, padx=10, pady=10, sticky='w')
        txtCity = StringVar()
        entCity = ttk.Entry(registerAuthorForm, width=40, textvariable=txtCity)
        entCity.grid(row=5, column=1, padx=10, pady=10)

        lblState = Label(registerAuthorForm, text='State: ')
        lblState.grid(row=6, column=0, padx=10, pady=10, sticky='w')
        txtState = StringVar()
        StateList = ['CA', 'IN', 'KS', 'MD', 'MI', 'OR', 'TN', 'UT']
        cmbState = ttk.Combobox(registerAuthorForm, width=36, textvariable=txtState, values=StateList)
        cmbState.grid(row=6, column=1, padx=10, pady=10)

        lblZip = Label(registerAuthorForm, text='Zip: ')
        lblZip.grid(row=7, column=0, padx=10, pady=10, sticky='w')
        txtZip = StringVar()
        entZip = ttk.Entry(registerAuthorForm, width=40, textvariable=txtZip)
        entZip.grid(row=7, column=1, padx=10, pady=10)

        lblContract = Label(registerAuthorForm, text='Contract: ')
        lblContract.grid(row=8, column=0, padx=10, pady=10, sticky='w')
        intContract = IntVar()
        rdbContractYes = ttk.Radiobutton(registerAuthorForm, text='Yes', variable=intContract, value=1)
        rdbContractYes.grid(row=8, column=1, padx=60, pady=10, sticky='w')
        rdbContractNo = ttk.Radiobutton(registerAuthorForm, text='No', variable=intContract, value=2)
        rdbContractNo.grid(row=8, column=1, padx=60, pady=10, sticky='e')
        intContract.set(1)

        btnBacktoMain = ttk.Button(registerAuthorForm, width=15, text='Back To Main', command=backTomain)
        btnBacktoMain.grid(row=9, column=0, padx=20, pady=20, sticky='e')

        btnRegisterAuthor = ttk.Button(registerAuthorForm, width=18, text='Register Author', command=registerAuthor)
        btnRegisterAuthor.grid(row=9, column=1, padx=20, pady=20, sticky='w')

        btnResetForm = ttk.Button(registerAuthorForm, width=15, text='Reset Form', command=resetForm)
        btnResetForm.grid(row=9, column=1, padx=20, pady=20, sticky='e')

        registerAuthorForm.mainloop()
