import sqlite3
import tkinter
from tkinter import Checkbutton, IntVar, messagebox
from tkinter import ttk



class StaffMember():
  def __init__(self, staffID, firstName, surname, dob, staffRole, weeklyHours, payPerHour):
      self.firstName = str(input("Enter the staff's first name: "))
      self.firstName = self.firstName.capitalize()
      self.surname = input("Enter the staff's surname: ")
      self.surname = self.surname.capitalize()
      self.staffID = input("Enter the staff's ID number: ")
      self.staffRole = input("Enter the staff's role: ")
      self.weeklyHours = input("Enter the staff's weekly hours: ")
      self.payPerHour = input("Enter the staff's hourly pay: ")

  
  def getUserName(self):
    self.userName= self.firstName.capitalize()+"."+self.surname.capitalize()
    return



#start of the object assignment
staffNumber=int(input("Enter the number of staff members you want to add: "))
#array, list and tuple creation
staffArray=[]
staffUserNames=[]
staffPasswords=[]
tasks=[]
roles=[]
########################################################
#setting a connection to memory to allow my dtabase to be stored
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
for i in range(0, staffNumber):
  tempName=input("Enter the name of the staff member you want to create: ")
  tempTasks=[tempName.capitalize()]
  tempName=StaffMember('','','','','','','')
  staffArray.append(tempName)
  tasks.append(tempTasks)
  staffArray[i].getUserName()
  roles.append(tempName.staffRole.capitalize())
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


##############################################################
#staff timetable viewer
def staffTimetableProcedure():
  print("View Staff Timetable")
  print(timetable)
  back=input("\n Press the enter key to return to the menu: ")
  return

  #staff task viewer
def checkTasks(staffCode):
  cursor.execute("SELECT firstName FROM staffDatabase WHERE staffID=?", staffCode)
  staffLoggedIn=cursor.fetchall()
  print(staffLoggedIn)
  staffLoggedIn=staffLoggedIn[0][0]
  print(staffLoggedIn)
  for x in range(0,len(tasks)):
    if tasks[x][0]==staffLoggedIn:
      print (tasks[x])
      back=input("\n Press the enter key to return to the menu: ")
  return

##############################################################
def managerTable():
  edit=int(input("\n Enter 1 to edit timetable: "))
  if edit==1:
    managerTimetable()

    repeat=int(input("\n Enter 1 to edit another day on the timetable \n Enter 2 to go back: "))
    while repeat ==1:
      managerTimetable()
      repeat=int(input("\n Enter 1 to edit another day on the timetable \n Enter 2 to go back: "))
    print(timetable)
  else:
    print(timetable)
  back=input("\n Press the enter key to return to the menu: ")
  
  return 




def managerTasks():
  edit=int(input("\n Enter 1 to assign tasks: "))
  if edit==1:
    taskAssignment()

    repeat=int(input("\n Enter 1 to assign another task \n Enter 2 to go back: "))
    while repeat ==1:
      taskAssignment()
      repeat=int(input("\n Enter 1 to assign another task \n Enter 2 to go back: "))
  else:
    print(tasks)
  back=input("\n Press the enter key to return to the menu: ")
  
  return 
#manager timetable procedure
def managerTimetable():
  print("\n View Staff Timetable")
  print(timetable)
  #code a database
  daySelection=int(input("\n Enter the day you want to edit, \n 1:Monday \n 2:Tuesday \n 3:Wednesday \n 4:Thursday \n 5:Friday \n:"))
  timeSelection=int(input("\n Enter the time you want to edit,\n 9,\n 10,\n 11,\n 12,\n 13,\n 14,\n 15,\n 16,\n 17: "))
  timeSelection=timeSelection-8
  tableChange=input("\n Enter the staff member working this time: ")
  timetable[daySelection] = timetable[daySelection][:timeSelection] + (tableChange,) + timetable[daySelection][timeSelection+1:]
  print (timetable)
  return
#manager task function
def taskAssignment():
  print("\n View Staff Tasks")
  print(tasks)
  
  staffSelection=input("\n Enter the staff member you want to view tasks for: ")
  taskGive=input("\n Enter the task you want to give the staff member: ")
  for x in range(0,len(tasks)):
    if staffSelection.capitalize()==tasks[x][0]:
      tasks[x].append(taskGive)
      print(tasks)
  return
  



  

#payslip function
def payslip(staffCode):
  print("View Staff Payslip")
  cursor.execute("SELECT weeklyHours FROM staffDatabase WHERE staffID=?",staffCode)
  weeklyHours=cursor.fetchall()
  weeklyHours=weeklyHours[0][0]
  weeklyHours=float(weeklyHours)
  cursor.execute("SELECT payPerHour FROM staffDatabase WHERE staffID=?",staffCode,)
  payPerHour=cursor.fetchall()
  payPerHour=payPerHour[0][0]
  totalPay=weeklyHours*payPerHour
  totalPay=totalPay
  monthlyPay=totalPay*4
  print("\n You have been paid ",monthlyPay)
  cursor.execute("SELECT firstName FROM staffDatabase WHERE staffID=?",staffCode)
  name=cursor.fetchall()
  name=name[0][0]
  file=int(input("\n Enter 1 to download your payslip: "))
  name=("payslip"+name+".txt")
  if file==1:
    file=open(name,"w")
    file.write("You worked " + str(weeklyHours) + " hours this week and your hourly rate is £" + str(payPerHour))
    file.write("\n You have been paid £" + str(totalPay) + " this week")
    file.write("\n You have been paid £"+str(monthlyPay) + " this month")
    file.close()
  return 








################################################################
#manager area selction procedure
def managerArea(staffCode):
  areaSelection=int(input("\n Enter the number of the area you want to view: \n 1: Edit Timetable \n 2: Assign Tasks \n 3: View Payslip \n 4: Logout \n :"))

  if areaSelection==1:
    print("\n Edit timetable")
    managerTable()
  elif areaSelection==2:
    print("\n Assign Tasks")
    managerTasks()
  elif areaSelection==3:
    print("\n View Payslip")
    payslip(staffCode)
  elif areaSelection==4:
    print("\n Logout")
    login()
  managerArea(staffCode)
  return staffCode
###############################################################
#staff area selection procedure
def staffArea(staffCode):
  areaSelection=int(input("\n Enter the number of the area you want to view: \n 1: View Timetable \n 2: View Tasks \n 3: View Payslip \n 4: Logout \n : "))

  if areaSelection==1:
    print("\n View timetable")
    staffTimetableProcedure()
  elif areaSelection==2:
    print("\n View Tasks")
    checkTasks(staffCode)
  elif areaSelection==3:
    print("\n View Payslip")
    payslip(staffCode)
  elif areaSelection==4:
    print("\n Logout")
    login()
  staffArea(staffCode)
  return
###############################################################
#login page
def login():
  userNameInput=input("\n Enter your username: ")
  passwordInput=input("\n Enter your password: ")

  while userNameInput not in staffUserNames or passwordInput not in staffPasswords:
    print("Incorrect username or password")
    userNameInput=input("\n Enter your username: ")
    passwordInput=input("\n Enter your password: ")

  staffCode=( passwordInput,)
  cursor.execute("SELECT firstName FROM staffDatabase WHERE staffID=?", staffCode)
  print("\n Welcome", cursor.fetchall())
  cursor.execute("SELECT staffRole FROM staffDatabase WHERE staffID=?", staffCode)
  staffRole=cursor.fetchall()
  staffRole=staffRole[0][0].capitalize()
  if staffRole=="Manager":
    managerArea(staffCode)
  elif staffRole in roles:
    staffArea(staffCode)
  return


###################################################################
#main running of code
login()
  
###################################################################
