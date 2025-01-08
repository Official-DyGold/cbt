from tkinter import *
import subprocess
from component.defineQuery import userLoginQuery

app = Tk()
app.geometry('500x500')
app.title('ESEF Amplitude Test (CBT)')
app.configure(background='#000')

# Login Section
def loginAuthentication():
    loginFrame = Frame(app, bg='#000', width=494, height=494)
    loginFrame.place(x=2, y=2)
    backButton = Label(loginFrame, text='Back', font=("Microsoft Yahei Ui Light", 11, 'bold'), bg='#000', fg='#fff', cursor='hand2')
    backButton.place(x=450, y=5)
    backButton.bind('<Button-1>', lambda e: homepage())
    titleLabel = Label(loginFrame, text='Amplitude Test (CBT) Login Page', font=("Microsoft Yahei Ui Light", 20, 'bold'), bg='#000', fg='#fff')
    titleLabel.place(x=30, y=50)

    # user switch function
    def userPanel():
        adminFrame.place_forget()
        userLoginButton.place_forget()
        userFrame.place(x=30, y=100)
        adminLoginButton.place(x=250, y=100)

    # admin switch function
    def adminPanel():
        userFrame.place_forget()
        adminLoginButton.place_forget()
        adminFrame.place(x=250, y=100)
        userLoginButton.place(x=30, y=100)

    # Admin login function
    def adminLoginCommand():
        adminError.config(text='')
        if adminUsername.get() == '' or adminPassword.get() == '':
            adminError.config(text='Both field cannot be empty', fg='red', font=9)
        else:
            user_id = adminUsername.get()
            password = adminPassword.get()
            tableName = 'admin_details'
            columnName = ['username', 'password']
            row = userLoginQuery(tableName, columnName, user_id, password)
            if row:
                subprocess.run(['python', 'cbt_file/adminhomepage.py'], check=True)
            else:
                adminError.config(text='Invalid Login Details', fg='red', font=11)
        adminUsername.delete(0, 'end')
        adminPassword.delete(0, 'end')

    adminLoginButton = Button(loginFrame, text='Admin Login', font=("Microsoft Yahei Ui Light", 11, 'bold'), height=15, width=20, fg='#fff', bg='#000', activebackground='#fff', activeforeground='#000', border=2, command=adminPanel)
    adminLoginButton.place(x=250, y=100)
    userLoginButton = Button(loginFrame, text='User Login', font=("Microsoft Yahei Ui Light", 11, 'bold'), height=15, width=20, fg='#fff', bg='#000', activebackground='#fff', activeforeground='#000', border=2, command=userPanel)
    userLoginButton.place(x=30, y=100)

    adminFrame = Frame(loginFrame, bg='#fff', height=315, width=215)
    # adminFrame.place(x=40, y=110)
    adminLoginLabel = Label(adminFrame, text='ADMIN LOGIN', font=("Microsoft Yahei Ui Light", 11, 'bold'), bg='#FFF', fg='#000')
    adminLoginLabel.place(x=40, y=50)
    adminUsername =  Entry(adminFrame, width=21, font=("Microsoft Yahei Ui Light", 11, 'bold'), border=2)
    adminUsername.place(x=10, y=90)
    adminPassword = Entry(adminFrame, width=21, font=("Microsoft Yahei Ui Light", 11, 'bold'), show='.', border=2)
    adminPassword.place(x=10, y=130)
    adminError = Label(adminFrame, font=("Microsoft Yahei Ui Light", 11, 'bold'), bg='#FFF', fg='#000')
    adminError.place(x=10, y=170)
    adminLogin = Button(adminFrame, text='Login', font=("Microsoft Yahei Ui Light", 11, 'bold'), width=18, fg='#fff', bg='#000', activebackground='#fff', activeforeground='#000', border=2, command=adminLoginCommand)
    adminLogin.place(x=10, y=210)

    userFrame = Frame(loginFrame, bg='#fff', height=315, width=215)
    # userFrame.place(x=260, y=110)
    userLoginLabel = Label(userFrame,  text='USER LOGIN', font=("Microsoft Yahei Ui Light", 11, 'bold'), bg='#FFF', fg='#000')
    userLoginLabel.place(x=50, y=50)
    userUniqueID = Entry(userFrame, width=21, font=("Microsoft Yahei Ui Light", 11, 'bold'), border=2)
    userUniqueID.place(x=10, y=90)

    # User login function
    def userLoginCommand():
        userError.config(text='')
        if userUniqueID.get() == '':
            userError.config(text='ID field cannot be empty', fg='red', font=9)
        else:
            user_id = userUniqueID.get()
            tableName = 'user_details'
            columnName = 'user_id'
            password = ''
            row = userLoginQuery(tableName, columnName, user_id, password)
            if row:
                try:
                    with open("user_details.txt", "w") as file:
                        file.truncate()
                        file.write(user_id)
                    subprocess.run(['python', 'cbt_file/userExemPage.py'], check=True)
                except subprocess.CalledProcessError as e:
                    userError.config(text=f"Error: {e}", fg='red', font=11)
            else:
                userError.config(text='Invalid Login Details', fg='red', font=11)
        userUniqueID.delete(0, 'end')

    userError = Label(userFrame, font=("Microsoft Yahei Ui Light", 11, 'bold'), bg='#FFF', fg='#000')
    userError.place(x=10, y=130)
    userLogin = Button(userFrame, text='Login', font=("Microsoft Yahei Ui Light", 11, 'bold'), width=18, fg='#fff', bg='#000', activebackground='#fff', activeforeground='#000', border=2, command=userLoginCommand)
    userLogin.place(x=10, y=170)

    descLabel = Label(app, text='Please login as either you are admin or student (Please know \nthat student can only login in with your unique ID to have \naccess to the test)', font=("Microsoft Yahei Ui Light", 11, 'bold'), bg='#000', fg='#fff')
    descLabel.place(x=10, y=420)

# Homepage Section
def homepage():
    homeFrame = Frame(app, bg='#000', width=494, height=494)
    homeFrame.place(x=2, y=2)
    titleLabel = Label(homeFrame, text='ESEF Amplitude Test (CBT)', font=("Microsoft Yahei Ui Light", 20, 'bold'), bg='#000', fg='#fff')
    titleLabel.place(x=80, y=50)
    nextButton = Button(homeFrame, text='Next', font=("Microsoft Yahei Ui Light", 11, 'bold'), bg='#000', fg='#fff', activebackground='#fff', activeforeground='#000', command=loginAuthentication, cursor='hand2', border=0, width=20)
    nextButton.place(x=150, y=430)

homepage()
app.mainloop()