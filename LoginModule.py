from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msg
from BusinessLogicLayer.LoginBLL_Module import LoginBLL_Class
from Model.UserModel import UserModel_Class
from babel import dates
from babel import numbers



def set_background(loginForm, image_path):
    # Load the image (must be a GIF or PNG)
    background_image = PhotoImage(file=image_path)

    # Create a label to hold the image
    background_label = Label(loginForm, image=background_image)
    background_label.image = background_image  # Keep a reference to avoid garbage collection
    background_label.place(relwidth=1, relheight=1)

    return background_label

def loginEvent():
    userName = txtUserName.get()
    password = txtPassword.get()
    loginBLL_Object = LoginBLL_Class()
    loginBLL_Object.loginCheck(userName,password)
    rows = loginBLL_Object.loginCheck(userName,password)
    if len(rows) >0:
        # msg.showinfo('WellCome','Welcome')
        loginForm.destroy()
        from UserInterfaceLayer.Main_Module import MainUIClass
        userObject = UserModel_Class(userName= rows[0][0], password=rows[0][1],firstName=rows[0][2],lastName=rows[0][3], isAdmin=rows[0][4])
        mainUIObject = MainUIClass()
        mainUIObject.mainForm_Load(userObject)
    else:
        msg.showerror('Error', 'Invalid UserName and Password')

loginForm = Tk()


loginForm.title ('login Form')
loginForm.geometry('400x160')
loginForm.resizable (0,0)
loginForm.iconbitmap('images/Users.ico')

x = int(loginForm.winfo_screenwidth() / 2 - 400 / 2)
y = int(loginForm.winfo_screenheight() / 2 - 440 / 2)
loginForm.geometry('+{}+{}'.format(x, y))


lblUserName = Label(loginForm, text='User Name: ')
lblUserName.grid(row=0,column=0,padx=10,pady=10,sticky= 'e')
txtUserName=StringVar()
entUserName=ttk.Entry (loginForm,textvariable=txtUserName, width=40)
entUserName.grid (row=0,column=1,padx=10,pady=10, sticky='e')


lblPassword = Label(loginForm, text='Password: ')
lblPassword.grid(row=1,column=0,padx=10,pady=10,sticky= 'e')
txtPassword=StringVar()
entPassword=ttk.Entry (loginForm,textvariable=txtPassword, width=40, show='*')
entPassword.grid (row=1,column=1,padx=10,pady=10, sticky='e')


btnLogin=ttk.Button (loginForm, text='Login',width= 16, command=loginEvent)
btnLogin.grid(row=2,column=1,padx=10,pady=10, sticky='e')




loginForm.mainloop()