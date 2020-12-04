#mainmenu 

import csv
import sys
#import numpy as np
#import pandas as pd

#### Global Variable 
uin = []
lab_m = []
exam_m = []
quiz_m = []
ra_m = []
score = []
grade = []
counter = 0
project = []

def main():
    menu()
    
def menu():
    print("*******************Main Menu*****************")
    print("1. Read CSV file of grades")
    print("2. Generate student report file")
    print("3. Generate student report charts")
    print("4. Generate class report file")
    print("5. Generate class report charts")
    print("6. Quit")
    print("************************************************")
    
    choice = input("Please chose your option: ")
    
    if choice == "1" or choice == "1.":
        read()
        #Eb
        #read csv file code
    elif choice == "2" or choice == "2.":
        s_report()
    elif choice == "3" or choice == "3.":
        s_charts()   
    elif choice == "4" or choice == "4.":
        c_report()   
    elif choice == "5" or choice == "5.":
        c_charts()     
    elif choice == "6" or choice == "6.":
        sys.exit
        #we might want to chose another option
    else: 
        print("You must select an option 1-6")
        print("Please try again")
        menu()
        
def read():
    with open ('grades.csv','rt') as f:
        data = csv.reader(f)  # reads file
        next(data, None)
        for row in data:  #### indexes data 
            uin = row[0]
            print(uin)
            lab_m = row[1:7]
            quiz_m = row[6:13]
            ra_m = row[12:19]
            exam_m = row[18:22]
            project = row [22:23]
            #print()

            

def s_report():
    uin = input("Please enter the UIN of the student you would like to general a report for: ")
    #e_mean = 
    #l_mean = 
    #q_mean = 
    #r_mean = 
    #score = 
    #grade = 
    print("Exam mean: ")
    print("Labs mean: ")
    print("Quizzes mean: ")
    print("Reading activties mean: ")
    print("Score: ")
    print("Letter grade: ")
    
##def s_charts():

def c_report():
    #tot = 
    #min = 
    #max = 
    #med = 
    #mean = 
    #std = 
    print("Total numebr of students: ")
    print("Minimum score: ")
    print("Maximum score: ")
    print("Medium score: ")
    print("Mean score: ")
    print("Standard deviation: ")
    

##def c_charts():

main()
