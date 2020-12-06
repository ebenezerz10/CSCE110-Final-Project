#mainmenu 

import csv
import sys
import os
import pathlib

# Global Variable 
uin = []
lab_m = []
exam_m = []
quiz_m = []
ra_m = []
score = []
grade = []
counter = 0
project = []
student_report= []

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
    elif choice == "2" or choice == "2.":
        s_report()
    elif choice == "3" or choice == "3.":
        s_charts()  
    elif choice == "4" or choice == "4.":
        c_report()   
    elif choice == "5" or choice == "5.":
        c_charts()   
    elif choice == "6" or choice == "6." or choice == "q" or choice == "quit":
        sys.exit 
        #we might change this to break
    else: 
        print("You must select an option 1-6")
        print("Please try again")
        menu()
        
def read():
    data = input("Please enter the path and name of your CSV file: ")
    #noah's path 
    #C:\Users\noahw\OneDrive\Desktop\CSCE 110\Project\Data\grades.csv
    #eb's path 
    #C:\Users\ebenezerz10\Documents\GitHub\CSCE110-Final-Project
    with open (data) as f:
        data = csv.reader(f)  # reads file
        next(data, None)
        for row in data:
            student_report = row[0:23]
            #print(student_report)  
            uin = row[0]
            lab_m = row[1:7]
            quiz_m = row[6:13]
            ra_m = row[12:19]
            exam_m = row[18:22]
            project = row [22:23]
            res = [int(float(i)) for i in lab_m]
            lab_f = sum(res)/len(res)
            #print(round(lab_f,1))
    return student_report, uin, lab_m, quiz_m, ra_m, exam_m, project, res, lab_f
    
    is_there_data == 1
        
def s_report():
    while True:
        student = input("Please enter the UIN of the student you would like to general a report for: ")
        if student.isdigit() and len(student) == 10:
            print("This is a valid UIN") 
            break
        #add to make sure it checks to see if the UIN is in the data
        else:
            print("This is not valid")
            student = input("Please enter the UIN of the student you would like to general a report for: ") 
    txt = open(f"{student}.txt","w+")
    txt.write("Exams mean: {}\nLab mean: {}\nQuizzes mean: {}\nReading activites mean: {}\n".format(exam_m,lab_m,quiz_m,ra_m))
    print("Your report has been created as a .txt file")
    #need to add score and letter grade
    txt.close
    
def s_charts():
    pass

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
    pass
    

def c_charts():
    pass

main()