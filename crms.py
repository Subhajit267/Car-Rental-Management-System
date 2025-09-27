"""welcome to car management version 3.05""" #main program
"""BETA 2, full functionality with csv files, all features work; sql connectivity absent"""
"""this is the main file of the program, each screen instance is stored as a function and is executed after its previous screen execution is terinated via a user input"""
"""Developer: SUBHAJIT HALDER"""
"""importing os,sys and my modules to gain access to system commands and the visual elements and string tables."""

"""file imports"""
import os,sys,csv,getpass
"""THIS MODULE IS CREATED TO DEFINE ALL VISUAL ELEMENTS FOR THE PROGRAM"""
#It contains the cursor manipulation function named gotoxy, user icons, progress bar and program logo  

"""LIBRARY IMPORTS"""
import sys,os,ctypes     #using library ctypes to get the classic c/c++ functions to create a local gotoxy function here in python.
import time as t        #time is used for sleep and; os, sys libraries are used to use cmd commands within python such as changing the screen size to enable full screen even in windows 7 and lower, this proram works on any machine with win xp sp3 and above with python 3.xx preinstalled. 


"""GOTOXY FUNCTION"""

#A FEW THINGS WHICH I HAD LEARNED WHILE LEARNING C++, the implementation of gotoxy(); decarng the standard output console handle for use
STD_ERROR_HANDLE = -12  #Standard error handler
#Defining a class named coord containing the _fields_ for data types of x,y using short int data types to store the co-ordinates of x and y; x refers horizontal and y refers vertical

class COORD(ctypes.Structure):      
    _fields_ = [("X", ctypes.c_short), ("Y", ctypes.c_short)]

#defining the function gotoxy for changing the console cursor position to print strings at user defined places rather then printing them line by line. It helps to create a common background or logo and adding a new data/ string on top of it rather than desiging each screen of program seperately thus saving a lot of time.

def gotoxy(x, y): 
    std_out_handle = ctypes.windll.kernel32.GetStdHandle(-11) # We know that the standard buffer for the output handle is -11 thus using it to get the output window from windows 
    coord = COORD(x, y) #Coord here is a cpp function used for setting up the screen cursor position 
    ctypes.windll.kernel32.SetConsoleCursorPosition(std_out_handle, coord) #Setting the console cursor position in the output window



"""MAIN PROGRAM FUNCTIONS: LOOKS BASED"""

"""Background"""
def bg():#Common bacground the big box displaying software name and version in background
    os.system("cls")        #Clearing the screen each time by using windows cmd command, a reason to #include the os and sys modules
    os.system("mode con: cols=193 lines=58")   #Setting an arbitary full screen mode with 192 spaces for characters in x axis and 56 in y.
    #THE BOX CODE Begins
    os.system("cls")
    print()
    print(" ","="*188," ",)
    for i in range(1,53):                                               #instead of printing 52 times a same statement to create border loop is used
        print(" |"," "*186,"|")
    print(" ","="*188," ")
    gotoxy(0,3);print(" |"+" "*82+"CAR RENTAL MANAGEMENT SYSTEM"+" "*75,"  |")  #name
    gotoxy(0,4);print(" |"+" "*82+"--- ------ ---------- ------"+" "*75,"  |")  #name
    gotoxy(0,6);print(" |"+" "*82+"BETA 5, Ver:3.21, Test_BUILD"+" "*75,"  |")  #version
    gotoxy(0,7);print(" |"+" "*82+"~~~~ ~~ ~~~~~~~~~ ~~~~~~~~~~"+" "*75,"  |")  #name
    

"""Logo"""
def logo():#LOGO OF THE PROGRAM, displaying the shortform as an ASCII ART
    gotoxy(1,1);gotoxy(1,1);gotoxy(1,1);gotoxy(1,1);gotoxy(1,1) #providing fixed co ordinates for each ine of the logo as throught the code it remains at the same position.
    #gotoxy(153,24);print(".------------------------------.")
    #gotoxy(153,25);print("| ----    ---   -     -  .---- |")
    #gotoxy(153,26);print("||       |   |  |\   /|  |     |")  old logo 
    #gotoxy(153,27);print("||       .---   | \ / |   ----.|")
    #gotoxy(153,28);print("||       | \    |  -  |       ||")
    #gotoxy(153,29);print("| ---- . |  \ . |     | . ----.|")
    #gotoxy(153,30);print(".------------------------------.")
    gotoxy(148,24);print(".--------------------------------------.")
    gotoxy(148,25);print("|     ____   _____   _     __    _____ |")
    gotoxy(148,26);print("|   /       /     / / |   / /  /       |")
    gotoxy(148,27);print("|  /       /_____/ /  |__/ /  /_____   |")
    gotoxy(148,28);print("| /       /  \    /       /         /  |")
    gotoxy(148,29);print("| _____. /    \. /       /  . _____/.  |")
    gotoxy(148,30);print(".--------------------------------------.")

"""Progress Bar"""
def pb():#A fake progress bar to add to the looks and asthetics of this program.
    gotoxy(93, 39);print("Please Wait..")#Some common strings to be used in every progres bar execution
    gotoxy(95, 40);print("Loading..")
    gotoxy(78, 42);print("[                                        ]");    
    for i in range(1,41):
        gotoxy((78+i), 42);
        print("=",)
        t.sleep(0.08)
        gotoxy((79+i), 42);
    gotoxy(89, 39);print("                      ")#Some common strings to be used in every progres bar execution
    gotoxy(91, 40);print("                       ")

def mu():#user icon for management personnel
    gotoxy(25,20);print("._______________________.")
    gotoxy(25,21);print("| .___________________. |")
    gotoxy(25,22);print("|||                   |||")
    gotoxy(25,23);print("|||      .-----.      |||")    #formal shirt/ uniform
    gotoxy(25,24);print("|||     | ----- |     |||") 
    gotoxy(25,25);print("|||     \|~   ~|/     |||")
    gotoxy(25,26);print("|||     | ^ _ ^ |     |||")
    gotoxy(25,27);print("|||      \ ._. /      |||")
    gotoxy(25,28);print("|||       \___/       |||")
    gotoxy(25,29);print("|||   ____|   |____   |||")
    gotoxy(25,30);print("|||  |   [ \_/ ]   |  |||")
    gotoxy(25,31);print("|||  |    \(|)/    |  |||")
    gotoxy(25,32);print("|||  |      |* ___ |  |||")
    gotoxy(25,33);print("|||  |      |*|---||  |||")
    gotoxy(25,34);print("|||  |      |*|   ||  |||")    
    gotoxy(25,35);print("|||  |      |* --- |  |||")
    gotoxy(25,36);print("|||  |      |*     |  |||")
    gotoxy(25,37);print("|||  |      |*     |  |||")
    gotoxy(25,38);print("|||  |      |*     |  |||")
    gotoxy(25,39);print("|||   -------------   |||")
    gotoxy(25,40);print("|||                   |||")
    gotoxy(25,41);print("| .___________________. |")
    gotoxy(25,42);print("._______________________.")

def nu():#user icon for normal user
    gotoxy(25,21);print("._______________________.")
    gotoxy(25,22);print("| .___________________. |")
    gotoxy(25,23);print("|||                   |||")
    gotoxy(25,24);print("|||      .-----.      |||")    #casual tshirt
    gotoxy(25,25);print("|||     | ----- |     |||") 
    gotoxy(25,26);print("|||     \|~   ~|/     |||")
    gotoxy(25,27);print("|||     | ' _ ' |     |||")
    gotoxy(25,28);print("|||      \ ._. /      |||")
    gotoxy(25,29);print("|||       \___/       |||")
    gotoxy(25,30);print("|||   ____|   |____   |||")
    gotoxy(25,31);print("|||  |   (_____)   |  |||")
    gotoxy(25,32);print("|||  |      |*     |  |||")
    gotoxy(25,33);print("|||  |      |* ___ |  |||")
    gotoxy(25,34);print("|||  |        |---||  |||")
    gotoxy(25,35);print("|||  |        |   ||  |||")
    gotoxy(25,36);print("|||  |         --- |  |||")
    gotoxy(25,37);print("|||  |             |  |||")
    gotoxy(25,38);print("|||  |             |  |||")
    gotoxy(25,39);print("|||  |             |  |||")
    gotoxy(25,40);print("|||   -------------   |||")
    gotoxy(25,41);print("| .___________________. |")
    gotoxy(25,42);print("._______________________.")


    
"""STRING FILE"""
"""THIS FILE IS CREATED TO STORE EVERY SORT OF INSTRUCTIONS AND DEATILS TO BE SHOWN TO THE  USER"""
#This file contains the forms and other piece of info displayed to the user during the installation.

#Importing gotoxy only from looks to change the cursor position


"""Function used to display the Pre-login page""" 
def plp():
    gotoxy(58,16);print(" -------------------------------------------------------------------------------- ")
    gotoxy(58,17);print("|  !!!!!!!!!!!!!!!!WELCOME TO THE CAR RENTAL MANAGEMENT SYSTEM:!!!!!!!!!!!!!!!!  |")
    gotoxy(58,18);print(" -------------------------------------------------------------------------------- ")
    gotoxy(58,19);print("|  ----------------------------------------------------------------------------  |")
    gotoxy(58,20);print("| |                             Available options:                             | |")
    gotoxy(58,21);print("|  ----------------------------------------------------------------------------  |")
    gotoxy(58,22);print("| |          a. LOGIN - press 'l'     b.REGISTER/ SIGN-UP - Press any key      | |")
    gotoxy(58,23);print("| |   Enter You choice:                                                        | |")    
    gotoxy(58,24);print("|  ----------------------------------------------------------------------------  |")

    gotoxy(58,25);print(" -------------------------------------------------------------------------------- ")   

"""Function to take user details"""    
def lp():
    gotoxy(58,18);print(" -------------------------------------------------------------------------------- ")
    gotoxy(58,19);print("|             ENTER USER/ MANAGEMENT PERSONNEL DETAILS TO LOGIN:                 |")
    gotoxy(58,20);print(" -------------------------------------------------------------------------------- ")
    gotoxy(58,21);print("|  ----------------------------------------------------------------------------  |")
    gotoxy(58,22);print("| |                                                                            | |")   
    gotoxy(58,23);print("| |                                                                            | |")   
    gotoxy(58,24);print("| | Enter USER/ Management ID:                                                 | |")
    gotoxy(58,25);print("| |                                                                            | |")  
    gotoxy(58,26);print("| |                                                                            | |")   
    gotoxy(58,27);print("| |                                                                            | |")   
    gotoxy(58,28);print("|  ----------------------------------------------------------------------------  |")
    gotoxy(58,29);print(" -------------------------------------------------------------------------------- ")     
    
"""Function to display installation success and providing some general info regarding the program and its location."""
def ST():
    gotoxy(58,34);print(" -------------------------------------------------------------------------------- ")
    gotoxy(58,35);print("|                                 LOGIN STATUS:                                  |")
    gotoxy(58,36);print(" -------------------------------------------------------------------------------- ")
    gotoxy(58,37);print("|                                                                                |")
    gotoxy(58,38);print("|                                                                                |")
    gotoxy(58,39);print("|                                                                                |")
    gotoxy(58,40);print("|                          <<PRESS ANY KEY TO CONTINUE>>                         |")    
    gotoxy(58,41);print("|                                                                                |")
    gotoxy(58,42);print(" -------------------------------------------------------------------------------- ") 
    
def  mmu():
    gotoxy(58,24);print(" -------------------------------------------------------------------------------- ")
    gotoxy(58,25);print("|  CRMS_MAIN VER: 1.02                              WELCOME:                     |")
    gotoxy(58,26);print(" -------------------------------------------------------------------------------- ")
    gotoxy(58,27);print("|                        |                              |                        |")    
    gotoxy(58,28);print("|                         ------------------------------                         |")
    gotoxy(58,29);print("|                                                                                |")
    gotoxy(58,30);print("|                                                                                |")
    gotoxy(58,31);print("|  Available commands:                                                           |")
    gotoxy(58,32);print("|  ~~~~~~~~~ ~~~~~~~~                                                            |")
    gotoxy(58,33);print("|                                                                                |")
    gotoxy(58,34);print("|                                                                                |")
    gotoxy(58,35);print("|                                                                                |")
    gotoxy(58,36);print("|                                                                                |")
    gotoxy(58,37);print("|                                                                                |")
    gotoxy(58,38);print("|                                                                                |")
    gotoxy(58,39);print("|                                                                                |")
    gotoxy(58,40);print("|      ENTER CHOICE:                                                             |")    
    gotoxy(58,41);print("|                                                                                |")
    gotoxy(58,42);print(" -------------------------------------------------------------------------------- ") 

def  settings():
    gotoxy(58,24);print(" -------------------------------------------------------------------------------- ")
    gotoxy(58,25);print("|  CRMS_MAIN VER: 1.02                              WELCOME:                     |")
    gotoxy(58,26);print(" -------------------------------------------------------------------------------- ")
    gotoxy(58,27);print("|                        |                              |                        |")    
    gotoxy(58,28);print("|                         ------------------------------                         |")
    gotoxy(58,29);print("|                                                                                |")
    gotoxy(58,30);print("|                                                                                |")
    gotoxy(58,31);print("|                                   SETTINGS:                                    |")
    gotoxy(58,32);print("|                                   ~~~~~~~~                                     |")
    gotoxy(58,33);print("|                                                                                |")
    gotoxy(58,34);print("|      a. Update/ Change Account info.                                           |")
    gotoxy(58,35);print("|      b. Change Password only.                                                  |")
    gotoxy(58,36);print("|                                                                                |")
    gotoxy(58,37);print("|                                                                                |")
    gotoxy(58,38);print("|                                                                                |")
    gotoxy(58,39);print("|                                                                                |")
    gotoxy(58,40);print("|      ENTER CHOICE:                                                             |")    
    gotoxy(58,41);print("|                                                                                |")
    gotoxy(58,42);print(" -------------------------------------------------------------------------------- ")

def bookcar():
    gotoxy(58,10);print(" -------------------------------------------------------------------------------- ")
    gotoxy(58,11);print("|  CRMS_MAIN VER: 1.02                              WELCOME:                     |")
    gotoxy(58,12);print(" -------------------------------------------------------------------------------- ")
    gotoxy(58,13);print("|                             | Car Booking Wizard |                             |")    
    gotoxy(58,14);print("|                              --------------------                              |")
    gotoxy(58,15);print("|  AVAILABLE CARS:                                                               |")
    gotoxy(58,16);print("|                                                                                |")
    gotoxy(58,17);print("|                                                                                |")    
    gotoxy(58,18);print("|                                                                                |")
    gotoxy(58,19);print("|                                                                                |")
    gotoxy(58,20);print("|                                                                                |")
    gotoxy(58,21);print("|                                                                                |")
    gotoxy(58,22);print("|                                                                                |")
    gotoxy(58,23);print("|                                                                                |")
    gotoxy(58,24);print("|                                                                                |")
    gotoxy(58,25);print("|                                                                                |")
    gotoxy(58,26);print("|                                                                                |")
    gotoxy(58,27);print("|                                                                                |")
    gotoxy(58,28);print("|                                                                                |")
    gotoxy(58,29);print("|                                                                                |")
    gotoxy(58,30);print("|                                                                                |")
    gotoxy(58,31);print("|                                                                                |")
    gotoxy(58,32);print("|                                                                                |")
    gotoxy(58,33);print("|                                                                                |")
    gotoxy(58,34);print("|                                                                                |")
    gotoxy(58,35);print("|                                                                                |")
    gotoxy(58,36);print("|                                                                                |")
    gotoxy(58,37);print("|                                                                                |")
    gotoxy(58,38);print("|                                                                                |")
    gotoxy(58,39);print("|                                                                                |")
    gotoxy(58,40);print("|                                                                                |")
    gotoxy(58,41);print("|                                                                                |")
    gotoxy(58,42);print("|                                                                                |")
    gotoxy(58,43);print("|                                                                                |")
    gotoxy(58,44);print("|                                                                                |")    
    gotoxy(58,45);print("|                                                                                |")
    gotoxy(58,46);print("|                                                                                |")
    gotoxy(58,47);print("|                                                                                |")
    gotoxy(58,48);print("|                                                                                |") 
    gotoxy(58,49);print("|                                                                                |")     
    gotoxy(58,50);print("|                                                                                |")   
    gotoxy(58,51);print("|                                                                                |")   
    gotoxy(58,52);print("|                                                                                |")
    gotoxy(58,53);print(" -------------------------------------------------------------------------------- ")
    
def rp():
    gotoxy(58,19);print(" -------------------------------------------------------------------------------- ")
    gotoxy(58,20);print("|          ENTER USER/ MANAGEMENT PERSONNEL DETAILS FOR THE DATABASE:            |")
    gotoxy(58,21);print(" -------------------------------------------------------------------------------- ")
    gotoxy(58,22);print("|                                                                                |")
    gotoxy(58,23);print("|  NAME:                                                                         |")
    gotoxy(58,24);print("|  ENTER DESIRED ID NAME: US/ MG -                                               |")
    gotoxy(58,25);print("|  PHONE NUMBER:                                                                 |")
    gotoxy(58,26);print("|  EMAIL ADDRESS:                                                                |")
    gotoxy(58,27);print("|  CITY/ TOWN /Village:                                                          |")
    gotoxy(58,28);print("|  PIN CODE:                                                                     |")
    gotoxy(58,29);print("|  PASSWORD:                                                                     |")    
    gotoxy(58,30);print("|  USER-ID TYPE (Press u for user or press any key for management):              |")
    gotoxy(58,31);print(" -------------------------------------------------------------------------------- ")
    
def up():
    gotoxy(58,19);print(" -------------------------------------------------------------------------------- ")
    gotoxy(58,20);print("|             ENTER USER/ MANAGEMENT PERSONNEL DETAILS TO UPDATE:                |")
    gotoxy(58,21);print(" -------------------------------------------------------------------------------- ")
    gotoxy(58,22);print("|                                                                                |")
    gotoxy(58,23);print("|                                                                                |")
    gotoxy(58,24);print("|                                                                                |")
    gotoxy(58,25);print("|  PHONE NUMBER:                                                                 |")
    gotoxy(58,26);print("|  EMAIL ADDRESS:                                                                |")
    gotoxy(58,27);print("|  CITY/ TOWN /Village:                                                          |")
    gotoxy(58,28);print("|  PIN CODE:                                                                     |")
    gotoxy(58,29);print("|                                                                                |")    
    gotoxy(58,30);print("|                                                                                |")
    gotoxy(58,31);print(" -------------------------------------------------------------------------------- ")     

def pu():
    gotoxy(58,19);print(" -------------------------------------------------------------------------------- ")
    gotoxy(58,20);print("|          ENTER USER/ MANAGEMENT PERSONNEL DETAILS FOR THE DATABASE:            |")
    gotoxy(58,21);print(" -------------------------------------------------------------------------------- ")
    gotoxy(58,22);print("|                                                                                |")
    gotoxy(58,23);print("|                                                                                |")
    gotoxy(58,24);print("|  ENTER old password:                                                           |")
    gotoxy(58,25);print("|  ENTER new password:                                                           |")
    gotoxy(58,26);print("|                                                                                |")
    gotoxy(58,27);print("|                                                                                |")    
    gotoxy(58,28);print("|                                                                                |")
    gotoxy(58,29);print(" -------------------------------------------------------------------------------- ")    


from time import *


nm=uid=pwd=pd=""

def bs(): 
    if os.path.isdir("C:\\CAR_RENTAL_MANAGEMENT_SYSTEM"):#Loading screen of program
        bg();    logo();    pb()
        gotoxy(84,45);    print("<<<PRESS ANY KEY TO CONTINUE>>>")   #SCreen CHanger
        gotoxy(0,56);   input() #Waiting for user input to change the screen
    else:
        bg();    logo();os.system("color 48");
        gotoxy(58,19);print(" -------------------------------------------------------------------------------- ");os.system("color 48")
        gotoxy(58,20);print("| !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!ALERT!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! |");os.system("color 48")
        gotoxy(58,21);print(" -------------------------------------------------------------------------------- ");os.system("color 48")
        gotoxy(58,22);print("|  This computer doesn't contain any version of Car Rental Management System     |");os.system("color 48")
        gotoxy(58,23);print("|  installed. First install the program then run crms_main.exe.                  |");os.system("color 48")
        gotoxy(58,24);print("|                          \a\a\a\a\a\a\a\a\a\a                                                      |");os.system("color 48")
        gotoxy(58,25);print(" -------------------------------------------------------------------------------- ");os.system("color 48")
        gotoxy(85,24);os.system("color 48");a=input();exit();

"""LOGIN FUMCTION"""
def lpi():
    for i in range(0,5):    ##user is provided with five chances to enter correct login credentials
        bg();    logo(); lp();
        if os.path.is

        global pwd,uid,nm,pd ##Name of user aong with user id would be used ater thus global variables
        gotoxy(89,24);   uid=input();
        gotoxy(62,25);   pwd=getpass.getpass()#To hide the password when entered
        with open(r"C:\CAR_RENTAL_MANAGEMENT_SYSTEM\DATABASES\US_DB\usdb.csv","r",newline="\r\n") as ri:#opening the user database file
            rr=list(csv.reader(ri));ri.close();   ##reading the file
        for j in rr:        ##Traversing through details of every user to find the current user
            gotoxy(21,21);
            if j[1]==uid and j[2]==pwd:     ##IF USER FOUND, checking the password
               ST(); gotoxy(58,38);print("|                             LOGIN DETAILS VERIFIED.                            |");    ##Login Verified 
               if uid.startswith("U"):     ##checking if user is normal user
                  nu();           ##displying the normal profile pic 
               else:   
                  mu();           ##displaying management personnel profile pic
               nm=j[0];pd=pwd;input(); """Screen changer"""
               mmui();#Main menu utility
        """collecting the name of user from database"""                    ;
        
        ST(); gotoxy(58,37);print("|\a\a\a                            LOGIN DETAILS MISMATCHED.                           |");input();##Warning of improper details;
    else:
        os.system("color 48");gotoxy(58,38);print("|                LOGIN DETAILS MISMATCHED PROGRAM IS SHUTTING DOWN \a\a\a\a\a\a\a              |");sleep(1); exit(0);##Shutting down the program

"""Pre_LOGIN Page"""
def plpi():
    bg();    logo();    plp();gotoxy(83,23);pi=input()     #Taking user choice for registration/ login
    if pi=="l" or pi=="L":
        lpi();## if registered user
    
    else:       #Registration wizard
        bg();    logo(); rp()
        gotoxy(67,23);  nm=input()  #NAME;
        gotoxy(94,24);  id=input()  #ID
        gotoxy(75,25);  pn=input()  #PhNo.
        gotoxy(76,26);  ea=input()  #Email
        gotoxy(83,27);  ctv=input() #city/town/village
        gotoxy(71,28);  pc=input()  #pincode
        gotoxy(71,29);  pwd=input() #password
        gotoxy(126,30);  a=input()   #user type
        ad={"CITY/ TOWN / VILLAGE:":ctv,"PIN CODE": pc} # ADDRESS DETAILS ALLTOGETHER;
        if a=="u" or a=="U":
            id="US-"+id         #deciding user type user
        else:
            id="MG-"+id         #deciding user type management personnel
        gotoxy(126,33); print("Your user-id is: ",id)
        lc=[nm,id,pn,ea,ctv,pc,pwd]
        #email checker
        import re
        if re.search(r'[\w.]+\@[\w.]+',ea):
            ec=1;
        else:
            ec=0
        for i in lc:
            if i.isspace() or i=="":
               gotoxy(59,35);sc=1;print("One or more of your entered fields is empty. Fill all details. Press any key to continue.");input();plpi();
        else:
            sc=0           
        if len(pn)!=10 or ec==0:
            gotoxy(59,35);print("Your phone number/ email-id is invalid, check it. Fill all details. Press any key to continue.");input();plpi();
     
        if len(pwd)>=6 and len(pwd)<=15 and ec==1:
            for i in lc:
                if i.isspace() or i=="":
                   gotoxy(59,35);print("One or more of your entered fields is empty. Fill all details. Press any key to continue.");input();plpi();
            else:
                sc=0;gotoxy(126,33); print("Your user-id is: ",id)
                gotoxy(78, 38);print("Saving Details....PLEASE WAIT....");sleep(1)
                with open(r"C:\CAR_RENTAL_MANAGEMENT_SYSTEM\DATABASES\US_DB\usdb.csv","a") as f:
                    fw=csv.writer(f)
                    fw.writerow([nm,id,pwd,ea,pn,ad])       #saving new user
                pb();                                           # FAKE loading bar
                gotoxy(80,45);    print("<<<PRESS ANY KEY TO CONTINUE>>>")   #SCreen CHanger
                input();lpi();  #going to the login page for first login.
            
        else:
            gotoxy(15,33);print("\a\a\a\a\aPASSWORD MUST BE HAVING BETWEEN 6 to 15 CHARACTERS. Change your password. Press any key.")
            input();plpi();

"""Main Menu Utility Inputs"""
def mmui():
    while 1:    ##Infinite loop to create a shell
        bg();   logo(); mmu(); #Page setup
        gotoxy(65,33);print("\aa. Settings.")     #Common options for nu and mu
        gotoxy(65,34);print("b. Exit.");gotoxy(120,25); print(nm)
        if uid[0]=="U":         #If normal user
            gotoxy(84,27);print("         USER_CONSOLE");nu();
            gotoxy(65,35);print("c. Book car.");
            gotoxy(80,40);cmd=input();gotoxy(0,56)
            if cmd=="login":        #an easy way to switch user
                lpi()
            elif cmd=="plpi":   #an easy way to create new user
                plpi()
            elif cmd=="a" or cmd=="A":      #displaying settings page
                settings();gotoxy(120,25); print(nm); gotoxy(84,27);print("         USER_CONSOLE");nu();gotoxy(80,40);ch=input();
                if ch=="a" or ch=="A":
                    bg();logo;nu(); up();
                    gotoxy(75,25);  pn=input()  #PhNo.
                    gotoxy(76,26);  ea=input()  #Email
                    gotoxy(83,27);  ctv=input() #city/town/village
                    gotoxy(71,28);  pc=input()  #pincode
                    ad={"CTY/ TWN / VILL:":ctv,"PIN": pc} # ADDRESS DETAILS ALLTOGETHER;
                    gotoxy(94,51);udd=[nm,uid,pd,pn,ea,ad]
                    import re
                    if re.search(r'[\w.]+\@[\w.]+',ea):
                        ec=1;
                    else:
                        ec=0;
                    if ec==0 or len(pn)!=10 or ctv.count(" ")==len(ctv) or pc.count(" ")==len(pc) or ctv=="" or pc=="":
                        gotoxy(59,35);print("Your phone number/ email-id might be invalid. Fill all details. Press any key to continue.");input();mmui();
                    with open(r"C:\CAR_RENTAL_MANAGEMENT_SYSTEM\DATABASES\US_DB\usdb.csv","r",newline='\r\n') as ri:      #loading previous car availability details
                        rr=list(csv.reader(ri));ri.close();
                        for i in rr:
                            if i[1]==uid:
                                ind=rr.index(i)
                                rr.pop(ind)
                                rr.insert(ind,udd)
                                with open(r"C:\CAR_RENTAL_MANAGEMENT_SYSTEM\DATABASES\US_DB\usdb_t.csv","w") as r1:               #copying to temp file             
                                    rt=csv.writer(r1)
                                    rt.writerows(rr)
                                os.system(r"del C:\CAR_RENTAL_MANAGEMENT_SYSTEM\DATABASES\US_DB\usdb.csv")                            #deleting previous details
                                with open(r"C:\CAR_RENTAL_MANAGEMENT_SYSTEM\DATABASES\US_DB\usdb_t.csv","r",newline='\r\n') as r1i:   #Reading from temp file
                                    rr1=list(csv.reader(r1i))
                                    with open(r"C:\CAR_RENTAL_MANAGEMENT_SYSTEM\DATABASES\US_DB\usdb.csv","w") as r2:                 #Writing to new availability file        
                                        r1t=csv.writer(r2)
                                        r1t.writerows(rr1)              
                                os.system(r"del C:\CAR_RENTAL_MANAGEMENT_SYSTEM\DATABASES\US_DB\usdb_t.csv")              #            #Deleting the temp file
                    gotoxy(58,30);print("|                           DETAILS SAVED SUCCESSFULLY                           |");input();
                elif ch=="b" or ch=="B":
                    bg();logo;nu(); pu();
                    gotoxy(82,24);  opwd=input()  #PhNo.
                    gotoxy(82,25);  npwd=input()  #Email
                    if opwd==pwd:
                        with open(r"C:\CAR_RENTAL_MANAGEMENT_SYSTEM\DATABASES\US_DB\usdb.csv","r",newline='\r\n') as ri:      #loading previous car availability details
                            rr=list(csv.reader(ri));ri.close();
                            for i in rr:
                                if i[1]==uid:
                                    N=rr.index(i)
                                    rr[N][2]=npwd
                            with open(r"C:\CAR_RENTAL_MANAGEMENT_SYSTEM\DATABASES\US_DB\usdb_t.csv","w") as r1:               #copying to temp file             
                                rt=csv.writer(r1)
                                rt.writerows(rr)
                        os.system(r"del C:\CAR_RENTAL_MANAGEMENT_SYSTEM\DATABASES\US_DB\usdb.csv")                            #deleting previous details
                        with open(r"C:\CAR_RENTAL_MANAGEMENT_SYSTEM\DATABASES\US_DB\usdb_t.csv","r",newline='\r\n') as r1i:   #Reading from temp file
                            rr1=list(csv.reader(r1i))
                            with open(r"C:\CAR_RENTAL_MANAGEMENT_SYSTEM\DATABASES\US_DB\usdb.csv","w") as r2:                 #Writing to new availability file        
                                r1t=csv.writer(r2)
                                r1t.writerows(rr1)              
                        os.system(r"del C:\CAR_RENTAL_MANAGEMENT_SYSTEM\DATABASES\US_DB\crasdb_t.csv")
                        gotoxy(58,28);print("|                           DETAILS SAVED SUCCESSFULLY                           |");input();
                else:   #If enetered command/ option doesn't exist.
                    gotoxy(78, 38);print("\a\t Entered command doesn't exist.....");input()

            elif cmd=="b" or cmd=="B":      #Program exit          
                gotoxy(82,42);print("\a\a\a\a\a\a\a\a\aTHANK YOU FOR USING, SHUTTING DOWN");sleep(1)
                exit(0)
            elif cmd=="c" or cmd=="C":      #car booking wizard
                bg();   logo(); nu(); bookcar();gotoxy(120,11); print(nm);gotoxy(58,13);print("|                             | Car Booking Wizard |                             |")     #changing the caption for car booking
                gotoxy(58,48);print("|      ENTER Car-ID, time slot and date:                                         |") 
                gotoxy(58,49);print("|      STATUS:                                                                   |") 
                with open(r"C:\CAR_RENTAL_MANAGEMENT_SYSTEM\DATABASES\CR_DB\crasdb.csv","r",newline='\r\n') as ri:  #displaying available and booked cars
                    rr=csv.reader(ri);n=16;
                    for j in rr:
                        m=0;
                        for k in j:
                            gotoxy(60+m,n);print(k)
                            m+=15
                        n+=1
                        gotoxy(64,n);                        
                gotoxy(100,48);l=[uid]+input().split(','); N=l[1]      #taking user choice of rental car

                                    
                with open(r"C:\CAR_RENTAL_MANAGEMENT_SYSTEM\DATABASES\CR_DB\crasdb.csv","r",newline='\r\n') as ri:      #loading previous car availability details
                    rr=list(csv.reader(ri));ri.close();
                    for j in rr:
                        if j[0]==l[1] and  j[-1]=="Available":
                            with open(r"C:\CAR_RENTAL_MANAGEMENT_SYSTEM\DATABASES\RT_DB\rtdb.csv","a") as rty:  #saving car rental details
                                rtw=csv.writer(rty)
                                rtw.writerow(l)
                            with open(r"C:\CAR_RENTAL_MANAGEMENT_SYSTEM\DATABASES\CR_DB\crasdb.csv","r",newline='\r\n') as ri:      #loading previous car availability details
                                rr=list(csv.reader(ri));rr[int(N)][-1]="Booked"
                                with open(r"C:\CAR_RENTAL_MANAGEMENT_SYSTEM\DATABASES\CR_DB\crasdb_t.csv","w") as r1:               #copying to temp file             
                                    rt=csv.writer(r1)
                                    rt.writerows(rr)
                            os.system(r"del C:\CAR_RENTAL_MANAGEMENT_SYSTEM\DATABASES\CR_DB\crasdb.csv")                            #deleting previous details
                            with open(r"C:\CAR_RENTAL_MANAGEMENT_SYSTEM\DATABASES\CR_DB\crasdb_t.csv","r",newline='\r\n') as r1i:   #Reading from temp file
                                rr1=list(csv.reader(r1i))
                                with open(r"C:\CAR_RENTAL_MANAGEMENT_SYSTEM\DATABASES\CR_DB\crasdb.csv","w") as r2:                 #Writing to new availability file        
                                    r1t=csv.writer(r2)
                                    r1t.writerows(rr1)              
                            os.system(r"del C:\CAR_RENTAL_MANAGEMENT_SYSTEM\DATABASES\CR_DB\crasdb_t.csv")                          #Deleting the temp file
                            gotoxy(75,52);print("\a\aCAR details added/ updated SUCCESSFULLY.");input();mmui();                 
                    else:
                        gotoxy(75,52);print("\a\a\aCAR doesn't exist/ or unavailable.");input();mmui();                  
                                                               #SUccessfully booked the car           
                
            else:   #If enetered command/ option doesn't exist.
                gotoxy(78, 38);print("\a\t Entered command doesn't exist.....");input()


        else:   #if management personnel
            gotoxy(84,27);print("      MANAGEMENT_CONSOLE");mu();
            gotoxy(65,35);print("c. Add/update car details.")
            gotoxy(65,36);print("d. Delete car details.")
            gotoxy(65,37);print("e. Car availability update.")
            gotoxy(65,38);print("f. Check user details.")
            gotoxy(80,40);cmd=input();gotoxy(0,56)
            if cmd=="login":        #an easy way to switch user
                lpi()
            elif cmd=="new_user":   #an easy way to create new user
                plpi()
            elif cmd=="a" or cmd=="A":      #displaying settings page
                settings();gotoxy(120,25); print(nm);gotoxy(84,27);print("      MANAGEMENT_CONSOLE");mu();gotoxy(80,40);ch=input();
                if ch=="a" or ch=="A":
                    bg();logo;nu(); up();
                    gotoxy(75,25);  pn=input()  #PhNo.
                    gotoxy(76,26);  ea=input()  #Email
                    gotoxy(83,27);  ctv=input() #city/town/village
                    gotoxy(71,28);  pc=input()  #pincode
                    ad={"CITY/ TOWN / VILLAGE:":ctv,"PIN CODE": pc} # ADDRESS DETAILS ALLTOGETHER;
                    gotoxy(94,51);udd=[nm,uid,pd,pn,ea,ad]
                    import re
                    if re.search(r'[\w.]+\@[\w.]+',ea):
                        ec=1;
                    else:
                        ec=0;
                    if ec==0 or len(pn)!=10 or ctv.isspace() or pc.isspace or ctv=="" or pc=="":
                        gotoxy(15,35);print("Your phone number/ email-id might be invalid. Fill all details. Press any key to continue.");input();mmui();
                    with open(r"C:\CAR_RENTAL_MANAGEMENT_SYSTEM\DATABASES\US_DB\usdb.csv","r",newline='\r\n') as ri:      #loading previous car availability details
                        rr=list(csv.reader(ri));ri.close();
                        for i in rr:
                            if i[1]==uid:
                                ind=rr.index(i)
                                rr.pop(ind)
                                rr.insert(ind,udd)
                                with open(r"C:\CAR_RENTAL_MANAGEMENT_SYSTEM\DATABASES\US_DB\usdb_t.csv","w") as r1:               #copying to temp file             
                                    rt=csv.writer(r1)
                                    rt.writerows(rr)
                                os.system(r"del C:\CAR_RENTAL_MANAGEMENT_SYSTEM\DATABASES\US_DB\usdb.csv")                            #deleting previous details
                                with open(r"C:\CAR_RENTAL_MANAGEMENT_SYSTEM\DATABASES\US_DB\usdb_t.csv","r",newline='\r\n') as r1i:   #Reading from temp file
                                    rr1=list(csv.reader(r1i))
                                    with open(r"C:\CAR_RENTAL_MANAGEMENT_SYSTEM\DATABASES\US_DB\usdb.csv","w") as r2:                 #Writing to new availability file        
                                        r1t=csv.writer(r2)
                                        r1t.writerows(rr1)              
                                os.system(r"del C:\CAR_RENTAL_MANAGEMENT_SYSTEM\DATABASES\US_DB\usdb_t.csv")              #            #Deleting the temp file
                    gotoxy(58,30);print("|\a\a\a                           DETAILS SAVED SUCCESSFULLY                           |");input();
                elif ch=="b" or ch=="B":
                    bg();logo;nu(); pu();
                    gotoxy(82,24);  opwd=input()  #PhNo.
                    gotoxy(82,25);  npwd=input()  #Email
                    if opwd==pwd:
                        with open(r"C:\CAR_RENTAL_MANAGEMENT_SYSTEM\DATABASES\US_DB\usdb.csv","r",newline='\r\n') as ri:      #loading previous car availability details
                            rr=list(csv.reader(ri));ri.close();
                            for i in rr:
                                if i[1]==uid:
                                    N=rr.index(i)
                                    rr[N][2]=npwd
                            with open(r"C:\CAR_RENTAL_MANAGEMENT_SYSTEM\DATABASES\US_DB\usdb_t.csv","w") as r1:               #copying to temp file             
                                rt=csv.writer(r1)
                                rt.writerows(rr)
                        os.system(r"del C:\CAR_RENTAL_MANAGEMENT_SYSTEM\DATABASES\US_DB\usdb.csv")                            #deleting previous details
                        with open(r"C:\CAR_RENTAL_MANAGEMENT_SYSTEM\DATABASES\US_DB\usdb_t.csv","r",newline='\r\n') as r1i:   #Reading from temp file
                            rr1=list(csv.reader(r1i))
                            with open(r"C:\CAR_RENTAL_MANAGEMENT_SYSTEM\DATABASES\US_DB\usdb.csv","w") as r2:                 #Writing to new availability file        
                                r1t=csv.writer(r2)
                                r1t.writerows(rr1)              
                        os.system(r"del C:\CAR_RENTAL_MANAGEMENT_SYSTEM\DATABASES\US_DB\usdb_t.csv")
                        gotoxy(58,28);print("|\a\a\a                           DETAILS SAVED SUCCESSFULLY                           |");input();
                else:   #If enetered command/ option doesn't exist.
                    gotoxy(78, 38);print("\a\a\a\a\t Entered command doesn't exist.....");input()
            elif cmd=="b" or cmd=="B":                
                gotoxy(84, 42);print("\a\a\a\a\a\a\a\a\aTHANK YOU FOR USING, SHUTTING DOWN");sleep(1)
                exit()
            elif cmd=="c" or cmd=="C":
                bookcar();gotoxy(120,11); print(nm);
                gotoxy(58,13);print("|                       | Add/Update Car Details Wizard |                        |");gotoxy(58,14);print("|                        -------------------------------                         |")
                with open(r"C:\CAR_RENTAL_MANAGEMENT_SYSTEM\DATABASES\CR_DB\crasdb.csv","r",newline='\r\n') as ri:  #displaying available and booked cars
                    rr=csv.reader(ri);n=16;
                    for j in rr:
                        m=0;
                        for k in j:
                            gotoxy(60+m,n);print(k)
                            m+=15
                        n+=1
                        gotoxy(64,n);
                gotoxy(58,50);print("|      ENTER New/Existing Car-ID:                                                |");gotoxy(94,50);cid=input()
                gotoxy(58,51);print("|      ENTER new Brand,MODEL,type:                                               |");gotoxy(94,51);cdt=[str(cid),]+input().split(',')+["Available"];
                if cid=="":
                    gotoxy(75,52);print("\a\a\aCAR doesn't exist.");input();mmui();
                    
                with open(r"C:\CAR_RENTAL_MANAGEMENT_SYSTEM\DATABASES\CR_DB\crasdb.csv","r",newline='\r\n') as ri:      #loading previous car availability details
                    rr=list(csv.reader(ri));
                    for j in rr:
                        if j[0]==cid:
                            ji=rr.index(j)
                            rr.pop(ji)
                            rr.insert(ji,cdt);break;                    
                    else:
                        if int(cid)>len(rr):
                            rr.append(cdt)
                        else:
                            rr.insert(int(cid),cdt);
                        
                    with open(r"C:\CAR_RENTAL_MANAGEMENT_SYSTEM\DATABASES\CR_DB\crasdb_t.csv","w") as r1:               #copying to temp file             
                        rt=csv.writer(r1)
                        rt.writerows(rr)
                os.system(r"del C:\CAR_RENTAL_MANAGEMENT_SYSTEM\DATABASES\CR_DB\crasdb.csv")                            #deleting previous details
                with open(r"C:\CAR_RENTAL_MANAGEMENT_SYSTEM\DATABASES\CR_DB\crasdb_t.csv","r",newline='\r\n') as r1i:   #Reading from temp file
                    rr1=list(csv.reader(r1i))
                    with open(r"C:\CAR_RENTAL_MANAGEMENT_SYSTEM\DATABASES\CR_DB\crasdb.csv","w") as r2:                 #Writing to new availability file        
                        r1t=csv.writer(r2)
                        r1t.writerows(rr1)              
                os.system(r"del C:\CAR_RENTAL_MANAGEMENT_SYSTEM\DATABASES\CR_DB\crasdb_t.csv")                          #Deleting the temp file
                gotoxy(75,52);print("\a\aCAR details added/ updated SUCCESSFULLY.");input();

            elif cmd=="d" or cmd=="D":
                bookcar();gotoxy(120,25); print(nm);
                gotoxy(58,13);print("|                     | Delete Car Details Booking Wizard |                      |");gotoxy(58,14);print("|                      -----------------------------------                       |")
                with open(r"C:\CAR_RENTAL_MANAGEMENT_SYSTEM\DATABASES\CR_DB\crasdb.csv","r",newline='\r\n') as ri:  #displaying available and booked cars
                    rr=csv.reader(ri);n=16;
                    for j in rr:
                        m=0;
                        for k in j:
                            gotoxy(60+m,n);print(k)
                            m+=15
                        n+=1
                        gotoxy(64,n);
                gotoxy(58,50);print("|      ENTER Car-ID:                                                             |");gotoxy(80,50);cid=input()
                with open(r"C:\CAR_RENTAL_MANAGEMENT_SYSTEM\DATABASES\CR_DB\crasdb.csv","r",newline='\r\n') as ri:      #loading previous car availability details
                    rr=list(csv.reader(ri));ri.close()
                    for i in rr:
                        if i[0]==str(cid):
                            rr.pop(int(cid))
                            with open(r"C:\CAR_RENTAL_MANAGEMENT_SYSTEM\DATABASES\CR_DB\crasdb_t.csv","w") as r1:               #copying to temp file             
                                rt=csv.writer(r1)
                                rt.writerows(rr)                      
                            os.system(r"del C:\CAR_RENTAL_MANAGEMENT_SYSTEM\DATABASES\CR_DB\crasdb.csv")                            #deleting previous details
                            with open(r"C:\CAR_RENTAL_MANAGEMENT_SYSTEM\DATABASES\CR_DB\crasdb_t.csv","r",newline='\r\n') as r1i:   #Reading from temp file
                                rr1=list(csv.reader(r1i))
                                with open(r"C:\CAR_RENTAL_MANAGEMENT_SYSTEM\DATABASES\CR_DB\crasdb.csv","w") as r2:                 #Writing to new availability file      
                                    r1t=csv.writer(r2)
                                    r1t.writerows(rr1)              
                            os.system(r"del C:\CAR_RENTAL_MANAGEMENT_SYSTEM\DATABASES\CR_DB\crasdb_t.csv")
                            gotoxy(75,51);print("\a\aCAR details removed SUCCESSFULLY.");input();break;
                    else:
                        gotoxy(75,51);print("\a\a\aCAR doesn't exist.");input();                    
                
                    
            elif cmd=="e" or cmd=="e":
                bookcar();gotoxy(120,11); print(nm);
                gotoxy(58,13);print("|                     |   Car Availability Update Wizard  |                      |");gotoxy(58,14);print("|                      -----------------------------------                       |")
                with open(r"C:\CAR_RENTAL_MANAGEMENT_SYSTEM\DATABASES\CR_DB\crasdb.csv","r",newline='\r\n') as ri:  #displaying available and booked cars
                    rr=csv.reader(ri);n=16;
                    for j in rr:
                        m=0;
                        for k in j:
                            gotoxy(60+m,n);print(k)
                            m+=15
                        n+=1
                        gotoxy(64,n);
                gotoxy(58,50);print("|      ENTER Car-ID:                                                             |");gotoxy(80,50);cid=input()
                with open(r"C:\CAR_RENTAL_MANAGEMENT_SYSTEM\DATABASES\CR_DB\crasdb.csv","r",newline='\r\n') as ri:      #loading previous car availability details
                    rr=list(csv.reader(ri));ri.close()
                    for i in rr:
                        if i[0]==str(cid):
                            rr[int(cid)][4]="Available"
                            with open(r"C:\CAR_RENTAL_MANAGEMENT_SYSTEM\DATABASES\CR_DB\crasdb_t.csv","w") as r1:               #copying to temp file             
                                rt=csv.writer(r1)
                                rt.writerows(rr)                      
                            os.system(r"del C:\CAR_RENTAL_MANAGEMENT_SYSTEM\DATABASES\CR_DB\crasdb.csv")                            #deleting previous details
                            with open(r"C:\CAR_RENTAL_MANAGEMENT_SYSTEM\DATABASES\CR_DB\crasdb_t.csv","r",newline='\r\n') as r1i:   #Reading from temp file
                                rr1=list(csv.reader(r1i))
                                with open(r"C:\CAR_RENTAL_MANAGEMENT_SYSTEM\DATABASES\CR_DB\crasdb.csv","w") as r2:                 #Writing to new availability file      
                                    r1t=csv.writer(r2)
                                    r1t.writerows(rr1)              
                            os.system(r"del C:\CAR_RENTAL_MANAGEMENT_SYSTEM\DATABASES\CR_DB\crasdb_t.csv")
                            gotoxy(75,49);print("\a\aCAR made available SUCCESSFULLY.");input();break;
                    else:
                        gotoxy(75,51);print("\a\a\aCAR doesn't exist.");input();
            elif cmd=="f" or cmd=='F':
                bookcar();gotoxy(120,11); print(nm);
                gotoxy(58,13);print("|                    |   USER_DETAILS(MANAGEMENT INCLUDED) |                     |");gotoxy(58,14);print("|                      -----------------------------------                       |")
                with open(r"C:\CAR_RENTAL_MANAGEMENT_SYSTEM\DATABASES\US_DB\usdb.csv","r",newline='\r\n') as ri:  #displaying available and booked cars
                    rr=csv.reader(ri);n=16;
                    for j in rr:
                        m=0;
                        for k in j:
                            gotoxy(60+m,n);print(k)
                            m+=9
                        n+=1
                        gotoxy(64,n);
                input();
            else:   #If enetered command/ option doesn't exist.
                gotoxy(78, 38);print("\a\a\a\t Entered command doesn't exist.....");input()
                    
                

#EXECUTION BEGINS
#__main__
bs()
plpi()
