from component.homeFrame import fetchAll

# Admin home switch Function
def homeSwitch(homeFrameLine, homeFrame, homeStudentManagementLine, homeStudentManagementFrame, 
               homeExamManagementLine, homeExamManagementFrame, adminHomepage, adminStudentManagement,
               adminExamManagementButton, totalUserCount, totalUserAboveAverageCount, totalUserBelowAverageCount):
    fetchAll(totalUserCount, totalUserAboveAverageCount, totalUserBelowAverageCount)
    homeFrameLine.config(bg='#fff')
    homeFrame.place(x=20, y=65)
    homeStudentManagementLine.config(bg='gray')
    homeStudentManagementFrame.place_forget()
    homeExamManagementLine.config(bg='gray')
    homeExamManagementFrame.place_forget()
    adminHomepage.config(bg='#fff')
    adminStudentManagement.config(bg='gray')
    adminExamManagementButton.config(bg='gray')

# Admin user switch Function
def studentSwitch(homeFrameLine, homeFrame, homeStudentManagementLine, homeStudentManagementFrame, 
                  homeExamManagementLine, homeExamManagementFrame, adminHomepage, adminStudentManagement, 
                  adminExamManagementButton):
    homeFrameLine.config(bg='gray')
    homeFrame.place_forget()
    homeStudentManagementLine.config(bg='#fff')
    homeStudentManagementFrame.place(x=20, y=65)
    homeExamManagementLine.config(bg='gray')
    homeExamManagementFrame.place_forget()
    adminHomepage.config(bg='gray')
    adminStudentManagement.config(bg='#fff')
    adminExamManagementButton.config(bg='gray')

# Admin exam switch Function
def examSwitch(homeFrameLine, homeFrame, homeStudentManagementLine, homeStudentManagementFrame, homeExamManagementLine, 
               homeExamManagementFrame, adminHomepage, adminStudentManagement, adminExamManagementButton):
    homeFrameLine.config(bg='gray')
    homeFrame.place_forget()
    homeStudentManagementLine.config(bg='gray')
    homeStudentManagementFrame.place_forget()
    homeExamManagementLine.config(bg='#fff')
    homeExamManagementFrame.place(x=20, y=65)
    adminHomepage.config(bg='gray')
    adminStudentManagement.config(bg='gray')
    adminExamManagementButton.config(bg='#fff')

# User home switch Function
def userHomeSwitch(homepageFrame, homeExamFrame, homeProfileFrame):
    homepageFrame.place(x=5, y=60)
    homeExamFrame.place_forget()
    homeProfileFrame.place_forget()

# User exam switch Function
def userExamSwitch(homepageFrame, homeExamFrame, homeProfileFrame):
    homepageFrame.place_forget()
    homeExamFrame.place(x=5, y=60)
    homeProfileFrame.place_forget()

# User profile switch Function
def userProfileSwitch(homepageFrame, homeExamFrame, homeProfileFrame):
    homepageFrame.place_forget()
    homeExamFrame.place_forget()
    homeProfileFrame.place(x=5, y=60)