from tkinter import *
from tkinter import ttk, END, font
from tkcalendar import DateEntry
from tkinter import messagebox as msg
from Model.StoreModel import StoreModel_Class
from BusinessLogicLayer.StoreCRUDBLL_Module import StoreCRUDBLL_CLass
from Model.UserModel import UserModel_Class


class StoreCRUD_UI_Class:
    def __init__(self, userModelObject : UserModel_Class):
        self.UserModel = userModelObject
    def StoreCRUD_FormLoad (self):
        registerStoreForm = Tk()
        registerStoreForm.title('Register Your Stores')
        registerStoreForm.geometry('400x310')
        registerStoreForm.resizable(False, False)
        registerStoreForm.iconbitmap('images/books.ico')

        x = int(registerStoreForm.winfo_screenwidth() / 2 - 400 / 2)
        y = int(registerStoreForm.winfo_screenheight() / 2 - 440 / 2)
        registerStoreForm.geometry('+{}+{}'.format(x, y))


        def resetForm():
            for widget in registerStoreForm.winfo_children():
                if isinstance(widget, ttk.Entry):
                    widget.delete(0, END)
                elif isinstance(widget, ttk.Combobox):
                    widget.set('')


        def registerStore():
            storeModelObject = StoreModel_Class(txtStoreID.get(), txtStoreName.get(), txtStoreAddress.get(),
                                                      txtCity.get(), txtState.get(),txtZip.get())

            storeCRUD_Object = StoreCRUDBLL_CLass()
            storeCRUD_Object.registerStore(storeModelObject)
            resetForm()
            msg.showinfo('Welcome', 'Register Store successfully')

        def backTomain():
            registerStoreForm.destroy()
            from UserInterfaceLayer.Main_Module import MainUIClass
            mainUIObject = MainUIClass()
            mainUIObject.mainForm_Load(self.UserModel)

        lblStoreID = Label(registerStoreForm, text='StoreID: ')
        lblStoreID.grid(row=0, column=0, padx=10, pady=10, sticky='w')
        txtStoreID = StringVar()
        entStoreID = ttk.Entry(registerStoreForm, width=40, textvariable=txtStoreID)
        entStoreID.grid(row=0, column=1, padx=10, pady=10)

        lblStoreName = Label(registerStoreForm, text='Store Name: ')
        lblStoreName.grid(row=1, column=0, padx=10, pady=10, sticky='w')
        txtStoreName = StringVar()
        entStoreName = ttk.Entry(registerStoreForm, width=40, textvariable=txtStoreName)
        entStoreName.grid(row=1, column=1, padx=10, pady=10)

        lblStoreAddress = Label(registerStoreForm, text='Store Address: ')
        lblStoreAddress.grid(row=2, column=0, padx=10, pady=10, sticky='w')
        txtStoreAddress = StringVar()
        entStoreAddress = ttk.Entry(registerStoreForm, width=40, textvariable=txtStoreAddress)
        entStoreAddress.grid(row=2, column=1, padx=10, pady=10)

        lblCity = Label(registerStoreForm, text='City: ')
        lblCity.grid(row=3, column=0, padx=10, pady=10, sticky='w')
        txtCity = StringVar()
        entCity = ttk.Entry(registerStoreForm, width=40, textvariable=txtCity)
        entCity.grid(row=3, column=1, padx=10, pady=10)

        lblState = Label(registerStoreForm, text='State: ')
        lblState.grid(row=4, column=0, padx=10, pady=10, sticky='w')
        txtState = StringVar()
        StateList = ['CA', 'IN', 'KS', 'MD', 'MI', 'OR', 'TN', 'UT']
        cmbState = ttk.Combobox(registerStoreForm, width=36, textvariable=txtState, values=StateList)
        cmbState.grid(row=4, column=1, padx=10, pady=10)

        lblZip = Label(registerStoreForm, text='Zip: ')
        lblZip.grid(row=5, column=0, padx=10, pady=10, sticky='w')
        txtZip = StringVar()
        entZip = ttk.Entry(registerStoreForm, width=40, textvariable=txtZip)
        entZip.grid(row=5, column=1, padx=10, pady=10)

        btnBacktoMain = ttk.Button(registerStoreForm, width=15, text='Back To Main', command=backTomain)
        btnBacktoMain.grid(row=6, column=0, padx=20, pady=20, sticky='e')

        btnRegisterStore = ttk.Button(registerStoreForm, width=18, text='Register Store', command=registerStore)
        btnRegisterStore.grid(row=6, column=1, padx=20, pady=20, sticky='w')

        btnResetForm = ttk.Button(registerStoreForm, width=15, text='Reset Form', command=resetForm)
        btnResetForm.grid(row=6, column=1, padx=20, pady=20, sticky='e')

        registerStoreForm.mainloop()
