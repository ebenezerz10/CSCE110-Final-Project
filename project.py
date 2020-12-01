#mainmenu 

import csv
import sys

def main():
    menu()
    
def menu():
    print("*******************Main Menu*****************")
    print("1. Read CSV file of grades")
    print("2. Generate student report file")
    print("4. Generate class report file")
    print("5. Generate class report charts")
    print("6. Quit")
    print("************************************************")
    
    choice = input("Please chose your option: ")
    
    if choice == "1" or choice == "1.":
        read()
        #Eb
        #read csv file code
    if choice == "2" or choice == "2.":
        s_report()
        #n
    if choice == "3" or choice == "3.":
        s_charts()   
    if choice == "4" or choice == "4.":
        c_report()   
    if choice == "5" or choice == "5.":
        c_charts()     
    if choice == "6" or choice == "6.":
        sys.exit
        #we might want to chose another option
    else: 
        print("You must select an option 1-6")
        print("Please try again")
        menu()
        
def read():
    student_file = open('grades.csv', 'r')
    print("Check")
##def s_report():

##def s_charts():

###def c_report():

##def c_charts():
def main():
    menu()
    
def menu():
    print("*******************Main Menu*****************")
    print("1. Read CSV file of grades")
    print("2. Generate student report file")
    print("4. Generate class report file")
    print("5. Generate class report charts")
    print("6. Quit")
    print("************************************************")
    
    choice = input("Please chose your option: ")
    
    if choice == "1" or choice == "1.":
        read()
        #Eb
        #read csv file code
    if choice == "2" or choice == "2.":
        s_report()
        #n
    if choice == "3" or choice == "3.":
        s_charts()   
    if choice == "4" or choice == "4.":
        c_report()   
    if choice == "5" or choice == "5.":
        c_charts()     
    if choice == "6" or choice == "6.":
        sys.exit
        #we might want to chose another option
    else: 
        print("You must select an option 1-6")
        print("Please try again")
        menu()
        
def read():
 student_file = open('grades.csv', "r")
 profile_list = student_file.readlines()
 print(student_file)
main()
