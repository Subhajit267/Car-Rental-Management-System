"""WELCOME TO CAR MANAGEMENT VERSION 1.10"""
'''
    This is setup script for installing CRMS
    Author: SUBHAJIT HALDER 
       DATE: 12/01/2024
'''

"""Importing os,sys and my modules to gain access to system commands and the visual elements and string tables."""

"""File Imports"""
import os,sys,csv
"""THIS MODULE IS CREATED TO DEFINE ALL VISUAL ELEMENTS FOR THE PROGRAM"""  

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
    print()
    print(" ","="*186," ",)
    for i in range(1,53):                                               #instead of printing 52 times a same statement to create border loop is used
        print("|"," "*186,"|")
    print(" ","="*186," ")
    gotoxy(0,3);print("|"+" "*82+"CAR RENTAL MANAGEMENT SYSTEM"+" "*75,"  |")  #name
    gotoxy(0,4);print("|"+" "*82+"--- ------ ---------- ------"+" "*75,"  |")  #name
    gotoxy(0,6);print("|"+" "*82+"BETA 1, Ver:2.02, INST_BUILD"+" "*75,"  |")  #version
    gotoxy(0,7);print("|"+" "*82+"~~~~ ~~ ~~~~~~~~~ ~~~~~~~~~~"+" "*75,"  |")  #name
    

"""Logo"""
def logo():#LOGO OF THE PROGRAM, displaying the shortform as an ASCII ART
    gotoxy(1,1);gotoxy(1,1);gotoxy(1,1);gotoxy(1,1);gotoxy(1,1) #providing fixed co ordinates for each ine of the logo as throught the code it remains at the same position.
    gotoxy(15,24);print(".------------------------------.")
    gotoxy(15,25);print("| ----    ---   -     -  .---- |")
    gotoxy(15,26);print("||       |   |  |\   /|  |     |")
    gotoxy(15,27);print("||       .---   | \ / |   ----.|")
    gotoxy(15,28);print("||       | \    |  -  |       ||")
    gotoxy(15,29);print("| ---- . |  \ . |     | . ----.|")
    gotoxy(15,30);print(".------------------------------.")

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

from time import *
"""STRING FILE"""
"""THIS FILE IS CREATED TO STORE EVERY SORT OF INSTRUCTIONS AND DEATILS TO BE SHOWN TO THE  USER"""
#This file contains the forms and other piece of info displayed to the user during the installation.

#from looks import gotoxy#Importing gotoxy only from looks to change the cursor position

"""Function used to display the instructions"""
def inst():
    gotoxy(58,19);print(" -------------------------------------------------------------------------------- ")
    gotoxy(58,20);print("|  WELCOME TO THE INSTALLER OF CAR RENTAL MANAGEMENT SYSTEM. ENTER THE DEATILS:  |")
    gotoxy(58,21);print(" -------------------------------------------------------------------------------- ")
    gotoxy(58,22);print("|                                                                                |")
    gotoxy(58,23);print("|                    Are you a user or a management personnel?                   |")
    gotoxy(58,24);print("|                                                                                |")
    gotoxy(58,25);print("| HELP ME DECIDE:                                                                |")
    gotoxy(58,26);print("|  ---------------------------------------------------------------------------   |")
    gotoxy(58,27);print("| |If you just wish to use/ book cars for personal use choose user by pressing|  |")
    gotoxy(58,28);print("| |'u'. Ifyou work in our organisation and need to update/ modify/ delete/ add|  |")
    gotoxy(58,29);print("| |car details   choose management by pressing 'm'. This software allows to   |  |")
    gotoxy(58,30);print("| |create multiple accounts for different users or management personnel.      |  |")
    gotoxy(58,31);print("|  ---------------------------------------------------------------------------   |")
    gotoxy(58,32);print("|                                                                                |")
    gotoxy(58,33);print("| ######YOU ARE ADVICED TO USE A STRONG PASSWORD TO PREVENT DATA BREACH.######   |")
    gotoxy(58,34);print("|                                                                                |")
    gotoxy(58,35);print("|     Enter You choice:                                                          |")
    gotoxy(58,36);print(" -------------------------------------------------------------------------------- ")   

"""Function to take user details"""    
def UD():
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
    gotoxy(58,30);print("|                                                                                |")
    gotoxy(58,31);print(" -------------------------------------------------------------------------------- ")     
    
"""Function to display installation success and providing some general info regarding the program and its location."""
def ST():
    gotoxy(58,19);print(" -------------------------------------------------------------------------------- ")
    gotoxy(58,20);print("|  INSTALLATION STATUS:                                                          |")
    gotoxy(58,21);print(" -------------------------------------------------------------------------------- ")
    gotoxy(58,22);print("|                                                                                |")
    gotoxy(58,23);print("|  Installed successfully.                                                       |")
    gotoxy(58,24);print("|  Open C:\Car_rental_management_system\crms.exe to access the program. You may  |")
    gotoxy(58,25);print("|  right click on the program and create desktop shortcut for ease in access.    |")
    gotoxy(58,26);print("|                                                                                |")
    gotoxy(58,27);print("|  !!!ENJOY USING THE PROGRAM!!!                                                 |")
    gotoxy(58,28);print("|                                                                                |")
    gotoxy(58,29);print("|  To uninstall the program use unist.exe                                        |")    
    gotoxy(58,30);print("|                                                                                |")
    gotoxy(58,31);print(" -------------------------------------------------------------------------------- ")   

       

def scr1(): #Loading screen of program
    bg();    logo();        #Adding the visual elements like the logo border and the progress bar
    if os.path.isdir("C:\\CAR_RENTAL_MANAGEMENT_SYSTEM\\DATABASES"):
        os.system("color cf");
        gotoxy(58,19);print(" -------------------------------------------------------------------------------- ");os.system("color cf")
        gotoxy(58,20);print("| !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!WARNING!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! |");os.system("color cf")
        gotoxy(58,21);print(" -------------------------------------------------------------------------------- ");os.system("color cf")
        gotoxy(58,22);print("|  This computer already has a version of Car Rental Management System installed |");os.system("color cf")
        gotoxy(58,23);print("|  If you proceed with the installation the previous version would be replaced.  |");os.system("color cf")
        gotoxy(58,24);print("|  Do You wish to continue?                                                      |");os.system("color cf")
        gotoxy(58,25);print(" -------------------------------------------------------------------------------- ");os.system("color cf")
        gotoxy(85,24);os.system("color cf");a=input();
        if a=="N" or a=="n":
            gotoxy(76,45);os.system("color cf");   print("<<<PRESS ANY KEY TO EXIT>>>");os.system("color cf");#SCreen CHanger
            gotoxy(0,56);   input()         
            exit(0)
        pb()
        gotoxy(80,45);    print("<<<PRESS ANY KEY TO CONTINUE>>>")   #SCreen CHanger
        gotoxy(0,56);   input();os.system("color 4f");
    else:
        pb()
        gotoxy(80,45);    print("<<<PRESS ANY KEY TO CONTINUE>>>")   #SCreen CHanger
        gotoxy(0,56);   input();#Waiting for user input to change the screen

def scr2():# USER TYPE DETERMINER
    bg();    logo();   inst()   #Adding the page setup
    if os.path.isdir("C:\\CAR_RENTAL_MANAGEMENT_SYSTEM\\DATABASES"):
         os.system("color 4f");
    gotoxy(83,35);global a;  a=input() #Taking input to determine the type of account to be created. USER_ID starts with  US-XXXX and Management as MG-XXXX
    pb()                        #casual progress bar to add a classy look
    sleep(0.75)                 #Auto screen change

def scr3():
    bg();    logo();    UD()    #adding the page setup
    if os.path.isdir("C:\\CAR_RENTAL_MANAGEMENT_SYSTEM\\DATABASES"):
         os.system("color 4f");
    gotoxy(67,23);  nm=input()  #NAME
    gotoxy(94,24);  id=input()  #ID
    gotoxy(75,25);  pn=input()  #PhNo.
    gotoxy(76,26);  ea=input()  #Email
    gotoxy(83,27);  ctv=input() #city/town/village
    gotoxy(71,28);  pc=input()  #pincode
    gotoxy(71,29);  pwd=input() #password
    ad={"CITY/ TOWN / VILLAGE:":ctv,"PIN CODE": pc} # ADDRESS DETAILS ALLTOGETHER;
    lc=[nm,id,pn,ea,ctv,pc,pwd];
    #email checker
    import re
    if re.search(r'[\w.]+\@[\w.]+',ea):
        ec=1;
    else:
        ec=0
    if a=="u" or a=="U":
        id="US-"+id
    else:
        id="MG-"+id
    gotoxy(124,33); print("Your user-id is: ",id)
    for i in lc:
        if i.isspace() or i=="":
           gotoxy(15,33);print("One or more of your entered fields is empty. Fill all details. Press any key to continue.");input();scr3();
    else:
        sc=0           
    if len(pn)!=10 or ec==0:
        gotoxy(15,33);print("Your phone number/ email-id is invalid, check it. Fill all details. Press any key to continue.");input();scr3();
       
    if len(pwd)>=6 and len(pwd)<=15 and ec==1:
        for i in lc:
            if i.isspace() or i=="":
               gotoxy(15,33);print("One or more of your entered fields is empty. Fill all details. Press any key to continue.");input();scr3();
        else:
            sc=0
            gotoxy(15,33);gotoxy(124,33); print("Your user-id is: ",id)
            os.system("mkdir C:\\CAR_RENTAL_MANAGEMENT_SYSTEM");gotoxy(15,34)
            os.system("xcopy .\\RESOURCES C:\\CAR_RENTAL_MANAGEMENT_SYSTEM /s /e /v");gotoxy(15,35)
            gotoxy(78, 38);print("Saving Details. Copying Files....");sleep(1)
            with open(r"C:\CAR_RENTAL_MANAGEMENT_SYSTEM\databases\us_db\usdb.csv","w") as f:
                fw=csv.writer(f)
                fw.writerow(['Name','ID','Password','Email','Ph No.','Address'])
                fw.writerow([nm,id,pwd,ea,pn,ad])
            os.system(r"shortcut.exe /f:""%homedrive%%homepath%\desktop\CRMS.lnk"" /a:c /t:C:\CAR_RENTAL_MANAGEMENT_SYSTEM\crms_main.exe")
            pb();                                           # FAKE loading bar
            gotoxy(80,45);    print("<<<PRESS ANY KEY TO CONTINUE>>>")   #SCreen CHanger
            input();scr4()
        
        
def scr4():
    bg();    logo();    ST()    #adding the page setup
    if os.path.isdir("C:\\CAR_RENTAL_MANAGEMENT_SYSTEM\\DATABASES"):
         os.system("color 4f");
    gotoxy(84,45);    print("<<<PRESS ANY KEY TO EXIT>>>")   #SCreen CHanger
    gotoxy(0,56);   input(); exit(0); #Waiting for user input to change the screen


#EXECUTION BEGINS
#__main__
scr1()
scr2()
scr3()


