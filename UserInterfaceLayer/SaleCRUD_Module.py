from tkinter import *
from tkinter import ttk, END, font
from tkcalendar import DateEntry
from tkinter import messagebox as msg
from Model.SaleModel import SaleModel_Class
from BusinessLogicLayer.SaleCRUDBLL_Module import SaleCRUDBLL_CLass
from Model.UserModel import UserModel_Class
class SaleCRUD_UI_Class:
    def __init__(self, userModelObject : UserModel_Class):
        self.UserModel = userModelObject
    def SaleCRUD_FormLoad (self):
        registerSalesForm = Tk()
        registerSalesForm.title('Register Sale')
        registerSalesForm.geometry('420x300')
        registerSalesForm.resizable(False, False)
        registerSalesForm.iconbitmap('images/Star.ico')

        x = int(registerSalesForm.winfo_screenwidth() / 2 - 400 / 2)
        y = int(registerSalesForm.winfo_screenheight() / 2 - 360 / 2)
        registerSalesForm.geometry('+{}+{}'.format(x, y))
        TitleDict = {}
        TitleList = []
        StoreDict = {}
        StoreList = []


        def resetForm():
            for widget in registerSalesForm.winfo_children():
                if isinstance(widget, ttk.Entry):
                    widget.delete(0, END)
                elif isinstance(widget, ttk.Combobox):
                    widget.set('')


        def registerSale():
            saleModelObject = SaleModel_Class(StoreDict[txtStoreID.get()], txtOrderNum.get(), txtDate.get(),txtQty.get(),txtPayterm.get(),TitleDict[txtTitleID.get()])

            saleCRUD_Object = SaleCRUDBLL_CLass()
            saleCRUD_Object.registerSale(saleModelObject)
            resetForm()
            msg.showinfo('Welcome', 'Register Sale successfully')


        def getTitleList():
            from BusinessLogicLayer.Title_CRUD_BLL import Title_CRUD_BLL_Class
            Title_CRUD_BLL_Object = Title_CRUD_BLL_Class()
            rows = Title_CRUD_BLL_Object.getTitleList()
            for row in rows:
                if row[1] not in TitleDict:
                    TitleDict[row[1]] = row[0]
            for Title in TitleDict.keys():
                TitleList.append(Title)

        def getStoreList():
            from BusinessLogicLayer.StoreCRUDBLL_Module import StoreCRUDBLL_CLass
            Store_CRUD_BLL_Object = StoreCRUDBLL_CLass()
            rows = Store_CRUD_BLL_Object.getStoreList()
            for row in rows:
                if row[1] not in StoreDict:
                    StoreDict[row[1]] = row[0]
            for Store in StoreDict.keys():
                StoreList.append(Store)


        def backTomain():
            registerSalesForm.destroy()
            from UserInterfaceLayer.Main_Module import MainUIClass
            mainUIObject = MainUIClass()
            mainUIObject.mainForm_Load(self.UserModel)


        lblStoreID = Label(registerSalesForm, text='Store ID: ')
        lblStoreID.grid(row=0, column=0, padx=10, pady=10, sticky='w')
        txtStoreID = StringVar()
        getStoreList()
        cmbStoreID = ttk.Combobox(registerSalesForm, width=37, textvariable=txtStoreID, values=StoreList)
        cmbStoreID.grid(row=0, column=1, padx=10, pady=10)

        lblOrderNum = Label(registerSalesForm, text='Order Number: ')
        lblOrderNum.grid(row=1, column=0, padx=10, pady=10, sticky='w')
        txtOrderNum = StringVar()
        entOrderNum = ttk.Entry(registerSalesForm, width=40, textvariable=txtOrderNum)
        entOrderNum.grid(row=1, column=1, padx=10, pady=10)

        lblDate = Label(registerSalesForm, text='Date: ')
        lblDate.grid(row=2, column=0, padx=10, pady=10, sticky='w')
        txtDate = StringVar()
        deDate = DateEntry(registerSalesForm, textvariable=txtDate, width=36)
        deDate.grid(row=2, column=1, padx=10, pady=10)

        lblQty = Label(registerSalesForm, text='Quantity: ')
        lblQty.grid(row=3, column=0, padx=10, pady=10, sticky='w')
        txtQty = StringVar()
        entQty = ttk.Entry(registerSalesForm, width=40, textvariable=txtQty)
        entQty.grid(row=3, column=1, padx=10, pady=10)

        lblPayterm = Label(registerSalesForm, text='Payterm: ')
        lblPayterm.grid(row=4, column=0, padx=10, pady=10, sticky='w')
        txtPayterm = StringVar()
        PaytermList = ['Net 30', 'Net 60', 'ON invoice']
        cmbPayterm = ttk.Combobox(registerSalesForm, width=37, textvariable=txtPayterm, values=PaytermList)
        cmbPayterm.grid(row=4, column=1, padx=10, pady=10)

        lblTitleID = Label(registerSalesForm, text='TitleID: ')
        lblTitleID.grid(row=5, column=0, padx=10, pady=10, sticky='w')
        txtTitleID = StringVar()
        getTitleList()
        cmbTitleID = ttk.Combobox(registerSalesForm, width=37, textvariable=txtTitleID, values=TitleList)
        cmbTitleID.grid(row=5, column=1, padx=10, pady=10)

        btnBacktoMain = ttk.Button(registerSalesForm, width=15, text='Back To Main', command=backTomain)
        btnBacktoMain.grid(row=6, column=0, padx=20, pady=20, sticky='e')

        btnRegisterSale = ttk.Button(registerSalesForm, width=18, text='Register Sale', command=registerSale)
        btnRegisterSale.grid(row=6, column=1, padx=20, pady=20, sticky='w')

        btnResetForm = ttk.Button(registerSalesForm, width=15, text='Reset Form', command=resetForm)
        btnResetForm.grid(row=6, column=1, padx=20, pady=20, sticky='e')

        registerSalesForm.mainloop()
