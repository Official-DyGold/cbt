from tkinter import *
from component.homeFrame import homeFrameUI, studentManagementUi, examManagementUI
from component.adminSwitchLogic import examSwitch, homeSwitch, studentSwitch
from component.defineQuery import logout

app = Tk()
app.geometry('500x500')
app.title('ESEF Amplitude Test (CBT)')
app.configure(background='#000')

# Home Frame
home_ui = homeFrameUI(app, lambda: homeSwitch(
    home_ui['homeFrameLine'], home_ui['homeFrame'], 
    student_ui['homeStudentManagementLine'], student_ui['homeStudentManagementFrame'], 
    exam_ui['homeExamManagementLine'], exam_ui['homeExamManagementFrame'], 
    home_ui['adminHomepage'], student_ui['adminStudentManagement'], 
    exam_ui['adminExamManagementButton'], home_ui['totalUserCount'], home_ui['totalUserAboveAverageCount'], home_ui['totalUserBelowAverageCount']
))

# Student Management
student_ui = studentManagementUi(app, lambda: studentSwitch(
    home_ui['homeFrameLine'], home_ui['homeFrame'], 
    student_ui['homeStudentManagementLine'], student_ui['homeStudentManagementFrame'], 
    exam_ui['homeExamManagementLine'], exam_ui['homeExamManagementFrame'], 
    home_ui['adminHomepage'], student_ui['adminStudentManagement'], 
    exam_ui['adminExamManagementButton']
))

# Exam Management
exam_ui = examManagementUI(app, lambda: examSwitch(
    home_ui['homeFrameLine'], home_ui['homeFrame'], 
    student_ui['homeStudentManagementLine'], student_ui['homeStudentManagementFrame'], 
    exam_ui['homeExamManagementLine'], exam_ui['homeExamManagementFrame'], 
    home_ui['adminHomepage'], student_ui['adminStudentManagement'], 
    exam_ui['adminExamManagementButton']
))

def adminLogout(): logout(app)
adminLogoutButton = Button(app, text='Logout', font=("Microsoft Yahei Ui Light", 9, 'bold'), fg='#000', bg='#fff', activebackground='red', activeforeground='#fff', border=0, command=adminLogout)
adminLogoutButton.place(x=415, y=20)

app.mainloop()