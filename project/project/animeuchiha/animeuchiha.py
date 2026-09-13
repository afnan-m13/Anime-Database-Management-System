from ast import Str
import mysql.connector

def DB_connection():
  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database='animeuchiha'
    )
  return mydb

mydb = DB_connection()


def menu():
  print("\n\nPlease select a task to do:")
  print("1- Add a new department") 
  print("2- Show all department")
  print("3- Remove a department")
  print("4- Search for a department")
  
  print("5- Add a new anime project")
  print("6- Show all anime project")
  print("7- Remove a anime project")
  print("8- Search for a anime project")
  
  print("9- Add a new staff member")
  print("10- Show allstaff member")
  print("11- Remove a staff member")
  print("12- Search for a staff member")
  
  print("13- Add a new staff member (Voice Actor)")
  print("14- Show allstaff member (Voice Actor)")
  print("15- Remove a staff member (Voice Actor)")
  print("16- Search for a staff member (Voice Actor)")
  
  print("17- Add a new staff member (Animation)")
  print("18- Show allstaff member (Animation)")
  print("19- Remove a staff member (Animation)")
  print("20- Search for a staff member (Animation)")

  print("21- Add a new staff member (Production Helpers)")
  print("22- Show allstaff member (Production Helpers)")
  print("23- Remove a staff member (Production Helpers)")
  print("24- Search for a staff member (Production Helpers)")
  
  print("25- Add a new episode")
  print("26- Remove a episode")
  print("27- Search for a episode")

  print("28- Add a new task")
  print("29- Show all tasks")
  print("30- Remove a new task")
  print("31- Search for a task")
  
  
  print("32- Add a new contract")
  print("33- Show all contract")
  print("34- Remove a new contract")
  print("35- Search for a contract")
  
  print("36- Add viewer")
  print("37- Show Viewers")
  print("38- Remove a Viewers")
  print("39- Search for a viewer")

  print("40- Exit")


def addDepartment():
    print("Please enter the new department details below")
    Dname = input("Department Name: ")
    Dgenres= input ("Department genres: ")
    Doffice= input("Ddepartment office Details: ")
    DID = input("Department ID: ")
    SID = input ("The Person who manage the departmen: ")
    sqlInsert = "INSERT INTO department VALUES(%s,%s,%s,%s,%s)"
    val = (Dname,Dgenres,Doffice,DID ,SID)
    mycursor = mydb.cursor()
    mycursor.execute(sqlInsert, val)
    mydb.commit()
    print("Department added successfully")
    
def allDepartments():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM department")
    myresult = mycursor.fetchall()
    print('Department ID' + '\t\t' + 'Department Name' + '\t\t' + 'Office Details' + '\t\t' + 'Department Genres' + '\t' + 'Department manage')
    print('-------------' + '\t\t' + '-------------' + '\t\t' + '-------------' + '\t\t' + '----------------' + '\t' + '-------------')
    for x in myresult:
        print(str(x[0]) + '\t\t\t' + x[1] + '\t\t\t' + str(x[2]) + '\t\t\t' + str(x[3]) + '\t\t\t' + str(x[4]))
        
def delDepartment():
  mid = input("Please enter the department ID: ")
  sqlsearch = "SELECT * FROM department WHERE DID = \'" + mid + "\'"
  mycursor = mydb.cursor()
  mycursor.execute(sqlsearch)
  myresult = mycursor.fetchall()
  if (mycursor.rowcount <= 0):
    print("There is no department with this ID.")
  else:
    sqldelete = "DELETE FROM department WHERE DID = \'" + mid + "\'"
    mycursor = mydb.cursor()
    mycursor.execute(sqldelete)
    mydb.commit()
    print("Deleted successfully")
    
def findDepartment():
  mid = input("Please enter the Department ID: ")
  sqlsearch = "SELECT * FROM department WHERE DID = \'" + mid + "\'"
  mycursor = mydb.cursor()
  mycursor.execute(sqlsearch)
  myresult = mycursor.fetchone()
  print(mycursor.rowcount)
  if (mycursor.rowcount <= 0):
    print("There is no Department with this ID.")
  else:
    print("The details of the Department are: ")
    print("Department Name: " + myresult[0])
    print("Department ID: " + str(myresult[3]))
    print("Department genres: " + myresult[1])
    print("Department manager: " + str(myresult[4]))
    print("Ddepartment office Details: " + myresult[2])
  




def addAnimeProject():
    print("Please enter the new anime projec details below")
    Atitle = input("Project Title: ")
    Acode = input("Project Code: ")
    Agenres = input("Project Genre: ")
    Adirector = input("Project Director: ")
    Adescription = input("Project Description: ")
    writerDesc = input("Project Scriptwriter: ")
    ADID = input("Department ID: ")
    sqlInsert = "INSERT INTO anime_projects VALUES(%s,%s,%s,%s,%s,%s,%s)"
    val = (Atitle,Agenres,Adirector, Adescription,writerDesc, ADID, Acode )
    mycursor = mydb.cursor()
    mycursor.execute(sqlInsert, val)
    mydb.commit()
    print("Anime project added successfully")

def allAnimeProjects():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM anime_projects")
    myresult = mycursor.fetchall()
    print('Project Code' + '\t\t' + 'Project Name' + '\t\t' + 'Project Genre' + '\t\t' + 'Scriptwriter' + '\t\t' + 'Director' + '\t\t' + 'Description' +  '\t\t' + 'Department number')
    print('-----------' + '\t\t' + '------------' + '\t\t' + '-------------' + '\t\t'  + '------------' + '\t\t' + '--------' + '\t\t' + '------------' + '\t\t' + '----------------' )
    for x in myresult:
        x3 = x[3] if(x[3]) else 'Unknown'
        print(str(x[6]) + '\t\t\t' + x[0] + '\t\t\t' + x[1] + '\t\t\t' + x[4] + '\t\t\t' + x[2] + '\t\t\t' + x[3] + '\t\t\t'+ str(x[5]) )

def delAnimeProject():
  mid = input("Please enter the Anime Project Code: ")
  sqlsearch = "SELECT * FROM anime_projects WHERE Acode = \'" + mid + "\'"
  mycursor = mydb.cursor()
  mycursor.execute(sqlsearch)
  myresult = mycursor.fetchall()
  if (mycursor.rowcount <= 0):
    print("There is no Anime Project with this Code.")
  else:
    sqldelete = "DELETE FROM anime_projects WHERE  Acode = \'" + mid + "\'"
    mycursor = mydb.cursor()
    mycursor.execute(sqldelete)
    mydb.commit()
    print("Deleted successfully")

def findAnimeProject():
  mid = input("Please enter the Anime Project ID: ")
  sqlsearch = "SELECT * FROM anime_projects WHERE Acode = \'" + mid + "\'"
  mycursor = mydb.cursor()
  mycursor.execute(sqlsearch)
  myresult = mycursor.fetchone()
  print(mycursor.rowcount)
  if (mycursor.rowcount <= 0):
    print("There is no Anime Project with this Code.")
  else:
    print("The details of the Anime Project are: ")
    print("Project Title: " + myresult[0])
    print("Project Code: " + str(myresult[5]))
    print("Project Genre: " + myresult[1])
    print("Project Director: " + myresult[2])
    print("Project Scriptwriter: " + myresult[4])
    print("Project Description: " + myresult[3])
    print("Department Number: " + str(myresult[6]))





def addStaffmember():
    SID = input("Staff Memeber ID: ")
    Fname = input("First Name: ")
    Lname = input("Last Name: ")
    S_job= input("Job Title: ")
    De_DID = input ("Department Number: ")
    sqlInsert = "INSERT INTO stuffmembers VALUES(%s,%s,%s,%s,%s)"
    val = (S_job,Fname,Lname,SID , De_DID)
    mycursor = mydb.cursor()
    mycursor.execute(sqlInsert, val)
    mydb.commit()
    print("Staff Member added successfully")
    
def allStaffmember():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM stuffmembers")
    myresult = mycursor.fetchall()
    print('Staff ID' + '\t\t' + 'First Name' + '\t\t' + 'Last Name' + '\t\t' + 'Job Title' + '\t\t' + 'Department Number')
    print('--------' + '\t\t' + '----------' + '\t\t' + '---------' + '\t\t' + '----------' + '\t\t' + '---------------' )
    for x in myresult:
        print(str(x[3]) + '\t\t\t' + str(x[1]) + '\t\t\t' + str(x[2]) + '\t\t\t' +str( x[0]) + '\t\t\t' + str( x[4]))
        
def delStaffmember():
  mid = input("Please enter the the Staff Memeber ID: ")
  sqlsearch = "SELECT * FROM stuffmembers WHERE SID = \'" + mid + "\'"
  mycursor = mydb.cursor()
  mycursor.execute(sqlsearch)
  myresult = mycursor.fetchall()
  if (mycursor.rowcount <= 0):
    print("There is no Staff Memeber with this ID.")
  else:
    sqldelete = "DELETE FROM stuffmembers WHERE SID = \'" + mid + "\'"
    mycursor = mydb.cursor()
    mycursor.execute(sqldelete)
    mydb.commit()
    print("Deleted successfully")
    
def findStaffmember():
  mid = input("Please enter the Staff Memeber ID: ")
  sqlsearch = "SELECT * FROM stuffmembers WHERE SID = \'" + mid + "\'"
  mycursor = mydb.cursor()
  mycursor.execute(sqlsearch)
  myresult = mycursor.fetchone()
  print(mycursor.rowcount)
  if (mycursor.rowcount <= 0):
    print("There is no Staff Memeber with this ID.")
  else:
    print("The details of the Staff Memeber are: ")
    print("Staff Memeber ID: " + str(myresult[3]))
    print("First Name: " + str(myresult[1]))
    print("Last Name: " + str(myresult[2]))
    print("Job Title: " + str(myresult[0]))
    print("Department Number: " + str(myresult[4]))
    




def addStaffVoiceActor():
    SID = input("Staff Memeber ID: ") 
    Fname = input("First Name: ")
    Lname = input("Last Name: ")
    S_job= input("Job Title: ")
    De_DID = input ("Department Number: ")
    sqlInsert = "INSERT INTO stuffmembers VALUES(%s,%s,%s,%s,%s)"
    val = (S_job,Fname,Lname,SID , De_DID)
    mycursor = mydb.cursor()
    mycursor.execute(sqlInsert, val)
    mydb.commit()
  
    SID = SID
    roles = input ("Prominent Roles: ")
    Vdate = input("Start Date: ")
    Vrange = input ("Voice Range: ")
    sqlInsert = "INSERT INTO voiceactor VALUES(%s,%s,%s,%s)"
    val = (SID,roles,Vdate ,Vrange)
    mycursor = mydb.cursor()
    mycursor.execute(sqlInsert, val)
    mydb.commit()
    print("Voice Actor added successfully.")

def allStaffVoiceActor():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM VoiceActor")
    myresult = mycursor.fetchall()
    print('Staff ID' + '\t\t' + 'Prominent Roles' + '\t\t\t' + 'Start Date' + '\t\t\t' + 'Voice Range')
    print('--------' + '\t\t' + '---------------' + '\t\t\t' + '---------' + '\t\t\t' + '-----------' )
    for x in myresult:
        print(str(x[0]) + '\t\t\t' + x[1] + '\t\t\t\t' +str(x[2]) + '\t\t\t\t' + x[3] )
      
def delStaffVoiceActor():
  mid = input("Please enter the Staff Voice Actor ID: ")
  sqlsearch = "SELECT * FROM VoiceActor WHERE  SID = \'" + mid + "\'"
  mycursor = mydb.cursor()
  mycursor.execute(sqlsearch)
  myresult = mycursor.fetchall()
  if (mycursor.rowcount <= 0):
    print("There is no Voice Actor with this ID.")
  else:
    sqldelete = "DELETE FROM VoiceActor WHERE SID = \'" + mid + "\'"
    mycursor = mydb.cursor()
    mycursor.execute(sqldelete)
    mydb.commit()
    sqldelete = "DELETE FROM stuffmembers WHERE SID = \'" + mid + "\'"
    mycursor = mydb.cursor()
    mycursor.execute(sqldelete)
    mydb.commit()
    print("Deleted successfully.")

def findStaffVoiceActor():
  mid = input("Please enter the Staff Voice Actor ID: ")
  sqlsearch = "SELECT * FROM VoiceActor WHERE SID = \'" + mid + "\'"
  mycursor = mydb.cursor()
  mycursor.execute(sqlsearch)
  myresult = mycursor.fetchone()
  print(mycursor.rowcount)
  if (mycursor.rowcount <= 0):
    print("There is no Staff Voice Actor with this ID.")
  else:
    print("The details of the Staff Voice Actor are: ")
    print("Stsff Memeber ID: " + str(myresult[0]))
    print("Prominent Roles: " + myresult[1])
    print("Start Date: " +str(myresult[2]))
    print("Voice Range: " + myresult[3])
   





def addStaffAnimation():
    SID = input("Staff Memeber ID: ") 
    Fname = input("First Name: ")
    Lname = input("Last Name: ")
    S_job= input("Job Title: ")
    De_DID = input ("Department Number: ")
    sqlInsert = "INSERT INTO stuffmembers VALUES(%s,%s,%s,%s,%s)"
    val = (S_job,Fname,Lname,SID , De_DID)
    mycursor = mydb.cursor()
    mycursor.execute(sqlInsert, val)
    mydb.commit()
    
    SID = SID
    astyle = input ("Animation Style: ")
    Date_joined = input("Date Joined: ")
    Notableworks= input ("Notable Works: ")
    sqlInsert = "INSERT INTO animation VALUES(%s,%s,%s,%s)"
    val = (SID,astyle,Notableworks ,Date_joined)
    mycursor = mydb.cursor()
    mycursor.execute(sqlInsert, val)
    mydb.commit()
    print("Animation added successfully.")
    
def allStaffAnimation():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM animation")
    myresult = mycursor.fetchall()
    print('Staff ID' + '\t\t' +  'Animation Style' + '\t\t' + 'Notable Works' + '\t\t' + 'Date Joined')
    print('--------' + '\t\t' + '--------------' + '\t\t' + '-------------' + '\t\t' + '-----------' )
    for x in myresult:
        print(str(x[0]) + '\t\t\t' + x[1] + '\t\t\t' + x[2] + '\t\t\t' + str(x[3]) )
        
def delStaffAnimation():
  mid = input("Please enter the Animation ID: ")
  sqlsearch = "SELECT * FROM animation WHERE SID = \'" + mid + "\'"
  mycursor = mydb.cursor()
  mycursor.execute(sqlsearch)
  myresult = mycursor.fetchall()
  if (mycursor.rowcount <= 0):
    print("There is no Animation with this ID.")
  else:
    sqldelete = "DELETE FROM animation WHERE SID = \'" + mid + "\'"
    mycursor = mydb.cursor()
    mycursor.execute(sqldelete)
    mydb.commit()
    sqldelete = "DELETE FROM stuffmembers WHERE SID = \'" + mid + "\'"
    mycursor = mydb.cursor()
    mycursor.execute(sqldelete)
    mydb.commit()
    print("Deleted successfully.")
      
def findStaffAnimation():
  mid = input("Please enter the Staff Animation ID: ")
  sqlsearch = "SELECT * FROM animation WHERE SID = \'" + mid + "\'"
  mycursor = mydb.cursor()
  mycursor.execute(sqlsearch)
  myresult = mycursor.fetchone()
  print(mycursor.rowcount)
  if (mycursor.rowcount <= 0):
    print("There is no  Animation with this ID.")
  else:
    print("The details of the  Animation are: ")
    print("Stsff Memeber ID: " + str(myresult[0]))
    print("Animation Style: " + myresult[1])
    print("Date Joined: " + str(myresult[3]))
    print("Notable Works: " + myresult[2])
    






def addStaffProduction():
    SID = input("Staff Memeber ID: ") 
    Fname = input("First Name: ")
    Lname = input("Last Name: ")
    S_job= input("Job Title: ")
    De_DID = input ("Department Number: ")
    sqlInsert = "INSERT INTO stuffmembers VALUES(%s,%s,%s,%s,%s)"
    val = (S_job,Fname,Lname,SID , De_DID)
    mycursor = mydb.cursor()
    mycursor.execute(sqlInsert, val)
    mydb.commit()
    
    SID = SID
    responisibility = input ("Responsibilty: ")
    specific_roles= input ("Specific Roles: ")
    sqlInsert = "INSERT INTO production_helpers VALUES(%s,%s,%s)"
    val = (SID,responisibility,specific_roles )
    mycursor = mydb.cursor()
    mycursor.execute(sqlInsert, val)
    mydb.commit()
    print("Production Helpers added successfully.")
    
def allStaffProduction():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM production_helpers")
    myresult = mycursor.fetchall()
    print('Staff ID' + '\t\t' + 'Responsibilty' + '\t\t' + 'Specific Roles' )
    print('--------' + '\t\t' + '-------------' + '\t\t' + '--------------'  )
    for x in myresult:
        print(str(x[0]) + '\t\t\t' + x[1] + '\t\t\t' + x[2] )
        
def delStaffProduction():
  mid = input("Please enter the Staff Production ID: ")
  sqlsearch = "SELECT * FROM production_helpers WHERE SID = \'" + mid + "\'"
  mycursor = mydb.cursor()
  mycursor.execute(sqlsearch)
  myresult = mycursor.fetchall()
  if (mycursor.rowcount <= 0):
    print("There is no Staff Production with this ID.")
  else:
    sqldelete = "DELETE FROM production_helpers WHERE SID = \'" + mid + "\'"
    mycursor = mydb.cursor()
    mycursor.execute(sqldelete)
    mydb.commit()
    sqldelete = "DELETE FROM stuffmembers WHERE SID = \'" + mid + "\'"
    mycursor = mydb.cursor()
    mycursor.execute(sqldelete)
    mydb.commit()
    print("Deleted successfully.") 
    
def findStaffProduction():
  mid = input("Please enter the Staff Production ID: ")
  sqlsearch = "SELECT * FROM production_helpers WHERE SID = \'" + mid + "\'"
  mycursor = mydb.cursor()
  mycursor.execute(sqlsearch)
  myresult = mycursor.fetchone()
  print(mycursor.rowcount)
  if (mycursor.rowcount <= 0):
    print("There is no Staff Production with this ID.")
  else:
    print("The details of the Staff Production are: ")
    print("Stsff Memeber ID: " + str(myresult[0]))
    print("Responsibilty: " + myresult[1])
    print("Specific Roles: " + myresult[2])
    




def addEpisode():
    Enumber = input("Episode Number: ")
    Etitle = input("Episode Title: ")
    ESummery = input("Episode Summary: ")
    AirDate = input("Episode Air Date (YYYY-MM-DD): ")
    Acode = input("Project code: ")
    sqlInsert = "INSERT INTO episodes VALUES(%s,%s,%s,%s,%s)"
    val = (Acode,ESummery,Etitle,AirDate,Enumber)
    mycursor = mydb.cursor()
    mycursor.execute(sqlInsert, val)
    mydb.commit()
    print("Episode added successfully.")

def delEpisode():
  mid = input("Please enter the Episode Enumber: ")
  sqlsearch = "SELECT * FROM episodes WHERE  Enumber = \'" + mid + "\'"
  mycursor = mydb.cursor()
  mycursor.execute(sqlsearch)
  myresult = mycursor.fetchall()
  if (mycursor.rowcount <= 0):
    print("There is no Episode with this Enumber.")
  else:
    sqldelete = "DELETE FROM episodes WHERE  Enumber= \'" + mid + "\'"
    mycursor = mydb.cursor()
    mycursor.execute(sqldelete)
    mydb.commit()
    print("Deleted successfully.") 
    
def findEpisode():
  mid = input("Please enter the Episode number: ")
  sqlsearch = "SELECT * FROM episodes WHERE Enumber = \'" + mid + "\'"
  mycursor = mydb.cursor()
  mycursor.execute(sqlsearch)
  myresult = mycursor.fetchone()
  print(mycursor.rowcount)
  if (mycursor.rowcount <= 0):
    print("There is no Episode with this number.")
  else:
    print("The details of the Episode are: ")
    print("Episode Number: " + str(myresult[4]))
    print("Episode Title: " + myresult[2])
    print("Episode Summary: " + myresult[1])
    print("Episode Air Date (YYYY-MM-DD): " + str(myresult[3]))
    print("Project Code: " + str(myresult[0]))





def addTask():
    TID = input("Task ID: ")
    Title = input("Task Title: ")
    Task_desc = input("Task Description: ")
    s_date = input("Task Start Date (YYYY-MM-DD): ")
    e_date = input("Task End Date (YYYY-MM-DD): ")
    Enumber =input("Episode number: ")
    sqlInsert = "INSERT INTO atasks VALUES(%s,%s,%s,%s,%s,%s)"
    val = (Title,s_date,e_date ,Task_desc,TID,Enumber)
    mycursor = mydb.cursor()
    mycursor.execute(sqlInsert, val)
    mydb.commit()
    print("Task added successfully.")
    
def allTask():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM atasks")
    myresult = mycursor.fetchall()
    print( 'Task ID' + '\t\t\t' + 'Task Title' + '\t\t' + 'Task Start Date' + '\t\t' + 'Task End Date' + '\t\t' + 'Task Description' + '\t\t' + 'Episode number' )
    print('--------' + '\t\t' + '----------' + '\t\t' + '--------------'  + '\t\t' + '--------------' + '\t\t' + '----------------' + '\t\t' + '--------------'  )
    for x in myresult:
        print(str(x[4]) + '\t\t\t' + x[0] + '\t\t\t' + str(x[1]) + '\t\t\t' + str(x[2]) + '\t\t\t' + x[3] + '\t\t\t\t' + str(x[5]) )

def delTask():
  mid = input("Please Enter The Task ID: ")
  sqlsearch = "SELECT * FROM atasks WHERE TID = \'" + mid + "\'"
  mycursor = mydb.cursor()
  mycursor.execute(sqlsearch)
  myresult = mycursor.fetchall()
  if (mycursor.rowcount <= 0):
    print("There is no Viewers with this id.")
  else:
    sqldelete = "DELETE FROM atasks WHERE TID = \'" + mid + "\'"
    mycursor = mydb.cursor()
    mycursor.execute(sqldelete)
    mydb.commit()
    print("Deleted successfully.") 

def findTask():
  mid = input("Please enter the Task ID: ")
  sqlsearch = "SELECT * FROM atasks WHERE TID = \'" + mid + "\'"
  mycursor = mydb.cursor()
  mycursor.execute(sqlsearch)
  myresult = mycursor.fetchone()
  print(mycursor.rowcount)
  if (mycursor.rowcount <= 0):
    print("There is no Task with this ID.")
  else:
    print("The details of the Task are: ")
    print("Task ID: " + str(myresult[4]))
    print("Task Title: " + myresult[0])
    print("Task Description: " + myresult[3])
    print("Task Start Date (YYYY-MM-DD): " + str(myresult[1]))
    print("Task End Date (YYYY-MM-DD): " + str(myresult[2]))
    print("Episode Number: " + str(myresult[5]))
    




def addContract():
    CID = input("Contract ID: ")
    Sdate = input("Contract Start Date (YYYY-MM-DD): ")
    Edate = input("Contract End Date (YYYY-MM-DD): ")
    payment = input("Contract Payment Info: ")
    sqlInsert = "INSERT INTO contract VALUES(%s,%s,%s,%s)"
    val = (Sdate,Edate ,payment ,CID)
    mycursor = mydb.cursor()
    mycursor.execute(sqlInsert, val)
    mydb.commit()
    print("Contract added successfully.")

def allContract():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM contract")
    myresult = mycursor.fetchall()
    print( 'Contract ID' + '\t\t' + 'Contract Start Date' + '\t\t' + 'Contract End Date' + '\t\t' + 'Contract Payment Info'  )
    print( '-----------' + '\t\t' + '-------------------' + '\t\t' + '-----------------'  + '\t\t' + '--------------------'  )
    for x in myresult:
        print(str(x[3]) +  '\t\t\t' + str(x[0]) + '\t\t\t' + str(x[1]) + '\t\t\t\t' + x[2] )
    
def delContrac():
  mid = input("Please Enter The Contrac ID: ")
  sqlsearch = "SELECT * FROM contract WHERE CID = \'" + mid + "\'"
  mycursor = mydb.cursor()
  mycursor.execute(sqlsearch)
  myresult = mycursor.fetchall()
  if (mycursor.rowcount <= 0):
    print("There is no contract with this id.")
  else:
    sqldelete = "DELETE FROM contract WHERE CID = \'" + mid + "\'"
    mycursor = mydb.cursor()
    mycursor.execute(sqldelete)
    mydb.commit()
    print("Deleted successfully.") 

def findContract():
  mid = input("Please enter the Contract ID: ")
  sqlsearch = "SELECT * FROM contract WHERE CID = \'" + mid + "\'"
  mycursor = mydb.cursor()
  mycursor.execute(sqlsearch)
  myresult = mycursor.fetchone()
  print(mycursor.rowcount)
  if (mycursor.rowcount <= 0):
    print("There is no Contract with this ID.")
  else:
    print("The details of the Contract are: ")
    print("Contract ID: " + str(myresult[3]))
    print("Contract Start Date (YYYY-MM-DD): " +str( myresult[0]))
    print("Contract End Date (YYYY-MM-DD): " + str(myresult[1]))
    print("Contract Payment Info: " + myresult[2])







def addViewers():
    VID = input("Viewers ID: ")
    rate = input("Viewers Rate: ")
    sqlInsert = "INSERT INTO viewers VALUES(%s,%s)"
    val = (rate,VID)
    mycursor = mydb.cursor()
    mycursor.execute(sqlInsert, val)
    mydb.commit()
    print("Viewers added successfully")

def allViewers():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM viewers")
    myresult = mycursor.fetchall()
    print('Viewers ID' + '\t\t' + 'Viewers Rate')
    print('----------' + '\t\t' + '------------')
    for x in myresult:
        print(str(x[1]) + '\t\t\t' + x[0])

def delViewers():
  mid = input("Please Enter The Viewers ID: ")
  sqlsearch = "SELECT * FROM viewers WHERE VID = \'" + mid + "\'"
  mycursor = mydb.cursor()
  mycursor.execute(sqlsearch)
  myresult = mycursor.fetchall()
  if (mycursor.rowcount <= 0):
    print("There is no Viewers with this id.")
  else:
    sqldelete = "DELETE FROM viewers WHERE VID = \'" + mid + "\'"
    mycursor = mydb.cursor()
    mycursor.execute(sqldelete)
    mydb.commit()
    print("Deleted successfully.") 
    
def findViewers():
  mid = input("Please enter the Viewers ID: ")
  sqlsearch = "SELECT * FROM viewers WHERE VID = \'" + mid + "\'"
  mycursor = mydb.cursor()
  mycursor.execute(sqlsearch)
  myresult = mycursor.fetchone()
  print(mycursor.rowcount)
  if (mycursor.rowcount <= 0):
    print("There is no Viewers with this ID.")
  else:
    print("The details of the Viewers are: ")
    print("Viewers ID: " + str(myresult[1]))
    print("Viewers Rate: " + myresult[0])
    





def main():
  key = '0'
  print("\t\t\t Welcome to the Anime System!")
  while key != '40':
    menu()
    key = input("Choose: ")
    
    if key == '1':
      addDepartment()
    elif key == '2':
      allDepartments()
    elif key == '3':
      delDepartment()
    elif key == '4':
      findDepartment()
      

    elif key == '5':
      addAnimeProject()
    elif key == '6':
      allAnimeProjects()
    elif key == '7':
      delAnimeProject()
    elif key == '8':
      findAnimeProject()
      

    elif key == '9':
      addStaffmember()
    elif key == '10':
      allStaffmember()
    elif key == '11':
      delStaffmember()
    elif key == '12':
      findStaffmember()
      

    elif key == '13':
      addStaffVoiceActor()
    elif key == '14':
      allStaffVoiceActor()
    elif key == '15':
      delStaffVoiceActor()
    elif key == '16':
      findStaffVoiceActor()
      

    elif key == '17':
      addStaffAnimation()
    elif key == '18':
      allStaffAnimation()
    elif key == '19':
      delStaffAnimation()
    elif key == '20':
      findStaffAnimation()
      

    elif key == '21':
      addStaffProduction()
    elif key == '22':
      allStaffProduction()
    elif key == '23':
      delStaffProduction()
    elif key == '24':
      findStaffProduction()
      

    elif key == '25':
      addEpisode()
    elif key == '26':
      delEpisode()
    elif key == '27':
      findEpisode()


    elif key == '28':
      addTask()
    elif key == '29':
      allTask()
    elif key == '30':
      delTask()
    elif key == '31':
      findTask()
      

    elif key == '32':
      addContract()
    elif key == '33':
      allContract()
    elif key == '34':
      delContrac()
    elif key == '35':
      findContract()
      

    elif key == '36':
      addViewers()
    elif key == '37':
      allViewers()
    elif key == '38':
      delViewers()
    elif key == '39':
      findViewers()
    
    elif key == '40':
      print("\n\nThank you for using our system.")
    else:
      print("Select a number from 0 to 42")

main()



