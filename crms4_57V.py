"""welcome to car management version 4.57""" #main program
"""BETA 9, full functionality with csv files, all features work; sql connectivity absent"""
"""this is the main file of the program, each screen instance is stored as a function and is executed after its previous screen execution is terinated via a user input"""
'''     Author: SUBHAJIT HALDER 
       DATE: 23/01/2024'''
"""importing os,sys and my modules to gain access to system commands and the visual elements and string tables."""

"""file imports"""
import os,sys,csv,getpass
from time import *
"""THIS MODULE IS CREATED TO DEFINE ALL VISUAL ELEMENTS FOR THE PROGRAM"""
#It contains the cursor manipulation function named gotoxy, user icons, progress bar and program logo  

"""LIBRARY IMPORTS"""
import ctypes     #using library ctypes to get the classic c/c++ functions to create a local gotoxy function here in python.
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
    gotoxy(0,6);print(" |"+" "*82+"BETA 9, Ver:4.57, Eval_BUILD"+" "*75,"  |")  #version
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


    


nm=uid=pwd=pd=""
cs=""
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
    gotoxy(58,22);print("| | a. LOGIN - press 'l'   b.REGISTER/ SIGN-UP - Press any key     c. Exit     | |")
    gotoxy(58,23);print("| |   Enter You choice:                                                        | |")    
    gotoxy(58,24);print("|  ----------------------------------------------------------------------------  |")

    gotoxy(58,25);print(" -------------------------------------------------------------------------------- ")   

"""Function to take user details"""    
def lp():
    gotoxy(58,18);print(" -------------------------------------------------------------------------------- ")
    gotoxy(58,19);print("|              ENTER USER/ MANAGEMENT PERSONNEL DETAILS TO LOGIN:                |")
    gotoxy(58,20);print(" -------------------------------------------------------------------------------- ")
    gotoxy(58,21);print("|  ----------------------------------------------------------------------------  |")
    gotoxy(58,22);print("| |              ####press e in user-id to exit this menu ####                 | |")
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
    gotoxy(58,25);print("|  CRMS_MAIN VER: 4.22                              WELCOME:                     |")
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
    gotoxy(58,18);print(" "*110)
    gotoxy(58,19);print(" "*110)
    gotoxy(58,20);print(" "*110)
    gotoxy(58,21);print(" "*110)
    gotoxy(58,22);print(" "*110)
    gotoxy(58,23);print(" "*110)
    gotoxy(58,24);print(" -------------------------------------------------------------------------------- ")
    gotoxy(58,25);print("|  CRMS_MAIN VER: 1.02                              WELCOME:                     |")
    gotoxy(58,26);print(" -------------------------------------------------------------------------------- ")
    gotoxy(58,27);print("|                        |                              |                        |")    
    gotoxy(58,28);print("|                         ------------------------------                         |")
    gotoxy(58,29);print("|                                                                                |")
    gotoxy(58,30);print("|                                                                                |")
    gotoxy(58,31);print("|                                   SETTINGS:                                    |")
    gotoxy(58,32);print("|                                   ~~~~~~~~                                     |")
    gotoxy(58,33);print("|                                                                                |"," "*11)
    gotoxy(58,34);print("|      a. Update/ Change Account info.                                           |"," "*11)
    gotoxy(58,35);print("|      b. Change Password only.                                                  |"," "*11)
    gotoxy(58,36);print("|      c. Return to previous menu.                                               |"," "*11)
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
    gotoxy(58,20);print("|             ENTER USER/ MANAGEMENT PERSONNEL DETAILS TO UPDATE:                |")
    gotoxy(58,21);print(" -------------------------------------------------------------------------------- ")
    gotoxy(58,22);print("|               ####press e in 1st field to exit this menu ####                  |")
    gotoxy(58,23);print("|                                                                                |")
    gotoxy(58,24);print("|                                                                                |")
    gotoxy(58,25);print("|  PHONE NUMBER:                                                                 |")
    gotoxy(58,26);print("|  EMAIL ADDRESS:                                                                |")
    gotoxy(58,27);print("|  CITY/ TOWN /Village:                                                          |")
    gotoxy(58,28);print("|  PIN CODE:                                                                     |")
    gotoxy(58,29);print("|                                                                                |")    
    gotoxy(58,30);print("|                                                                                |")
    gotoxy(58,31);print(" -------------------------------------------------------------------------------- ")  
    gotoxy(58,32);print("                                                                                  ")  
    gotoxy(58,33);print("                                                                                  ")  
    gotoxy(58,34);print("                                                                                  ")  
    gotoxy(58,35);print("                                                                                  ")  
    gotoxy(58,36);print("                                                                                  ")  
    gotoxy(58,37);print("                                                                                  ")  
    gotoxy(58,38);print("                                                                                  ")  
    gotoxy(58,39);print("                                                                                  ")  
    gotoxy(58,40);print("                                                                                  ")  
    gotoxy(58,41);print("                                                                                  ")  
    gotoxy(58,42);print("                                                                                  ")  
    gotoxy(58,43);print("                                                                                  ")  
    
    

def pu():
    gotoxy(58,19);print(" -------------------------------------------------------------------------------- ")
    gotoxy(58,20);print("|          ENTER USER/ MANAGEMENT PERSONNEL DETAILS FOR THE DATABASE:            |")
    gotoxy(58,21);print(" -------------------------------------------------------------------------------- ")
    gotoxy(58,22);print("|             ####press e in old password to exit this menu ####                 |")
    gotoxy(58,23);print("|                                                                                |")
    gotoxy(58,24);print("|  ENTER old password:                                                           |")
    gotoxy(58,25);print("|  ENTER new password:                                                           |")
    gotoxy(58,26);print("|                                                                                |")
    gotoxy(58,27);print("|                                                                                |")    
    gotoxy(58,28);print("|                                                                                |")
    gotoxy(58,29);print(" -------------------------------------------------------------------------------- ")    


def check_internet():
    cmd = os.system('ping google.com -w 4 > clear')
    if cmd == 0:
        print('Internet is not connected')
        t.sleep(1);exit(0)

import mysql.connector as sq
mycon=sq.connect(host="mysql-39564a5e-harukiokinawa267-1671.a.aivencloud.com",user="avnadmin",passwd="AVNS_NYrquhFEr67c70lQ3f0",port=26911,database="defaultdb")
if mycon.is_connected():
    pass;
else:
    print("ERROR connecting to database")
    time.sleep(1);exit(0);
myc=mycon.cursor()

'''BOOTSCREEN/ SYSTEM INSTALLATION STATE CHECKER'''
def bs(): 

    if os.path.isdir("C:\\CAR_RENTAL_MANAGEMENT_SYSTEM\\DATABASES"):#Checking if the system has any version of crms installed
        bg();    logo();    pb()                                    #LOADING SCREEN
        gotoxy(84,45);    print("<<<PRESS ANY KEY TO CONTINUE>>>")  #SCreen CHanger
        gotoxy(0,56);   input()                                     #Waiting for user input to change the screen

    else:                                                           #IF THE PROGRAM IS NOT INSTALLED
        bg();    logo();os.system("color 48");                      #SCREEN SETUP, Setting red color to display alert!!!
        gotoxy(58,19);print(" -------------------------------------------------------------------------------- ");os.system("color 48")
        gotoxy(58,20);print("| !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!ALERT!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! |");os.system("color 48") #STRING TABLE DISPLAYING ERROR MESSAGE
        gotoxy(58,21);print(" -------------------------------------------------------------------------------- ");os.system("color 48")
        gotoxy(58,22);print("|  This computer doesn't contain any version of Car Rental Management System     |");os.system("color 48") #ASKING THE USER FOR A FRESH INSTALLATION
        gotoxy(58,23);print("|  installed. First install the program then run crms_main.exe.                  |");os.system("color 48")
        gotoxy(58,24);print("|                          \a\a\a\a\a\a\a\a\a\a                                                      |");os.system("color 48")#ERROR SOUND
        gotoxy(58,25);print(" -------------------------------------------------------------------------------- ");os.system("color 48")
        gotoxy(85,24);os.system("color 48");a=input();exit();                                                                           #SHUTS THE PROGRAM

'''LOGIN PAGE INTERFACE'''
def lpi():
    
    if os.path.isdir("C:\\CAR_RENTAL_MANAGEMENT_SYSTEM\\DATABASES"):     ####CHECKING IF THE USER PROFILE DATABASE EXISTS
        global uid,pwd,pd,nm
        for i in range(0,5):                                                            ##user is provided with five chances to enter correct login credentials

            bg();    logo(); lp();                                                      #Screen setup, dispaying the login screen
                                                           ##Name of user along with user id would be used later thus global variables
            gotoxy(89,24);   uid=input();
            if uid=="e" or uid=="E":
                plpi();
            gotoxy(62,25);   pwd=getpass.getpass()                                      #To hide the password when entered

            #with open(r"C:\CAR_RENTAL_MANAGEMENT_SYSTEM\DATABASES\US_DB\usdb.csv","r",newline="\r\n") as ri:                    #OPENING THE USER DATABASE FILE
            myc.execute("select * from usdb")
            rr=list(myc.fetchall());                                                                          ##reading the file
            for j in rr:                                                                ##Traversing through details of every user to check if enetered USER_ID exists
                gotoxy(21,21);
                if j[1]==uid and j[2]==pwd:     ##IF USER FOUND, checking the entered password with the database password
                    ST(); gotoxy(58,38);print("|                             LOGIN DETAILS VERIFIED.                            |");    ##PASSWORD CORRECT, LOGIN SUCCESS 
                    if uid.startswith("U"):     #####CHECKING USER TYPE TO DISPLAY PROPER PROFILE IMAGE
                        nu();                       #Regular user; casually dressed guy  
                    else:   
                        mu();                       #Management personnel, formally dressed guy 
                    nm=j[0];"""collecting the name of user from database"""  ;pd=pwd;input(); """Screen changer"""
                    mmui();                     #####MAIN SHELL LINK#####
            else:  
                ST(); gotoxy(58,37);print("|\a\a\a                            LOGIN DETAILS MISMATCHED.                           |");input();##Warning of improper details;

        else:                                                                           #####IF WRONG PASSWORD IS ENTERED FOR MORE THAN 5 TIMES   
            os.system("color 48");gotoxy(58,38);print("|                LOGIN DETAILS MISMATCHED PROGRAM IS SHUTTING DOWN \a\a\a\a\a\a\a              |");sleep(1); exit() ##Shutting down the program, to prevent unauthorised access.
    else:                                                                               ######IF USER DATABASE DOESN"T EXIST                                     
        os.system("color 48");gotoxy(58,38);    print("              LOGIN DETAILS DOESN'T EXIST. REGISTER USER TO LOGIN   \a\a\a\a\a\a\a             |");sleep(1); plpi();

def reg():
    global rs,nm,uid,pwd,cs
    if rs==0:
        rp();
        if rs!=1:
            gotoxy(58,23);print("|  NAME:                                                                         |")
            gotoxy(58,24);print("|  ENTER DESIRED ID NAME: US/ MG -                                               |")
            gotoxy(58,29);print("|  PASSWORD:                                                                     |")    
            gotoxy(58,30);print("|  USER-ID TYPE (Press u for user or press any key for management):              |")
            gotoxy(67,23);  unm=input()  #NAME;
            if unm=="e" or unm=="E":
                plpi();
            gotoxy(94,24);  id=input()  #ID        
    gotoxy(75,25);  pn=input()  #PhNo.
    gotoxy(76,26);  ea=input()  #Email
    gotoxy(83,27);  ctv=input() #city/town/village
    gotoxy(71,28);  pc=input()  #pincode    
    if rs==0:
        gotoxy(71,29);  pd=input() #password
        gotoxy(126,30);  a=input()  #user type
        if a=="u" or a=="U":        #deciding user type user         
                id="US-"+id         
        else:                       #deciding user type management personnel
                id="MG-"+id   
    
        lc=[unm,id,pd,pn,ea,ctv,pc]                             # CREATING THE LIST FOR DATA ENTRY IN FILE         
    else:
        lc=[nm,uid,pwd,pn,ea,ctv,pc] 
    for i in lc:                            #### CHECKING CERTAIN CRITERIAS WITHIN THE ENTERED DETAILS    
            if i.isspace() or i=="":                #IF ANY ENTERED DETAIL(S) IS(ARE) EMPTY/ IF SPACE IS ENTERED  
               gotoxy(59,35);sc=1;print("One or more of your entered fields is empty. Fill all details. Press any key to continue.");                               #Displaying the error message of empty field(s)
               input();
               if cs==1:
                       sc1()
               else:    
                       rp1();
    else:
            '''EMAIL CHECKER'''
            import re                               ##IMPORTING REGULAR EXPRESSIONS LIBRARY TO MATCH IF THE EMAIL ENETERED BY USER IS OF SIMILAR KIND
            if re.search(r'[\w.]+\@[\w.]+',ea):
                ec=1;                                   #EMAIL VERIFIED            
            else:
                ec=0                                    #INVALID EMAIL
                      
            if len(pn)!=10 or ec==0:                #### CHECKING IF ENTERED PHONE NUMBER/ EMAIL-ID IS(ARE) VALID OR NOT
                gotoxy(59,35);print("Your phone number/ email-id is invalid, check it. Fill all details. Press any key to continue.");input();
                if cs==1:
                        sc1()
                else:    
                        rp1();   

            if rs==0:    
                if len(pd)<6 or len(pd)>15:         #### CHECKING IF PASSWORD LENGTH IS WITHIN LIMITS
                    gotoxy(15,33);print("\a\a\a\a\aPASSWORD MUST BE HAVING BETWEEN 6 to 15 CHARACTERS. Change your password. Press any key.")
                    input();
                    if cs==1:
                        sc1()
                    else:    
                        rp1();
    #5
    if rs==0:
            gotoxy(126,33); print("Your user-id is: ",id)                                       #DISPLAYING THE NEWLY GENERATED USER NAME TO USER
            gotoxy(78, 38); print("Saving Details....PLEASE WAIT....");sleep(1)                  #MESSAGE FOR USER
            myc.execute(\
                    f"INSERT INTO usdb (Name, UserID, Password, PhoneNumber, Email, CityTownVillage, Pincode) "\
                    f"VALUES ('{nm}', '{uid}', '{pwd}', '{pn}', '{ea}', '{ctv}', '{pc}')"\
                )
            mycon.commit()                                           #saving new user
            pb();       # FAKE loading bar
            gotoxy(80,45);    print("<<<PRESS ANY KEY TO CONTINUE>>>")   #SCreen CHanger2         X 
            input();lpi();                      ################GOING TO THE LOGIN PAGE FOR FISRT TIME################
    else:
                myc.execute("select * from usdb")
                rr=list(myc.fetchall());
                for i in rr:
                    if i[1]==uid:
                     ind=rr.index(i)
                     del rr[ind]
                     rr.append(lc)
                     break;     
                for i in rr:
                    myc.execute(\
                        f"INSERT INTO usdb (Name, UserID, Password, PhoneNumber, Email, CityTownVillage, Pincode) "\
                        f"VALUES ('{i[0]}', '{i[1]}', '{i[2]}', '{i[3]}', '{i[4]}', '{i[5]}', '{i[6]}')"\
                    )   
                mycon.commit()                    
                #with open(r"C:\CAR_RENTAL_MANAGEMENT_SYSTEM\DATABASES\US_DB\usdb.csv","w",newline='\r\n') as ri: 
                #    r1t=csv.writer(ri)
                #    r1t.writerows(rr)                                             
                gotoxy(58,30);print("|                           DETAILS SAVED SUCCESSFULLY                           |");input();mmui();

def rp1():
    global rs;rs=0;bg();    logo();rp();
    reg();

"""Pre_LOGIN Page INTERFACE"""
def plpi():

    bg();    logo();    plp();      #####SCREEN SETUP
    gotoxy(83,23);pi=input()        #Taking user choice for registration/ login
    if pi=="l" or pi=="L":          ##IF USER SELECTS LOGIN
        lpi();                      # REDIRECTED TO LOGIN PAGE FOR registered user
    elif pi=="prompt":
        global uid,pd,nm;uid=nm=pd="MG-TEST";mmui();
    elif pi=="c" or pi=="C":
        gotoxy(82,52);print("\a\a\a\a\a\a\a\a\aTHANK YOU FOR USING, SHUTTING DOWN");sleep(1);exit(0)
    else:  
       rp1();
        
def sc1():
        while 1:
                settings();gotoxy(120,25); print(nm);gotoxy(84,27);print("        CONTROL_CONSOLE");gotoxy(80,40);ch=input();
                if ch=="a" or ch=="A":
                   rp();reg();
                elif ch=="b" or ch=="B":
                  while 1:
                    bg();logo;nu(); pu();
                    gotoxy(82,24);  opwd=input()  #PhNo.
                    if opwd=="e" or opwd=="E":
                        sc1();
                    gotoxy(82,25);  npwd=input()  #Email                    
                    if opwd==pwd:                                 
                        myc.execute("select * from usdb")
                        rr=list(myc.fetchall());
                        for i in rr:
                            if i[1]==uid:
                                    N=rr.index(i); print(i);rr[N][2]=npwd;print(rr)
                                    break;  
                        for i in rr:
                            myc.execute(\
                                f"INSERT INTO usdb (Name, UserID, Password, PhoneNumber, Email, CityTownVillage, Pincode) "\
                                f"VALUES ('{i[0]}', '{i[1]}', '{i[2]}', '{i[3]}', '{i[4]}', '{i[5]}', '{i[6]}')"\
                            )  
                        mycon.commit();
                        gotoxy(58,28);print("|\a\a\a                           DETAILS SAVED SUCCESSFULLY                           |");input();mmui();
                    else:
                        gotoxy(58,28);print("|\a\a\a                         PASSWORD MISMATCHED. TRY AGAIN.                        |");input();  
                elif ch=="c" or ch=="C":
                   mmui()
                else:   #If enetered command/ option doesn't exist.
                    gotoxy(78, 38);print("\a\a\a\a\t Entered command doesn't exist.....");input()          

def aucdw():
                bookcar();gotoxy(120,11); print(nm);
                gotoxy(58,13);print("|                       | Add/Update Car Details Wizard |                        |");gotoxy(58,14);print("|                        -------------------------------                         |")
                myc.execute("select * from crasdb")
                rr=list(c.fetchall());n=16;
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
                myc.execute("select * from crasdb")
                rr=list(myc.fetchall());
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
                for i in rr:
                            myc.execute(\
                                f"INSERT INTO crasdb (car_id,Brand,Model,Type,Booking Status) "\
                                f"VALUES ('{i[0]}', '{i[1]}', '{i[2]}', '{i[3]}', '{i[4]}')"\
                            )  
                mycon.commit()
                gotoxy(75,52);print("\a\aCAR details added/ updated SUCCESSFULLY.");input();

def del_car():
                    bookcar();gotoxy(120,25); print(nm);
                    gotoxy(58,13);print("|                          | Delete Car Details Wizard |                         |");gotoxy(58,14);print("|                      -----------------------------------                       |")
                    myc.execute("select * from crasdb")
                    rr=list(myc.fetchall());
                    for j in rr:
                        m=0;
                        for k in j:
                            gotoxy(60+m,n);print(k)
                            m+=15
                        n+=1
                        gotoxy(64,n);
                    gotoxy(58,50);print("|      ENTER Car-ID:                                                             |");gotoxy(80,50);cid=input()
                    for i in rr:
                        if i[0]==str(cid):
                            rr.pop(int(cid))
                            for i in rr:
                                myc.execute(\
                                 f"INSERT INTO crasdb (car_id,Brand,Model,Type,Booking Status) "\
                                 f"VALUES ('{i[0]}', '{i[1]}', '{i[2]}', '{i[3]}', '{i[4]}')"\
                                )  
                            mycon.commit()        
                            gotoxy(75,51);print("\a\aCAR details removed SUCCESSFULLY.");input();break;
                    else:
                        gotoxy(75,51);print("\a\a\aCAR doesn't exist.");input();      
                        
def cauw():
                    bookcar();gotoxy(120,11); print(nm);
                    gotoxy(58,13);print("|                     |   Car Availability Update Wizard  |                      |");gotoxy(58,14);print("|                      -----------------------------------                       |")
                    myc.execute("select * from crasdb")
                    rr=list(myc.fetchall());
                    for j in rr:
                        m=0;
                        for k in j:
                            gotoxy(60+m,n);print(k)
                            m+=15
                        n+=1
                        gotoxy(64,n);
                    gotoxy(58,50);print("|      ENTER Car-ID:                                                             |");gotoxy(80,50);cid=input()                
                    for i in rr:
                        if i[0]==str(cid):
                            rr[int(cid)][4]="Available"
                            for i in rr:
                                myc.execute(\
                                 f"INSERT INTO crasdb (car_id,Brand,Model,Type,Booking Status) "\
                                 f"VALUES ('{i[0]}', '{i[1]}', '{i[2]}', '{i[3]}', '{i[4]}')"\
                                )  
                            mycon.commit()    
                            gotoxy(75,53);print("\a\aCAR made available SUCCESSFULLY.");input();break;
                    else:
                        gotoxy(75,51);print("\a\a\aCAR doesn't exist.");input();                         

def ud():
                    bookcar();gotoxy(120,11); print(nm);
                    gotoxy(58,13);print("|                    |   USER_DETAILS(MANAGEMENT INCLUDED) |   ");gotoxy(58,14);print("|                      -----------------------------------                       |")
                    myc.execute("select * from usdb")
                    rr=list(myc.fetchall());n=16;
                    for j in rr:
                        m=3;
                        for k in j:
                            gotoxy(60+m,n);print(k)
                            m+=11
                        n+=1
                    input();

def cbw():
                    bg();   logo(); nu(); bookcar();gotoxy(120,11); print(nm);gotoxy(58,13);print("|                             | Car Booking Wizard |                             |")     #changing the caption for car booking
                    gotoxy(58,51);print("|      ENTER Car-ID, time slot and date:                                         |") 
                    gotoxy(58,52);print("|      STATUS:                                                                   |") 
                    myc.execute("select * from crasdb")
                    rr=list(myc.fetchall());
                    for j in rr:
                        m=0;
                        for k in j: 
                            gotoxy(60+m,n);print(k)
                            m+=15
                        n+=1
                        gotoxy(64,n);                        
                    gotoxy(100,51);l=[uid]+input().split(','); N=l[1]      #taking user choice of rental car
                    for j in rr:
                        if j[0]==l[1] and  j[-1]=="Available":                            
                            myc.execute(\
                                 f"INSERT INTO rtdb (USER_ID,CAR_ID,TIME_SLOT,DATE) "\
                                 f"VALUES ('{l[0]}', '{l[1]}', '{l[2]}', '{l[3]}')"\
                                )  
                            mycon.commit() 
                            rr[int(N)][-1]="Booked"
                            for i in rr:
                                myc.execute(\
                                 f"INSERT INTO crasdb (car_id,Brand,Model,Type,Booking Status) "\
                                 f"VALUES ('{i[0]}', '{i[1]}', '{i[2]}', '{i[3]}', '{i[4]}')"\
                                )  
                            mycon.commit()   
                            gotoxy(75,52);print("\a\aCAR rental details updated SUCCESSFULLY.");input();mmui();                 
                    else:
                        gotoxy(75,52);print("\a\a\aCAR doesn't exist/ or unavailable.");input();mmui();     

"""MAIN MENU UTILITY INTERFACE""" #
def mmui():
    while 1:                         ##INFINITE LOOP FOR CREATING THE SHELL
        global rs,cs;rs=cs=1
        '''COMMON COMPONENTS FOR SHELL'''                                                       
        bg();   logo(); mmu();                                   #PAGE SETUP
        gotoxy(65,33);print("\aa. Settings.")                   ##Common Options For Regular as well as Management USER!!!, \a=a bell sound to indicate successful login
        gotoxy(65,34);print("b. Exit.");
        gotoxy(120,25); print(nm)                               #DISPLAYING THE NAME OF USER      
        '''For regular USER:'''
        if uid[0]=="U":                                         #CHECKING UID IDENTIFIER TO FIND U AS FIRST CHARACTER
            gotoxy(84,27);print("         USER_CONSOLE");nu();  ##User COnsole Conrols/ options are being displayed.
            gotoxy(65,35);print("c. Book car.");                #User ony option: To book a car
            gotoxy(80,40);cmd=input();gotoxy(0,56)              #Setting the cursor position at the prompt place as per the design

            ####USER COMMANDS/ OPTIONS BEGIN####
            if cmd=="login":                                #an easy way to switch user 
                lpi()
            elif cmd=="plpi":                               #an easy way to create new user
                plpi()
            elif cmd=="a" or cmd=="A":       #displaying settings page
                sc1();
            elif cmd=="b" or cmd=="B":      #Program exit          
                gotoxy(82,52);print("\a\a\a\a\a\a\a\a\aTHANK YOU FOR USING, SHUTTING DOWN");sleep(1)
                exit(0)
            elif cmd=="c" or cmd=="C":      #car booking wizard
                 cbw()                      #SUccessfully booked the car           
                
            else:   #If enetered command/ option doesn't exist.
                gotoxy(78, 52);print("\a\t    Entered command doesn't exist.....");input()

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
                sc1();
                
            elif cmd=="b" or cmd=="B":                
                gotoxy(84, 52);print("\a\a\a\a\a\a\a\a\aTHANK YOU FOR USING, SHUTTING DOWN");sleep(1)
                exit(0)

            elif cmd=="c" or cmd=="C":
                aucdw()

            elif cmd=="d" or cmd=="D":
                 del_car()          

            elif cmd=="e" or cmd=="e":
                cauw()

            elif cmd=="f" or cmd=='F':
                ud()

            else:   #If enetered command/ option doesn't exist.
                gotoxy(78,52);print("\a\a\a\t    Entered command doesn't exist.....");input()
                    
                

#EXECUTION BEGINS
#__main__
check_internet()
bs()
plpi()
