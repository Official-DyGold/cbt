import random
import string
import tkinter.messagebox as messageBox
from component.model import checkDB, bdQuery, fetchDB

# Logout message function
def logout(app):
        reply = messageBox.askyesno('Logout', 'Are you sure you want to logout')
        if reply:
            app.destroy()  

# Logout message function
def submitExamMessage():
        reply = messageBox.askyesno('End Exam', 'Are you sure you want to submit and end this exam')
        if reply:
            return reply

# User and admin login funtion
def userLoginQuery(tableName, columnName, user_id, password):
    if password == '':
        queryCheck = f"SELECT * FROM {tableName} WHERE {columnName} = %s"
        row = checkDB(queryCheck, (user_id,))
        return row
    else:
        queryCheck = f"SELECT * FROM {tableName} WHERE {columnName[0]} = %s AND {columnName[1]} = %s"
        row = checkDB(queryCheck, (user_id, password))
        return row

# user ID generation/fetching function
def generateOrSearchID(user_ID, letter, tableName, columnName):
    if user_ID == '':
        number = ''.join(random.choices(string.digits, k=3))
        random_id = letter + '/' + number
        return random_id
    else:
        queryCheck = f"SELECT * FROM {tableName} WHERE {columnName} = %s"
        row = checkDB(queryCheck, (user_ID,))
        if row:
            fullname = row[0][2]
            email = row[0][3]
            return fullname, email
        else:
            error = 'ID not Found! Please register this ID'
            return error
        
# function fetch data (profile, score)
def fetchUser(tableName, columnName, whereClause, decider):
    if decider == 1:
        queryCheck = f"SELECT COUNT(*) FROM {tableName}" 
        report = fetchDB(queryCheck)
        return report
    elif decider == 2:
        queryCheck = f"SELECT COUNT(*) FROM {tableName} WHERE {columnName} < {whereClause}" 
        report = fetchDB(queryCheck)
        return report
    elif decider == 3:
        queryCheck = f"SELECT COUNT(*) FROM {tableName} WHERE {columnName} > {whereClause}" 
        report = fetchDB(queryCheck)
        return report
    elif decider == 4:
        queryCheck = f"SELECT score FROM {tableName} WHERE {columnName} = '{whereClause}'" 
        report = fetchDB(queryCheck)
        if report:
            examReport = f'Your score is - {report[0]}'
            return examReport
        else:
            return 'Exam not taken yet'
    elif decider == 5:
        queryCheck = f"SELECT * FROM {tableName} WHERE {columnName} = %s" 
        report = checkDB(queryCheck, (whereClause,))
        if report:
            return report
        else:
            return None

#user save function
def saveUser(studentReport, user_ID, student_Fullname, student_Email, tableName, columnName, letter):
    query = f"INSERT INTO {tableName} ({', '.join(columnName)}) VALUES (%s, %s, %s)"
    queryCheck = f"SELECT * FROM {tableName} WHERE {columnName[0]} = %s" 
    if user_ID == '' or student_Fullname == '' or student_Email == '':
        studentReport.config(text='All field most not be empty', fg='red')
    else:
        if user_ID.startswith(letter):
            row = checkDB(queryCheck, (user_ID,))
            if row:
                studentReport.config(text='ID Already Exist', fg='red')
            else:
                reportLabel = 'Saved'
                report = bdQuery(query, reportLabel, (user_ID, student_Fullname, student_Email))
                studentReport.config(text=report, fg='green')
        else: 
            studentReport.config(text="Invalid ID", fg='red')

#user update function
def updateUser(studentReport, user_ID, student_Fullname, student_Email,tableName, columnName):
    query = f"UPDATE {tableName} SET  {columnName[1]} = %s, {columnName[2]} = %s WHERE {columnName[0]} = %s"
    queryCheck = f"SELECT * FROM {tableName} WHERE {columnName[0]} = %s"
    if user_ID == '':
        studentReport.config(text='ID field cannot be empty', fg='red')
    elif student_Fullname == '' or student_Email == '':
        studentReport.config(text='Please click on search button', fg='red')
    else:
        row = checkDB(queryCheck, (user_ID,))
        if row:
            reportLabel = 'Updated'
            report = bdQuery(query, reportLabel, (student_Fullname, student_Email, user_ID))
            studentReport.config(text=report, fg='green')
        else:
            studentReport.config(text='ID does not exist', fg='red')

# exam ID generation/fetching function
def generateOrSearchIDForExam(user_ID, letter, tableName, columnName):
    if user_ID == '':
        number = ''.join(random.choices(string.digits, k=3))
        random_id = letter + '/' + number
        return random_id
    else:
        queryCheck = f"SELECT * FROM {tableName} WHERE {columnName} = %s"
        row = checkDB(queryCheck, (user_ID,))
        if row:
            fullname = row[0][2]
            email = row[0][3]
            option_1 = row[0][5]
            option_2 = row[0][6]
            option_3 = row[0][7]
            option_4 = row[0][8]
            answer_to = row[0][9]
            return fullname, email, option_1, option_2, option_3, option_4, answer_to
        else:
            error = 'ID not Found!'
            return error

# exam save function
def saveExam(studentReport, user_ID, student_Fullname, student_Email, tableName, columnName, letter, option_1, option_2, option_3, option_4, answer_to):
    query = f"INSERT INTO {tableName} ({', '.join(columnName)}) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    queryCheck = f"SELECT * FROM {tableName} WHERE {columnName[0]} = %s" 
    if user_ID == '' or student_Fullname == '' or student_Email == '' or option_1 == '' or option_2 == '' or option_3 == '' or option_4 == '' or answer_to == '':
        studentReport.config(text='All field most not be empty', fg='red')
    else:
        if user_ID.startswith(letter):
            row = checkDB(queryCheck, (user_ID,))
            if row:
                studentReport.config(text='ID Already Exist', fg='red')
            else:
                reportLabel = 'Saved'
                report = bdQuery(query, reportLabel, (user_ID, student_Fullname, student_Email, option_1, option_2, option_3, option_4, answer_to))
                studentReport.config(text=report, fg='green')
        else: 
            studentReport.config(text="Invalid ID", fg='red')

# exam update function
def updateExam(studentReport, user_ID, student_Fullname, student_Email, tableName, columnName, option_1, option_2, option_3, option_4, answer_to):
    query = f"UPDATE {tableName} SET  {columnName[1]} = %s, {columnName[2]} = %s, {columnName[3]} = %s, {columnName[4]} = %s, {columnName[5]} = %s, {columnName[6]} = %s, {columnName[7]} = %s WHERE {columnName[0]} = %s"
    queryCheck = f"SELECT * FROM {tableName} WHERE {columnName[0]} = %s"
    if user_ID == '':
        studentReport.config(text='ID field cannot be empty', fg='red')
    elif student_Fullname == '' or student_Email == '' or option_1 == '' or option_2 == '' or option_3 == '' or option_4 == '' or answer_to == '':
        studentReport.config(text='Please click on search button', fg='red')
    else:
        row = checkDB(queryCheck, (user_ID,))
        if row:
            reportLabel = 'Updated'
            report = bdQuery(query, reportLabel, (student_Fullname, student_Email, option_1, option_2, option_3, option_4, answer_to, user_ID))
            studentReport.config(text=report, fg='green')
        else:
            studentReport.config(text='ID does not exist', fg='red')

# exam delete function
def deleteUser(studentReport, user_ID, student_Fullname, student_Email,tableName, columnName):
    query = f"DELETE FROM {tableName} WHERE {columnName} = %s"
    queryCheck = f"SELECT * FROM {tableName} WHERE {columnName} = %s"
    if user_ID == '':
        studentReport.config(text='ID field cannot be empty', fg='red')
    elif student_Fullname == '' or student_Email == '':
        studentReport.config(text='Please click on search button', fg='red')
    else:
        reply2 = messageBox.askyesno('Delete ID Details', 'Are you sure you want to delete this ID details')
        if reply2:
             row = checkDB(queryCheck, (user_ID,))
             if row:
                reportLabel = 'Deleted'
                report = bdQuery(query, reportLabel, (user_ID,))
                studentReport.config(text=report, fg='green')
             else:
                studentReport.config(text='ID does not exist', fg='red')
                
# fetch question function
def fetchAllQuestions():
    query = "SELECT exam_id, exam_qts, exam_instructions, option1, option2, option3, option4, answer FROM exam_details"
    result = checkDB(query)
    return result

# save score function
def saveUserResult(user_id, score):
    query = f"INSERT INTO result_details (user_id, score) VALUES (%s, %s)"
    reportLabel = 'Score Saved'
    result = bdQuery(query, reportLabel, (user_id, score))
    return result
     