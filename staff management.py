#importing of packages
import sqlite3
from tkinter import *
from tkinter import ttk, Checkbutton, IntVar, Button, messagebox, filedialog
import tkinter
staffRoles=[]
staffArray=[]
staffUserNames=[]
staffPasswords=[]
tasks=[]
roles=[]
managers=[]
staffNames=[]
count=0
global counter
counter=0

#getting the tick box entry as a value of 1 if it is ticked and 0 if it is not ticked
def enter():
  print(managerCheck.get())
  if managerCheck.get() == 1:
    staffRoles.append("Manager")
  if cashierCheck.get() == 1:
    staffRoles.append("Cahsier")
  if cleanerCheck.get() == 1:
    staffRoles.append("Cleaner")
  if bakerCheck.get() == 1:
    staffRoles.append("Baker")
  if stockerCheck.get() == 1:
    staffRoles.append("Stocker")
  print(staffRoles)
  managerCheckButton.destroy()
  cashierCheckButton.destroy()
  cleanerCheckButton.destroy()
  bakerCheckButton.destroy()
  stockerCheckButton.destroy()
  enterButton.destroy()
  label.destroy()
  staffCreator.pack()
  staffNumberSpinbox.pack()
  staffEnterButton.pack()

  return
#creating my front end, and then the role select window
root = tkinter.Tk()
root.geometry("400x400")
root.title("Staff Management System")
label=tkinter.Label(root,text="Role creation")
managerCheck=IntVar()
cashierCheck=IntVar()
cleanerCheck=IntVar()
bakerCheck=IntVar()
stockerCheck=IntVar()
managerCheckButton = Checkbutton(root, text='Manger', variable=managerCheck, onvalue=1, offvalue=0)
cashierCheckButton = Checkbutton(root, text='Cashier', variable=cashierCheck, onvalue=1, offvalue=0)
cleanerCheckButton = Checkbutton(root, text='Cleaner', variable=cleanerCheck, onvalue=1, offvalue=0)
bakerCheckButton = Checkbutton(root, text='Baker', variable=bakerCheck, onvalue=1, offvalue=0)
stockerCheckButton = Checkbutton(root, text='Stocker', variable=stockerCheck, onvalue=1, offvalue=0)
enterButton = Button(root, text='Enter', command=lambda:enter())
label.pack()
managerCheckButton.pack()
cashierCheckButton.pack()
cleanerCheckButton.pack()
bakerCheckButton.pack()
stockerCheckButton.pack()
enterButton.pack()

##########################################################################
#staff member class
class StaffMember():
  def __init__(self, staffID, firstName, surname, staffRole, weeklyHours, payPerHour):
      self.firstName = staffName.capitalize()


      self.surname = surname.capitalize()
      #while self.surname.isalpha()==False:
       # self.surname = input("Enter the staff's surname: ")
      #self.surname = self.surname.capitalize()
      self.staffID = str(staffID)
      self.staffRole=staffRole.capitalize()
      if self.staffRole  not in staffRoles:
        print("You did not enter a valid role")
        while self.staffRole not in staffRoles:
          self.staffRole= input("Enter a valid staff role: ").capitalize()
      #weeklyHours validation
      self.weeklyHours=weeklyHours
      self.payPerHour=payPerHour 
     #get user name method
  def getUserName(self):
    self.userName= self.firstName.capitalize()+"."+self.surname.capitalize()
    return

  #staff timetable viewer
  def staffTimetable(self):
    #hides window when back button is pressed
    def hideWindow():
      timetable.withdraw()
      makeTimetable.pack_forget()
      backButton.destroy()
      return
    if count ==0:
      print("There is no timetable availible")
    else:
      timetable.deiconify()
      makeTimetable.pack()
      backButton = tkinter.Button(timetable, text="Go Back", command=hideWindow)
      backButton.pack()
    return

    #staff task viewer
  def checkTasks(self,staffCode):
    #hides window when back button is pressed
    def hideWindow():
      taskUI.withdraw()
      taskList.pack_forget()
      backButton.destroy()
      return
    if count ==0:
      print("There is no task list availible")
    else:
      taskUI.deiconify()
      taskList.pack()
      backButton = tkinter.Button(taskUI, text="Go Back", command=hideWindow)
      backButton.pack()
    return

  #payslip function
  def payslip(self,staffCode):
    #gives the user options to open the file
    def openFile():
      filePath=filedialog.askopenfilename()
      file=open(filePath,"r")
      file.close()
      #downloads the txt file for the user
    def download():
      file=open(name,"w")
      file.write("You worked " + str(self.weeklyHours) + " hours this week and your hourly rate is £" + str(self.payPerHour))
      file.write("\n You have been paid £" + str(totalPay) + " this week")
      file.write("\n You have been paid £"+str(monthlyPay) + " this month")
      file.close()
      return
    payslipUI=tkinter.Tk()
    payslipUI.geometry("500x500")
    payslipUI.title("Payslip")
    #pay calculation
    totalPay = int(self.weeklyHours) * int(self.payPerHour)
    monthlyPay=totalPay*4
    print("\n You have been paid ",monthlyPay)
    name=("payslip"+ str(self.firstName)+".txt")
    messagebox.showinfo(title="Paylslip", message="you have been paid "+ str(monthlyPay))
    payslipUI.deiconify()
    downloadButton=tkinter.Button(payslipUI, text="Download", command=download)
    openButton=tkinter.Button(payslipUI, text="Open", command=openFile)
    downloadButton.pack()
    openButton.pack()
    logoutButton = tkinter.Button(payslipUI, text="Logout", command=payslipUI.destroy,)
    logoutButton.pack()
    return  

  ###############################################################
  #staff area selection procedure
  def staffArea(self,staffCode):
    #creates the staff area window
    staffUI = tkinter.Tk()
    staffUI.title("Select a function")
    staffUI.geometry('500x500')
    logoutButton = tkinter.Button(staffUI, text="Logout", command=staffUI.destroy, height=5, width=5)
    logoutButton.grid(row=0, column=0)
    timetableButton= tkinter.Button(staffUI, text="View Timetable", command=lambda:self.staffTimetable(), height=5, width=5)
    timetableButton.grid(row=0, column=4 )
    taskButton= tkinter.Button(staffUI, text="View and Assign Tasks", command=lambda:self.checkTasks(staffCode), height=5, width=5)
    taskButton.grid(row=0, column=8 )
    payslipButton= tkinter.Button(staffUI, text="Get Payslip", command=lambda:self.payslip(staffCode), height=5, width=5)
    payslipButton.grid(row=0, column=2)
    return
###############################################################################
#manager class creation
class Manager(StaffMember):
  def __init__ (self, staffID, firstName, surname, staffRole, weeklyHours, payPerHour,userName):

    self.staffID = staffArray[locate].staffID
    self.firstName = staffArray[locate].firstName
    self.surname = staffArray[locate].surname
    self.staffRole = staffArray[locate].staffRole
    self.weeklyHours = staffArray[locate].weeklyHours
    self.payPerHour = staffArray[locate].payPerHour
    self.userName = staffArray[locate].userName
#manager task viewing function


  #manager timetable procedure
  def managerTimetable(self):
    #creates changes to the timetable
    def changes(count):
      #creatse the listbox for day selection
      def daySelect():
        #adds the changes to timetable
        def timetableChanges():
          #updates the timetable display
          def showEdits():
            nextButton2.pack_forget()
            daySelectionListbox.pack_forget()

            return
          daySelection=daySelectionListbox.get(daySelectionListbox.curselection())
          print(daySelection)


          if daySelection=="Monday":
            makeTimetable.item(timeSelection, values=(str(timeSelection[0]) +':00',staffChange,'','','',''))
            showEdits()
          elif daySelection=="Tuesday":
            makeTimetable.item(timeSelection, values=(str(timeSelection[0]) +':00','',staffChange,'','',''))
            showEdits()
          elif daySelection=="Wednesday":
            makeTimetable.item(timeSelection, values=(str(timeSelection[0]) +':00','','',staffChange,'',''))
            showEdits()
          elif daySelection=="Thursday":
            makeTimetable.item(timeSelection, values=(str(timeSelection[0]) +':00','','','',staffChange,''))
            showEdits()
          elif daySelection=="Friday":
            makeTimetable.item(timeSelection, values=(str(timeSelection[0]) +':00','','','','',staffChange))
            showEdits()



          #tree.item(selected_item, text="blub", values=("foo", "bar"))
          return
        staffChange=staffChangeMenu.get(staffChangeMenu.curselection())
        staffChangeMenu.pack_forget()
        nextButton.pack_forget()
        daySelectionListbox=Listbox(timetable)
        daySelectionListbox.insert(1,'Monday')
        daySelectionListbox.insert(2,'Tuesday')
        daySelectionListbox.insert(3,'Wednesday')
        daySelectionListbox.insert(4,'Thursday')
        daySelectionListbox.insert(5,'Friday')
        daySelectionListbox.pack()


        nextButton2=Button(timetable,text="Next",command=timetableChanges)
        nextButton2.pack()

        return

      timetableEditLabel.pack_forget()
      editButton.pack_forget()
      global timeSelection
      timeSelection=makeTimetable.selection()
      staffChangeMenu=Listbox(timetable)

      for x in range(0,len(staffNames)):
        staffChangeMenu.insert(END,staffNames[x])
      staffChangeMenu.pack()
      nextButton=Button(timetable,text="Next",command=daySelect)
      nextButton.pack()

      return
      #hides window when back button is pressed
    def hideWindow():
      timetable.withdraw()
      makeTimetable.pack_forget()
      editButton.destroy()
      backButton.destroy()
      timetableEditLabel.destroy()

      return
    global count

    # shows the timetable when the window is opened
    def timetableShow():
      timetable.deiconify()
      makeTimetable.pack()
      global backButton
      backButton = tkinter.Button(timetable, text="Go Back", command=hideWindow)
      backButton.pack()
      print("\n View Staff Timetable")
      global timetableEditLabel
      timetableEditLabel=tkinter.Label(timetable,text="Select a time to edit")
      timetableEditLabel.pack()
      global editButton
      editButton=Button(timetable,text="Edit",command=lambda:changes(count))
      editButton.pack()
      return






    if count==0:
      global timetable
      timetable = tkinter.Tk()
      timetable.title("Timetable")
      timetable.geometry('500x500')
      global makeTimetable
      makeTimetable=ttk.Treeview(timetable)
      makeTimetable['columns']=('Times','Monday','Tuesday','Wednesday','Thursday','Friday')

      makeTimetable.column("#0", width=0)
      makeTimetable.column("Times", width=80)
      makeTimetable.column("Monday", width=80)
      makeTimetable.column("Tuesday", width=80)
      makeTimetable.column("Wednesday", width=90)
      makeTimetable.column("Thursday", width=80)
      makeTimetable.column("Friday", width=80)

      makeTimetable.heading("#0", text='')

      makeTimetable.heading("Monday",text="Monday")
      makeTimetable.heading("Tuesday",text="Tuesday")
      makeTimetable.heading("Wednesday",text="Wednesday")
      makeTimetable.heading("Thursday",text="Thursday")
      makeTimetable.heading("Friday",text="Friday")
      count=count+1


      for hour in range(9,18):
        time=(hour,":00")
        makeTimetable.insert(parent='',index='end',iid=hour,text='',values=(time,'','','','',''))
      print("\n View Staff Timetable")
      timetableShow()
    else:
      timetableShow()
    return

  #manager task function
  def managerTasks(self):
    #creates the task entry box
    def taskCreate():
      #makes the task list changes
      def taskChanges():
        #updates the task list display
        def taskEdits():
            nextButton2.pack_forget()
            taskEditLabel.pack_forget()
            taskEntry.pack_forget()
            return
        taskList.item(staff, values=(staffNames[x], staffTask))
        taskEdits()
        return
      editButton.pack_forget()
      global staffSelection
      staffSelection = taskList.selection()
      taskEntryLabel = Label(taskUI, text="Enter the task name: ")
      taskEntryLabel.pack()
      taskEntry = Entry(taskUI, width=50)
      staffTask=taskEntry.get()
      taskEntry.pack()
      nextButton2 = Button(taskUI, text="Next", command=taskChanges)
      nextButton2.pack()




      return


    #hides window when back button is pressed
    def hideWindow():
      taskUI.withdraw()
      taskList.pack_forget()
      editButton.destroy()
      backButton.destroy()
      taskEditLabel.destroy()

      return


    #shows the task list when the window is opened
    def tasksShow():
      taskUI.deiconify()
      taskList.pack()
      global backButton
      backButton = tkinter.Button(taskUI, text="Go Back", command=hideWindow)
      backButton.pack()
      print("\n View Staff Timetable")
      global taskEditLabel
      taskEditLabel=tkinter.Label(taskUI,text="Select a time to edit")
      taskEditLabel.pack()
      global editButton
      editButton=Button(taskUI,text="Edit",command=taskCreate)
      editButton.pack()
      return





    global counter
    if counter==0:
      global taskUI
      taskUI = tkinter.Tk()
      taskUI.title("Task list")
      taskUI.geometry('500x500')
      global taskList
      taskList=ttk.Treeview(taskUI)
      taskList['columns']=('Staff','Task')

      taskList.column("#0", width=0)
      taskList.column("Staff", width=80)
      taskList.column("Task", width=80)

      taskList.heading("#0", text='')
      taskList.heading("Staff",text="Staff")
      taskList.heading("Task",text="Task")

      counter=counter+1


      for staff in range(0, len(staffNames)):
        taskList.insert(parent='',index='end',iid=staffNames[staff],text='',values=(staffNames[staff],''))

      tasksShow()
    else:
      tasksShow()
      return
    return




    #payslip function
  def payslip(self,staffCode):
      def openFile():
        filePath=filedialog.askopenfilename()
        file=open(filePath,"r")
        file.close()
      def download():
        file=open(name,"w")
        file.write("You worked " + str(self.weeklyHours) + " hours this week and your hourly rate is £" + str(self.payPerHour))
        file.write("\n You have been paid £" + str(totalPay) + " this week")
        file.write("\n You have been paid £"+str(monthlyPay) + " this month")
        file.close()
        return
      payslipUI=tkinter.Tk()
      payslipUI.geometry("500x500")
      payslipUI.title("Payslip")

      totalPay = int(self.weeklyHours) * int(self.payPerHour)
      monthlyPay=totalPay*4
      print("\n You have been paid ",monthlyPay)
      name=("payslip"+ str(self.firstName)+".txt")
      messagebox.showinfo(title="Paylslip", message="you have been paid "+ str(monthlyPay))
      payslipUI.deiconify()
      downloadButton=tkinter.Button(payslipUI, text="Download", command=download)
      openButton=tkinter.Button(payslipUI, text="Open", command=openFile)
      downloadButton.pack()
      openButton.pack()
      logoutButton = tkinter.Button(payslipUI, text="Logout", command=payslipUI.destroy,)
      logoutButton.pack()
      return

################################################################
  #manager area selction procedure
  def managerArea(self,staffCode):
    managerUI = tkinter.Tk()
    managerUI.title("Select a function")
    managerUI.geometry('500x500')
    logoutButton = tkinter.Button(managerUI, text="Logout", command=managerUI.destroy, height=5, width=10)
    logoutButton.grid(row=0, column=0)
    timetableButton= tkinter.Button(managerUI, text="View Timetable", command=lambda:self.managerTimetable(), height=5, width=10)
    timetableButton.grid(row=0, column=4 )
    taskButton= tkinter.Button(managerUI, text="View and Assign Tasks", command=lambda:self.managerTasks(), height=5, width=10)
    taskButton.grid(row=0, column=8 )
    payslipButton= tkinter.Button(managerUI, text="Get Payslip", command=lambda:self.payslip(staffCode), height=5, width=10)
    payslipButton.grid(row=0, column=2)

##########################################################################################################
    #provides the staff member creation a front end
def staffNumberEntry():

    #try:
      ###############################
      #clears the entry boxes for staff names
      def staffCreationClear():
        firstNameLabel.destroy()
        firstNameBox.destroy()
        surnameLabel.destroy()
        surnameBox.destroy()
        weeklyHoursLabel.destroy()
        weeklyHoursBox.destroy()
        payPerHourLabel.destroy()
        payPerHourBox.destroy()
        staffRoleLabel.destroy()
        roleList.destroy()
        submitButton.destroy()
        return
        #creates the staff class with the entry box data, then adds them to a database
      def staffSubmit():

          global submitNumber
          global staffName
          staffName=firstNameBox.get()
          tempName=firstNameBox.get().capitalize()
          tempTasks=[tempName]
          print(roleList.get(roleList.curselection()))

          tempName=StaffMember(submitNumber,firstNameBox.get(),surnameBox.get(),roleList.get(roleList.curselection()),weeklyHoursBox.get(),payPerHourBox.get())
          staffArray.append(tempName)
          staffNames.append(tempName.firstName)
          tasks.append(tempTasks)
          print(staffArray)
          print(len(staffArray))
          print(submitNumber)

          staffArray[submitNumber].getUserName()
          roles.append(tempName.staffRole.capitalize())
          print(tempName.userName)
          print(staffArray[submitNumber].userName)
          submitNumber=int(submitNumber+1)
          print(submitNumber)
          cursor.execute("INSERT INTO staffDatabase VALUES ('{}', '{}', '{}', '{}', '{}','{}','{}')".format(tempName.staffID,
                                                                                                          tempName.firstName,
                                                                                                          tempName.surname,
                                                                                                          tempName.staffRole,
                                                                                                          tempName.weeklyHours,
                                                                                                          tempName.payPerHour,
                                                                                                          tempName.userName))



          staffUserNames.append(tempName.userName)
          staffPasswords.append(tempName.staffID)
          connection.commit()

          cursor.execute("SELECT * FROM staffDatabase")
          print(cursor.fetchall())

          connection.commit()
          firstNameBox.delete(0, END)
          surnameBox.delete(0, END)
          weeklyHoursBox.delete(0, END)
          payPerHourBox.delete(0, END)
          roleList.selection_clear(0, END)

          if submitNumber==staffNumber:
            staffCreationClear()
            loginPacks()
          return
      def loginFrontEnd():
        userNameInput=userNameEntry.get()
        passwordInput=passwordEntry.get()
        if userNameInput not in staffUserNames or passwordInput not in staffPasswords:
          print("Incorrect username or password")

        else:
          if staffUserNames.index(userNameInput)==staffPasswords.index(passwordInput):
            print("Welcome")
            global staffCode
            staffCode=( passwordInput,)
            cursor.execute("SELECT firstName FROM staffDatabase WHERE staffID=?", staffCode)
            nameCheck=cursor.fetchall()
            nameCheck=nameCheck[0][0].capitalize()
            print("\n Welcome", nameCheck)
            cursor.execute("SELECT staffRole FROM staffDatabase WHERE staffID=?", staffCode)
            staffRole=cursor.fetchall()
            staffRole=staffRole[0][0]
            if staffRole=="Manager":
              global managerLogins
              managerLogins=0
              print(staffArray)
              global locate
              locate=staffNames.index(nameCheck)
              managers.append(nameCheck)
              idNum=int(staffCode[0])

              managers[idNum]=Manager(staffArray[locate].staffID,
                      staffArray[locate].firstName,
                      staffArray[locate].surname,
                      staffArray[locate].staffRole,
                      staffArray[locate].weeklyHours,
                      staffArray[locate].payPerHour,
                      staffArray[locate].userName)
              managers[idNum].managerArea(staffCode)
              managerLogins=managerLogins+1

            elif staffRole in roles:
              staffCode=staffCode[0]
              userLoggedIn=staffNames.index(nameCheck)
              staffArray[userLoggedIn].staffArea(staffCode)
            return

          else:
            print("Incorrect username or password")
        return
        #displays the login buttons and entries
      def loginPacks():
        loginLabel.pack()
        userNameLabel.pack()
        userNameEntry.pack()
        passwordLabel.pack()
        passwordEntry.pack()
        loginButton.pack()
        return

      staffNumber=int(staffNumberSpinbox.get())
      connection = sqlite3.connect(':memory:')
      #declaring a cursor to allow changes and serchs within the database
      cursor = connection.cursor()
      cursor.execute("""CREATE TABLE staffDatabase (
                  staffID text,
                  firstName text,
                  surname text,
                  staffRole text,
                  weeklyHours int,
                  payPerHour float,
                  userName text)""")

      #assign the class values, then adding them into a database
      staffEnterButton.pack_forget()
      staffNumberSpinbox.pack_forget()
      staffCreator.pack_forget()
      staffCreation=Label(root,text="Staff member creation")
      staffCreation.pack()

      #code for the login page
      firstNameLabel=Label(root,text="Enter the staff member's first name: ")
      firstNameBox=Entry(root,width=20)
      surnameLabel=Label(root,text="Enter the staff member's surname: ")
      surnameBox=Entry(root,width=20)
      staffRoleLabel=Label(root,text="Select the staff member's role: ")
      weeklyHoursLabel=Label(root,text="Enter the staff member's weekly hours: ")
      weeklyHoursBox=Entry(root,width=20)
      payPerHourLabel=Label(root,text="Enter the staff member's pay per hour: ")
      payPerHourBox=Entry(root,width=20)
      roleList=Listbox(root,height=len(staffRoles))
      for x in range(0,len(staffRoles)):
        roleList.insert(END,staffRoles[x])
      submitButton=Button(root,text="Submit",command=staffSubmit)
      global submitNumber
      submitNumber=0
      for staffIDLoop in range(0, staffNumber):
        print(submitNumber)
        firstNameBox.delete(0, END)
        surnameBox.delete(0, END)
        weeklyHoursBox.delete(0, END)
        payPerHourBox.delete(0, END)
        roleList.selection_clear(0, END)
        firstNameLabel.pack()
        firstNameBox.pack()
        surnameLabel.pack()
        surnameBox.pack()
        weeklyHoursLabel.pack()
        weeklyHoursBox.pack()
        payPerHourLabel.pack()
        payPerHourBox.pack()
        staffRoleLabel.pack()
        roleList.pack()
        submitButton.pack()
        loginLabel=Label(root,text="Login")
        userNameLabel=Label(root,text="Enter your username: ")
        userNameEntry=tkinter.Entry(root,width=20)
        passwordLabel=Label(root,text="Enter your password: ")
        passwordEntry=tkinter.Entry(root,width=20)
        loginButton=tkinter.Button(root,text="Login",command=loginFrontEnd)
        loginLabel.pack_forget()
        userNameLabel.pack_forget()
        userNameEntry.pack_forget()
        passwordLabel.pack_forget()
        passwordEntry.pack_forget()
        loginButton.pack_forget()


    #except:
     # print("Error, please try again")


#start of the object assignment
staffCreator=tkinter.Label(root,text="Select the number of staff members you want to create")
staffCreator.pack_forget()
staffNumberSpinbox=tkinter.Spinbox(root,from_=1,to=100,width=5)
staffNumberSpinbox.pack_forget()
staffEnterButton=tkinter.Button(root,text="Enter",command=staffNumberEntry)
staffEnterButton.pack_forget()






root.mainloop()

staffNumber=input("Enter the number of staff members you want to add: ")
while staffNumber.isdigit()==False:
  staffNumber=input("Enter the number of staff members you want to add: ")
staffNumber=int(staffNumber)
#array, list and tuple creation

########################################################
#setting a connection to memory to allow my dtabase to be stored








#connection.close()
#setting a connection to memory to allow my dtabase to be stored
connectionTimetable = sqlite3.connect('timetableData.db')
#declaring a cursor to allow changes and serchs within the database
cursorTimetable = connectionTimetable.cursor()

cursorTimetable.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='timetableData'")
exists = cursorTimetable.fetchall()
if not exists:
    cursorTimetable.execute("""CREATE TABLE timetableData (
                        day text,
                        time_0900 text,
                        time_1000 text,
                        time_1100 text,
                        time_1200 text,
                        time_1300 text,
                        time_1400 text,
                        time_1500 text,
                        time_1600 text,
                        time_1700 text)""")

timetable=[("","09:00","10:00","11:00","12:00","13:00","14:00","15:00","16:00","17:00"),
  ("Monday","","","","","","","","",""),
  ("Tuesday","","","","","","","","",""),
  ("Wednesday","","","","","","","","",""),
  ("Thurday","","","","","","","","",""),
  ("Friday","","","","","","","","","")]
#cursorTimetable.execute("INSERT INTO timetableData VALUES ('{}', '{}', '{}', '{}', '{}', '{}','{}','{}','{}','{}')")




















staffIdentity=[]



#login page
def login():
  userNameInput=input("\n Enter your username: ")
  passwordInput=input("\n Enter your password: ")

  while userNameInput not in staffUserNames or passwordInput not in staffPasswords:
    print("Incorrect username or password")
    userNameInput=input("\n Enter your username: ")
    passwordInput=input("\n Enter your password: ")
  global staffCode
  staffCode=( passwordInput,)
  cursor.execute("SELECT firstName FROM staffDatabase WHERE staffID=?", staffCode)
  nameCheck=cursor.fetchall()
  nameCheck=nameCheck[0][0].capitalize()
  print("\n Welcome", nameCheck)
  cursor.execute("SELECT staffRole FROM staffDatabase WHERE staffID=?", staffCode)
  staffRole=cursor.fetchall()
  staffRole=staffRole[0][0]
  if staffRole=="Manager":
    global managerLogins
    managerLogins=0
    print(staffArray)
    global locate
    locate=staffNames.index(nameCheck)
    managers.append(nameCheck)
    idNum=int(staffCode[0])

    managers[idNum]=Manager(staffArray[locate].staffID,
            staffArray[locate].firstName,
            staffArray[locate].surname,
            staffArray[locate].staffRole,
            staffArray[locate].weeklyHours,
            staffArray[locate].payPerHour,
            staffArray[locate].userName)
    managers[idNum].managerArea(staffCode)
    managerLogins=managerLogins+1

  elif staffRole in roles:
    staffCode=staffCode[0]
    userLoggedIn=staffNames.index(nameCheck)
    staffArray[userLoggedIn].staffArea(staffCode)
  return


###################################################################

#main running of code 

#login()

##################################################################
#front end

