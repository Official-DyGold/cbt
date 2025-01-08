from tkinter import *
from component.defineQuery import logout, submitExamMessage
from component.defineQuery import fetchUser

# Admin homepage fetch function
def fetchAll(totalUserCount, totalUserAboveAverageCount, totalUserBelowAverageCount):
    tableName = 'user_details'
    columnName = 'user_ID'
    whereClause = ''
    decider = 1
    value1 = fetchUser(tableName, columnName, whereClause, decider)
    totalUserCount.config(text=value1)
    tableName2 = 'result_details'
    columnName2 = 'score'
    whereClause2 = 40
    decider = 2
    value2 = fetchUser(tableName2, columnName2, whereClause2, decider)
    totalUserAboveAverageCount.config(text=value2)
    decider = 3
    value3 = fetchUser(tableName2, columnName2, whereClause2, decider)
    totalUserBelowAverageCount.config(text=value3)

# Admin exam page clear function
def clearHomeObject(userID, studentFullname, studentEmail, option1, option2, option3, option4, answer):
        userID.delete(0, 'end')
        studentFullname.delete(0, 'end')
        studentEmail.delete(0, 'end')
        option1.delete(0, 'end')
        option2.delete(0, 'end')
        option3.delete(0, 'end')
        option4.delete(0, 'end')
        answer.delete(0, 'end')

# Admin user page clear function
def clearHomeObject_2(userID, studentFullname, studentEmail):
    userID.delete(0, 'end')
    studentFullname.delete(0, 'end')
    studentEmail.delete(0, 'end')

# Admin homepage function
def homeFrameUI(app, homeSwitch):
    adminHomepage = Button(app, text='Admin Homepage', font=("Microsoft Yahei Ui Light", 9, 'bold'), fg='#000', bg='#fff', activebackground='#000', activeforeground='#fff', border=0, command=homeSwitch)
    adminHomepage.place(x=20, y=20)
    homeFrameLine = Frame(height=20, width=15, bg='#fff')
    homeFrameLine.place(x=65, y=45)
    homeFrame = Frame(height=400, width=450, bg='#fff')
    homeFrame.place(x=20, y=65)    

    homepageHeader = Label(homeFrame, text='Exam Summery', font=("Microsoft Yahei Ui Light", 15, 'bold'), bg='#fff', fg='#000')
    homepageHeader.place(x=140, y=20)

    totalUser = Label(homeFrame, text='Total User', font=("Microsoft Yahei Ui Light", 12, 'bold'), bg='#fff', fg='#000')
    totalUser.place(x=40, y=100)
    totalUserCount = Label(homeFrame, font=("Microsoft Yahei Ui Light", 12, 'bold'), bg='#fff', fg='#000')
    totalUserCount.place(x=70, y=150)

    totalUserAboveAverage = Label(homeFrame, text='User Above Average', font=("Microsoft Yahei Ui Light", 12, 'bold'), bg='#fff', fg='#000')
    totalUserAboveAverage.place(x=220, y=100)
    totalUserAboveAverageCount = Label(homeFrame, text='#', font=("Microsoft Yahei Ui Light", 12, 'bold'), bg='#fff', fg='#000')
    totalUserAboveAverageCount.place(x=300, y=150)

    totalUserBelowAverage = Label(homeFrame, text='User Below Average', font=("Microsoft Yahei Ui Light", 12, 'bold'), bg='#fff', fg='#000')
    totalUserBelowAverage.place(x=130, y=230)
    totalUserBelowAverageCount = Label(homeFrame, text='#', font=("Microsoft Yahei Ui Light", 12, 'bold'), bg='#fff', fg='#000')
    totalUserBelowAverageCount.place(x=210, y=280)

    fetchAll(totalUserCount, totalUserAboveAverageCount, totalUserBelowAverageCount)
    return {
        'adminHomepage': adminHomepage,
        'homeFrameLine': homeFrameLine,
        'homeFrame': homeFrame,
        'totalUserCount': totalUserCount, 
        'totalUserAboveAverageCount': totalUserAboveAverageCount,
        'totalUserBelowAverageCount': totalUserBelowAverageCount
    }

# Admin student registration page function
def studentManagementUi(app, studentSwitch):
    adminStudentManagement = Button(app, text='Manage Student', font=("Microsoft Yahei Ui Light", 9, 'bold'), fg='#000', bg='gray', activebackground='#000', activeforeground='#fff', border=0, command=studentSwitch)
    adminStudentManagement.place(x=150, y=20)
    homeStudentManagementLine = Frame(height=20, width=15, bg='gray')
    homeStudentManagementLine.place(x=195, y=45)
    homeStudentManagementFrame = Frame(height=400, width=450, bg='#fff',)

    studentHeader = Label(homeStudentManagementFrame, text='Student Details', font=("Microsoft Yahei Ui Light", 15, 'bold'), bg='#fff', fg='#000')
    studentHeader.place(x=140, y=20)
    userIDLabel = Label(homeStudentManagementFrame, text='Student ID', font=("Microsoft Yahei Ui Light", 11, 'bold'), bg='#FFF', fg='#000')
    userIDLabel.place(x=10, y=70)
    userID =  Entry(homeStudentManagementFrame, width=21, font=("Microsoft Yahei Ui Light", 11, 'bold'), border=2)
    userID.place(x=10, y=100)

    #generate or fetch user query
    from component.defineQuery import generateOrSearchID
    def idClick():
        studentReport.config(text='')
        user_ID = userID.get()
        letter = 'ESEF/PYTHON'
        tableName = 'user_details'
        columnName = 'user_id'
        studentReport.config(text='')
        result = generateOrSearchID(user_ID, letter, tableName, columnName)
        if isinstance(result, str):  
            if result.startswith('ESEF/PYTHON'): 
                userID.insert(0, result)
            else: 
                studentReport.config(text=result, fg='red')
    
        elif isinstance(result, tuple):
            tableName1 = 'result_details'
            columnName1 = 'user_id'
            decider = 4
            result1 = fetchUser(tableName1, columnName1, user_ID, decider)
            studentScore.config(text=result1)
            fullname, email = result
            studentFullname.delete(0, 'end')
            studentEmail.delete(0, 'end')
            studentFullname.insert(0, fullname)
            studentEmail.insert(0, email)

    studentIdButton = Button(homeStudentManagementFrame, text='Generate/Search Student', font=("Microsoft Yahei Ui Light", 9, 'bold'), fg='#fff', bg='#000', activebackground='#fff', activeforeground='#000', border=0, width=23, command=idClick)
    studentIdButton.place(x=240, y=100)
    studentFullnameLabel = Label(homeStudentManagementFrame, text='Full Name', font=("Microsoft Yahei Ui Light", 11, 'bold'), bg='#FFF', fg='#000')
    studentFullnameLabel.place(x=10, y=150)
    studentFullname =  Entry(homeStudentManagementFrame, width=21, font=("Microsoft Yahei Ui Light", 11, 'bold'), border=2)
    studentFullname.place(x=10, y=180)
    studentEmailLabel = Label(homeStudentManagementFrame, text='Email Address', font=("Microsoft Yahei Ui Light", 11, 'bold'), bg='#FFF', fg='#000')
    studentEmailLabel.place(x=240, y=150)
    studentEmail =  Entry(homeStudentManagementFrame, width=21, font=("Microsoft Yahei Ui Light", 11, 'bold'), border=2)
    studentEmail.place(x=240, y=180)

    studentScore = Label(homeStudentManagementFrame, font=("Microsoft Yahei Ui Light", 11, 'bold'), bg='#FFF', fg='#000')
    studentScore.place(x=10, y=210)
    studentReport = Label(homeStudentManagementFrame, font=("Microsoft Yahei Ui Light", 11, 'bold'), bg='#fff')
    studentReport.place(x=10, y=260)

    #save user query
    from component.defineQuery import saveUser

    def saveCommand():
        user_ID = userID.get()
        student_Fullname = studentFullname.get()
        student_Email = studentEmail.get()
        letter = 'ESEF/PYTHON'
        tableName = 'user_details'
        columnName = ('user_id', 'fullname', 'email')
        saveUser(studentReport, user_ID, student_Fullname, student_Email, tableName, columnName, letter)
        clearHomeObject_2(userID, studentFullname, studentEmail)

    studentSaveButton = Button(homeStudentManagementFrame, text='Add Student', font=("Microsoft Yahei Ui Light", 9, 'bold'), fg='#fff', bg='#000', activebackground='#fff', activeforeground='#000', border=0, width=23, command=saveCommand)
    studentSaveButton.place(x=10, y=300)

    #update user query
    from component.defineQuery import updateUser

    def updateCommand():
        user_ID = userID.get()
        student_Fullname = studentFullname.get()
        student_Email = studentEmail.get()
        tableName = 'user_details'
        columnName = ('user_id', 'fullname', 'email')
        updateUser(studentReport, user_ID, student_Fullname, student_Email, tableName, columnName)
        clearHomeObject_2(userID, studentFullname, studentEmail)

    studentUpdateButton = Button(homeStudentManagementFrame, text='Update Student', font=("Microsoft Yahei Ui Light", 9, 'bold'), fg='#fff', bg='#000', activebackground='#fff', activeforeground='#000', border=0, width=23, command=updateCommand)
    studentUpdateButton.place(x=240, y=300)

    return {
        'adminStudentManagement': adminStudentManagement,
        'homeStudentManagementLine': homeStudentManagementLine,
        'homeStudentManagementFrame': homeStudentManagementFrame
    }

# Admin exam registration page function
def examManagementUI(app, examSwitch):
    adminExamManagementButton = Button(app, text='Manage Exam', font=("Microsoft Yahei Ui Light", 9, 'bold'), fg='#000', bg='gray', activebackground='#000', activeforeground='#fff', border=0, command=examSwitch)
    adminExamManagementButton.place(x=270, y=20)
    homeExamManagementLine = Frame(height=20, width=15, bg='gray')
    homeExamManagementLine.place(x=315, y=45)
    homeExamManagementFrame = Frame(height=400, width=450, bg='#fff')

    studentHeader = Label(homeExamManagementFrame, text='Exam Details', font=("Microsoft Yahei Ui Light", 15, 'bold'), bg='#fff', fg='#000')
    studentHeader.place(x=150, y=10)
    userIDLabel = Label(homeExamManagementFrame, text='Exam ID', font=("Microsoft Yahei Ui Light", 11, 'bold'), bg='#FFF', fg='#000')
    userIDLabel.place(x=10, y=40)
    userID =  Entry(homeExamManagementFrame, width=21, font=("Microsoft Yahei Ui Light", 11, 'bold'), border=2)
    userID.place(x=10, y=60)

    #generate or fetch exam query
    from component.defineQuery import generateOrSearchIDForExam
    def idClick():
        studentReport.config(text='')
        user_ID = userID.get()
        letter = 'ESEF/PYTHON/QTN'
        tableName = 'exam_details'
        columnName = 'exam_id'
        result = generateOrSearchIDForExam(user_ID, letter, tableName, columnName)
        studentReport.config(text='')
        if isinstance(result, str):  
            if result.startswith('ESEF/PYTHON/QTN'): 
                userID.insert(0, result)
            else: 
                studentReport.config(text=result, fg='red')
    
        elif isinstance(result, tuple):  
            fullname, email, option_1, option_2, option_3, option_4, answer_to = result
            studentFullname.delete(0, 'end')
            studentEmail.delete(0, 'end')
            option1.delete(0, 'end')
            option2.delete(0, 'end')
            option3.delete(0, 'end')
            option4.delete(0, 'end')
            answer.delete(0, 'end')
            studentFullname.insert(0, fullname)
            studentEmail.insert(0, email)
            option1.insert(0, option_1)
            option2.insert(0, option_2)
            option3.insert(0, option_3)
            option4.insert(0, option_4)
            answer.insert(0, answer_to)
            

    studentIdButton = Button(homeExamManagementFrame, text='Generate/Search Exam ID', font=("Microsoft Yahei Ui Light", 9, 'bold'), fg='#fff', bg='#000', activebackground='#fff', activeforeground='#000', border=0, width=23, command=idClick)
    studentIdButton.place(x=240, y=60)
    studentFullnameLabel = Label(homeExamManagementFrame, text='Exam Question', font=("Microsoft Yahei Ui Light", 11, 'bold'), bg='#FFF', fg='#000')
    studentFullnameLabel.place(x=10, y=90)
    studentFullname =  Entry(homeExamManagementFrame, width=46, font=("Microsoft Yahei Ui Light", 11, 'bold'), border=2)
    studentFullname.place(x=10, y=110)
    studentEmailLabel = Label(homeExamManagementFrame, text='Question Instruction', font=("Microsoft Yahei Ui Light", 11, 'bold'), bg='#FFF', fg='#000')
    studentEmailLabel.place(x=10, y=140)
    studentEmail =  Entry(homeExamManagementFrame, width=46, font=("Microsoft Yahei Ui Light", 11, 'bold'), border=2,)
    studentEmail.place(x=10, y=160)
    option1Label = Label(homeExamManagementFrame, text='Option A', font=("Microsoft Yahei Ui Light", 11, 'bold'), bg='#FFF', fg='#000')
    option1Label.place(x=10, y=190)
    option1 =  Entry(homeExamManagementFrame, width=21, font=("Microsoft Yahei Ui Light", 11, 'bold'), border=2)
    option1.place(x=10, y=210)
    option2Label = Label(homeExamManagementFrame, text='Option B', font=("Microsoft Yahei Ui Light", 11, 'bold'), bg='#FFF', fg='#000')
    option2Label.place(x=235, y=190)
    option2 =  Entry(homeExamManagementFrame, width=21, font=("Microsoft Yahei Ui Light", 11, 'bold'), border=2)
    option2.place(x=235, y=210)
    option3Label = Label(homeExamManagementFrame, text='Option C', font=("Microsoft Yahei Ui Light", 11, 'bold'), bg='#FFF', fg='#000')
    option3Label.place(x=10, y=240)
    option3 =  Entry(homeExamManagementFrame, width=21, font=("Microsoft Yahei Ui Light", 11, 'bold'), border=2)
    option3.place(x=10, y=260)
    option4Label = Label(homeExamManagementFrame, text='Option D', font=("Microsoft Yahei Ui Light", 11, 'bold'), bg='#FFF', fg='#000')
    option4Label.place(x=235, y=240)
    option4 =  Entry(homeExamManagementFrame, width=21, font=("Microsoft Yahei Ui Light", 11, 'bold'), border=2)
    option4.place(x=235, y=260)
    answerLabel = Label(homeExamManagementFrame, text='Correct Answer', font=("Microsoft Yahei Ui Light", 11, 'bold'), bg='#FFF', fg='#000')
    answerLabel.place(x=10, y=290)
    answer =  Entry(homeExamManagementFrame, width=21, font=("Microsoft Yahei Ui Light", 11, 'bold'), border=2)
    answer.place(x=10, y=310)
    studentReport = Label(homeExamManagementFrame, font=("Microsoft Yahei Ui Light", 11, 'bold'), bg='#fff')
    studentReport.place(x=235, y=290)

    #save exam query
    from component.defineQuery import saveExam

    def saveCommand():
        user_ID = userID.get()
        student_Fullname = studentFullname.get()
        student_Email = studentEmail.get()
        option_1 = option1.get()
        option_2 = option2.get()
        option_3 = option3.get()
        option_4 = option4.get()
        answer_to = answer.get()
        letter = 'ESEF/PYTHON/QTN'
        tableName = 'exam_details'
        columnName = ('exam_id', 'exam_qts', 'exam_instructions', 'option1', 'option2', 'option3', 'option4', 'answer')
        saveExam(studentReport, user_ID, student_Fullname, student_Email, tableName, columnName, letter, option_1, option_2, option_3, option_4, answer_to)
        clearHomeObject(userID, studentFullname, studentEmail, option1, option2, option3, option4, answer)

    studentSaveButton = Button(homeExamManagementFrame, text='Add Exam', font=("Microsoft Yahei Ui Light", 9, 'bold'), fg='#fff', bg='#000', activebackground='#fff', activeforeground='#000', border=0, width=23, command=saveCommand)
    studentSaveButton.place(x=235, y=310)

    #update exam query
    from component.defineQuery import updateExam

    def updateCommand():
        user_ID = userID.get()
        student_Fullname = studentFullname.get()
        student_Email = studentEmail.get()
        option_1 = option1.get()
        option_2 = option2.get()
        option_3 = option3.get()
        option_4 = option4.get()
        answer_to = answer.get()
        tableName = 'exam_details'
        columnName = ('exam_id', 'exam_qts', 'exam_instructions', 'option1', 'option2', 'option3', 'option4', 'answer')
        updateExam(studentReport, user_ID, student_Fullname, student_Email, tableName, columnName, option_1, option_2, option_3, option_4, answer_to)
        clearHomeObject(userID, studentFullname, studentEmail, option1, option2, option3, option4, answer)

    studentUpdateButton = Button(homeExamManagementFrame, text='Update Exam', font=("Microsoft Yahei Ui Light", 9, 'bold'), fg='#fff', bg='#000', activebackground='#fff', activeforeground='#000', border=0, width=23, command=updateCommand)
    studentUpdateButton.place(x=10, y=360)

    #delete exam ID
    from component.defineQuery import deleteUser

    def deleteCommand():
        user_ID = userID.get()
        student_Fullname = studentFullname.get()
        student_Email = studentEmail.get()
        tableName = 'exam_details'
        columnName = ('exam_id')
        deleteUser(studentReport, user_ID, student_Fullname, student_Email, tableName, columnName)
        clearHomeObject(userID, studentFullname, studentEmail, option1, option2, option3, option4, answer)

    examDeleteButton = Button(homeExamManagementFrame, text='Delete Exam', font=("Microsoft Yahei Ui Light", 9, 'bold'), fg='#fff', bg='#000', activebackground='red', activeforeground='#fff', border=0, width=23, command=deleteCommand)
    examDeleteButton.place(x=235, y=360)

    return {
        'adminExamManagementButton': adminExamManagementButton,
        'homeExamManagementLine': homeExamManagementLine,
        'homeExamManagementFrame': homeExamManagementFrame
    }

# Fetching current user function
def fetchUserID():
        with open('user_details.txt', 'r') as file:
            user_ID = file.read().strip()
        return user_ID

# User header page function
def userHeader(app, userProfileSwitch):
    headerFrame = Frame(app, bg='#fff', width=690, height=50)
    headerFrame.place(x=5, y=5)
    userID = Label(headerFrame, text='User ID - ' + fetchUserID(), bg='#fff', fg='#000', font=("Microsoft Yahei Ui Light", 12, 'bold'))

    def userLogout(): logout(app)

    userID.place(x=10, y=10)
    userProfileButton = Button(headerFrame, text='Profile', font=("Microsoft Yahei Ui Light", 9, 'bold'), fg='#000', bg='#fff', activebackground='#000', activeforeground='#fff', border=0, width=15, command=userProfileSwitch)
    userProfileButton.place(x=420, y=10)
    userLogoutButton = Button(headerFrame, text='Logout', font=("Microsoft Yahei Ui Light", 9, 'bold'), fg='#fff', bg='#000', activebackground='red', activeforeground='#fff', border=0, width=15, command=userLogout)
    userLogoutButton.place(x=555, y=10)

# User homepage function
def userHomePage(app, userExamSwitch):
    homepageFrame = Frame(app, bg='#fff', width=690, height=435)
    homepageFrame.place(x=5, y=60)
    examHeader = Label(homepageFrame, text='Exam Instructions', font=("Microsoft Yahei Ui Light", 15, 'bold'), bg='#fff', fg='#000')
    examHeader.place(x=270, y=70)
    examQuestion = Label(homepageFrame, text='#', bg='#fff', fg='#000', font=("Microsoft Yahei Ui Light", 11, 'bold'))
    examQuestion.place(x=50, y=120)
    examQuestion = Label(homepageFrame, text='#', bg='#fff', fg='#000', font=("Microsoft Yahei Ui Light", 11, 'bold'))
    examQuestion.place(x=50, y=150)
    startExamButton = Button(homepageFrame, text='Start Exam', font=("Microsoft Yahei Ui Light", 11, 'bold'), fg='#000', bg='#fff', activebackground='#000', activeforeground='#fff', border=0, width=20, command=userExamSwitch)
    startExamButton.place(x=470, y=380)
    return {'homepageFrame': homepageFrame}

current_question = 0
score = 0
option_buttons = [] 
exam_duration = 1 * 60
time_left = exam_duration

# User exam page function function
def userExamPage(app, userHomeSwitch):
    global selected_option
    selected_option = StringVar()

    homeExamFrame = Frame(app, bg='#fff', width=690, height=435)
    backButton = Button(homeExamFrame, text='Back to HomePage', font=("Microsoft Yahei Ui Light", 9, 'bold'), fg='#000', bg='#fff', activebackground='#000', activeforeground='#fff', border=0, width=20, command=userHomeSwitch)
    backButton.place(x=10, y=10)

    from component.defineQuery import fetchAllQuestions
    questions = fetchAllQuestions()

    # Display exam function
    def displayQuestion(option_buttons):
        global current_question
        examInstruction.config(text=f"Question instruction: {questions[current_question][2]}", fg='#000')
        examQuestion.config(text=f"Question {current_question + 1}: {questions[current_question][1]}")
        options = questions[current_question][3:7]
        idChecking.insert(0, questions[current_question][0])
        for i, option in enumerate(options):
            option_buttons[i].config(text=option, value=option)

    # Display answer option button function
    def loadButton(option_buttons):
        for i in range(4):
            btn = Radiobutton(homeExamFrame, text="", variable=selected_option, font=("Microsoft Yahei Ui Light", 12, 'bold'), value="", indicatoron=0, width=40, bg='#fff', fg='#000', activebackground='green', border=3)
            btn.place(x=130, y=200 + i * 40)
            option_buttons.append(btn)
        return option_buttons

    # start exam function
    def startExam():
        tableName1 = 'result_details'
        columnName1 = 'user_id'
        user_ID =  fetchUserID()
        decider = 5
        result1 = fetchUser(tableName1, columnName1, user_ID, decider)
        if result1:
            examInstruction.config(text="You have already take this exam", fg='#000')
        else:
            userStartButton.place_forget()
            userEndButton.place(x=555, y=10)
            global current_question, option_buttons
            startTimer()
            displayQuestion(loadButton(option_buttons))

    # Display next question function
    def nextQuestion():        
        global current_question, score, option_buttons
        if idChecking.get() == '':
            examInstruction.config(text="You can't move to the next question! Click on START EXAM BUTTON", fg='red')
        else:
            user_answers[current_question] = selected_option.get()
            previousButton.place(x=10, y=380)
            if selected_option.get() == questions[current_question][7]:
                score += 4

            current_question += 1

            if current_question < len(questions):
                selected_option.set("")  
                displayQuestion(option_buttons)
                selected_option.set(user_answers[current_question]) 

                if current_question == len(questions) - 1:
                    nextButton.place_forget()
                    submitButton.place(x=470, y=380)   

    user_answers = [""] * len(questions) 

    # Display previous question function
    def previousQuestion():
        global current_question, score, option_buttons
        user_answers[current_question] = selected_option.get()
        if current_question > 0:
            current_question -= 1

        displayQuestion(option_buttons)
        selected_option.set(user_answers[current_question])

        if current_question == 0: 
            previousButton.place_forget()
        else:
            previousButton.place(x=10, y=380)  
        nextButton.place(x=470, y=380)

        if current_question < len(questions) - 1:
            submitButton.place_forget()

    # End exam function
    def endExam():
        row = submitExamMessage()
        if row:
            endExamQuery()
        
    # End exam query function
    def endExamQuery():
        from component.defineQuery import saveUserResult
        global current_question, score, option_buttons
        if selected_option.get() == questions[current_question][7]:
            score += 4

        user_id = fetchUserID()
        saveUserResult(user_id, score)
        userStartButton.place(x=555, y=10)
        userEndButton.place_forget()
        previousButton.place_forget()
        submitButton.place_forget()
        nextButton.place(x=470, y=380)
        idChecking.delete(0, 'end')
        current_question = 0
        score = 0
        selected_option.set("")
        examInstruction.config(text="Please click on the START EXAM BUTTON to start exam")
        examQuestion.config(text="")
        for btn in option_buttons:
            btn.destroy()
        option_buttons = []

    # exam timer
    def startTimer():
        global time_left
        if time_left > 0:
            minutes, seconds = divmod(time_left, 60)
            formatted_time = f"{minutes:02}:{seconds:02}"
            examTimer.config(text=formatted_time, fg='green')
            if time_left <= 5 * 60:
                examTimer.config(fg="red")

            time_left -= 1
            app.after(1000, startTimer)  
        else:
            examTimer.config(text="00:00")
            endExamQuery()
            examTimer.place_forget()

    idChecking = Entry(homeExamFrame)
    examTimer = Label(homeExamFrame, font=("Microsoft Yahei Ui Light", 15, 'bold'), bg='#fff', fg='#000')
    examTimer.place(x=430, y=10)
    userStartButton = Button(homeExamFrame, text='Start Exam', font=("Microsoft Yahei Ui Light", 9, 'bold'), fg='#fff', bg='green', activebackground='#fff', activeforeground='green', border=0, width=15, command=startExam)
    userStartButton.place(x=555, y=10)
    userEndButton = Button(homeExamFrame, text='End Exam', font=("Microsoft Yahei Ui Light", 9, 'bold'), fg='#fff', bg='red', activebackground='#fff', activeforeground='red', border=0, width=15, command=endExam)
    examHeader = Label(homeExamFrame, text='Take Exam', font=("Microsoft Yahei Ui Light", 15, 'bold'), bg='#fff', fg='#000')
    examHeader.place(x=280, y=60)
    examInstruction = Label(homeExamFrame, text='Please click on the START EXAM BUTTON to start exam', bg='#fff', fg='#000', font=("Microsoft Yahei Ui Light", 11, 'bold'))
    examInstruction.place(x=50, y=100)
    examQuestion = Label(homeExamFrame, bg='#fff', fg='#000', font=("Microsoft Yahei Ui Light", 11, 'bold'))
    examQuestion.place(x=50, y=130)

    previousButton = Button(homeExamFrame, text='Previous Question', font=("Microsoft Yahei Ui Light", 11, 'bold'), fg='#000', bg='#fff', activebackground='#000', activeforeground='#fff', border=0, width=20, command=previousQuestion)
    nextButton = Button(homeExamFrame, text='Next Question', font=("Microsoft Yahei Ui Light", 11, 'bold'), fg='#000', bg='#fff', activebackground='#000', activeforeground='#fff', border=0, width=20, command=nextQuestion)
    nextButton.place(x=470, y=380)
    submitButton = Button(homeExamFrame, text='Submit Exam', font=("Microsoft Yahei Ui Light", 11, 'bold'), fg='#000', bg='#fff', activebackground='#000', activeforeground='#fff', border=0, width=20, command=endExam)
    return {'homeExamFrame': homeExamFrame}

# User profile function  
def userProfile(app, userHomeSwitch):
    homeProfileFrame = Frame(app, bg='#fff', width=690, height=435)
    backButton = Button(homeProfileFrame, text='Back to HomePage', font=("Microsoft Yahei Ui Light", 9, 'bold'), fg='#000', bg='#fff', activebackground='#000', activeforeground='#fff', border=0, width=20, command=userHomeSwitch)
    backButton.place(x=10, y=10)

    # fetch user details function
    def fetchProfile():
        tableName1 = 'user_details'
        columnName1 = 'user_id'
        user_ID =  fetchUserID()
        decider = 5
        result1 = fetchUser(tableName1, columnName1, user_ID, decider)
        tableName1 = 'result_details'
        decider = 4
        result4 = fetchUser(tableName1, columnName1, user_ID, decider)
        if result1:
            examQuestion.config(text=f'Fullname - {result1[0][2]}')
            examQuestion2.config(text=f'Email - {result1[0][3]}')
            examQuestion3.config(text=result4)
        else:
            examHeader.config(text='Login Error: Please re-login')

    examHeader = Label(homeProfileFrame, text='Profile Details', font=("Microsoft Yahei Ui Light", 15, 'bold'), bg='#fff', fg='#000')
    examHeader.place(x=270, y=70)
    examQuestion = Label(homeProfileFrame, bg='#fff', fg='#000', font=("Microsoft Yahei Ui Light", 11, 'bold'))
    examQuestion.place(x=50, y=120)
    examQuestion2 = Label(homeProfileFrame, bg='#fff', fg='#000', font=("Microsoft Yahei Ui Light", 11, 'bold'))
    examQuestion2.place(x=50, y=150)
    examQuestion3 = Label(homeProfileFrame, bg='#fff', fg='#000', font=("Microsoft Yahei Ui Light", 11, 'bold'))
    examQuestion3.place(x=50, y=180)

    fetchProfile()

    return {'homeProfileFrame': homeProfileFrame}