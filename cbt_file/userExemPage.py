from tkinter import *
from component.homeFrame import userHeader, userHomePage, userExamPage, userProfile
from component.adminSwitchLogic import userExamSwitch, userHomeSwitch, userProfileSwitch

app = Tk()
app.geometry('700x500')
app.title('ESEF Amplitude Test (CBT)')
app.configure(background='#000')

header_ui = userHeader(app, lambda:userProfileSwitch(
    home_ui['homepageFrame'], exam_ui['homeExamFrame'], profile_ui['homeProfileFrame']
))

home_ui = userHomePage(app, lambda: userExamSwitch(
    home_ui['homepageFrame'], exam_ui['homeExamFrame'], profile_ui['homeProfileFrame']
))

exam_ui = userExamPage(app, lambda: userHomeSwitch(
    home_ui['homepageFrame'], exam_ui['homeExamFrame'], profile_ui['homeProfileFrame']
))

profile_ui = userProfile(app, lambda: userHomeSwitch(
    home_ui['homepageFrame'], exam_ui['homeExamFrame'], profile_ui['homeProfileFrame']
))

app.mainloop()