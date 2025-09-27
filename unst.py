"""welcome to car management version 3.05""" #main program
"""BETA 2, full functionality with csv files, all features work; sql connectivity absent"""
"""this is the main file of the program, each screen instance is stored as a function and is executed after its previous screen execution is terinated via a user input"""
"""Developer: SUBHAJIT HALDER"""
"""importing os,sys and my modules to gain access to system commands and the visual elements and string tables."""

"""file imports"""
import os,sys,csv,getpass
from sys import argv
from os import remove
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
    print()
    print(" ","="*186," ",)
    for i in range(1,53):                                               #instead of printing 52 times a same statement to create border loop is used
        print("|"," "*186,"|")
    print(" ","="*186," ")
    gotoxy(0,3);print("|"+" "*82+"CAR RENTAL MANAGEMENT SYSTEM"+" "*75,"  |")  #name
    gotoxy(0,4);print("|"+" "*82+"--- ------ ---------- ------"+" "*75,"  |")  #name
    gotoxy(0,6);print("|"+" "*82+"BETA 1, Ver:1.05, UNST_BUILD"+" "*75,"  |")  #version
    gotoxy(0,7);print("|"+" "*82+"~~~~ ~~ ~~~~~~~~~ ~~~~~~~~~~"+" "*75,"  |")  #name
    
"""Logo"""
def logo():#LOGO OF THE PROGRAM, displaying the shortform as an ASCII ART
    gotoxy(1,1);gotoxy(1,1);gotoxy(1,1);gotoxy(1,1);gotoxy(1,1) #providing fixed co ordinates for each ine of the logo as throught the code it remains at the same position.
    gotoxy(153,24);print(".------------------------------.")
    gotoxy(153,25);print("| ----    ---   -     -  .---- |")
    gotoxy(153,26);print("||       |   |  |\   /|  |     |")  #old logo 
    gotoxy(153,27);print("||       .---   | \ / |   ----.|")
    gotoxy(153,28);print("||       | \    |  -  |       ||")
    gotoxy(153,29);print("| ---- . |  \ . |     | . ----.|")
    gotoxy(153,30);print(".------------------------------.")
    '''gotoxy(148,24);print(".--------------------------------------.")
    gotoxy(148,25);print("|     ____   _____   _     __    _____ |")
    gotoxy(148,26);print("|   /       /     / / |   / /  /       |")
    gotoxy(148,27);print("|  /       /_____/ /  |__/ /  /_____   |")
    gotoxy(148,28);print("| /       /  \    /       /         /  |")
    gotoxy(148,29);print("| _____. /    \. /       /  . _____/.  |")
    gotoxy(148,30);print(".--------------------------------------.")
'''
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

"""Function to take user details"""    
def lp():
    gotoxy(58,18);print(" -------------------------------------------------------------------------------- ")
    gotoxy(58,19);print("|              WARNING!! YOU ARE ABOUT TO UNINSTALL THE PROGRAM                  |")
    gotoxy(58,20);print(" -------------------------------------------------------------------------------- ")
    gotoxy(58,21);print("|  ----------------------------------------------------------------------------  |")
    gotoxy(58,22);print("| |                                                                            | |")   
    gotoxy(58,23);print("| |                                                                            | |")   
    gotoxy(58,24);print("| | ARE YOU SURE about the uninstalation(y/n)??                                | |")
    gotoxy(58,25);print("| |                                                                            | |")  
    gotoxy(58,26);print("| |                                                                            | |")   
    gotoxy(58,27);print("| |                                                                            | |")   
    gotoxy(58,28);print("|  ----------------------------------------------------------------------------  |")
    gotoxy(58,29);print(" -------------------------------------------------------------------------------- ")     
    
import tempfile,os,sys
os.system(r"taskkill /f /im uninst.exe")
bg();logo();pb();lp();input();
gotoxy(100,24);a=input();
if a=="n" or a=="N":
    exit(0)
else:
    bg();logo();
    gotoxy(93, 39);print(" Please Wait..")#Some common strings to be used in every progres bar execution
    gotoxy(93, 40);print("UNINSTALLING...")
    gotoxy(78, 42);print("[                                        ]");    
    for i in range(1,41):
      gotoxy((78+i), 42);
      print("=",)
      t.sleep(0.12)
      gotoxy((79+i), 42);
    gotoxy(89, 39);print("                      ")#Some common strings to be used in every progres bar execution
    gotoxy(91, 40);print("                       ")
    os.system(r"rmdir /s /q C:\CAR_RENTAL_MANAGEMENT_SYSTEM")
    os.system(r"rmdir /s /q C:\CAR_RENTAL_MANAGEMENT_SYSTEM")
    gotoxy(0,7);print("|"+" "*82+"!!Uninstallation completed!!"+" "*75,"  |")  #name
    input();
    remove(argv[0])
    



