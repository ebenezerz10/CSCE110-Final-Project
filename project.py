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
    else: 
        print("You must select an option 1-6")
        print("Please try again")
        menu()
        
def read():
    global student_report, uin, lab_m, quiz_m, ra_m, exam_m, project
    data = input("Please enter the path and name of your CSV file: ")
    #noah's path 
    #C:\Users\noahw\OneDrive\Desktop\CSCE 110\Project\Data\grades.csv
    #eb's path 
    #C:\Users\ebenezerz10\Documents\GitHub\CSCE110-Final-Project
    with open (data) as f:
        data_read = csv.reader(f)  # reads file
        next(data_read, None)
        for row in data_read:
            student_report.append(row[0:23])
            uin.append(row[0])
            lab_m.append(row[1:7])
            quiz_m.append(row[6:13])
            ra_m.append(row[12:19])
            exam_m.append(row[18:22])
            project.append(row [22:23])
        menu()
        return student_report, uin, lab_m, quiz_m, ra_m, exam_m, project     
       
def s_report():
    student = input("Please enter the UIN of the student you would like to general a report for: ")
    if student in uin:
        print("This is a valid UIN")
    else: 
        print("This is not valid")
    txt = open(f"{student}.txt","w+")
    print("Text file opened")
    for row in student_report:
        if student == row[0]:
            #uin_for_row = row[0]
            total = 0
            lab_total = 0
            quiz_total = 0
            reading_total = 0
            exam_total = 0
            project_total = 0 
            for index in range(1,6):
                thisGrade = float(row[index])
                lab_total = lab_total + thisGrade
                total = total + lab_total * .25
                lab_mean = lab_total / 6
            for index in range(7,12):
                thisGrade = float(row[index])
                quiz_total = quiz_total + thisGrade
                total = total + quiz_total * .1
                quiz_mean = quiz_total / 6
            for index in range(13,19):
                thisGrade = float(row[index])
                reading_total = reading_total + thisGrade
                total = total + reading_total * .1
                reading_mean = reading_total / 6
            for index in range(20,22):
                thisGrade = float(row[index])
                exam_total = exam_total + thisGrade
                total = total + exam_total * .45
                exam_mean = exam_total / 3
            for index in range(20,22):
                thisGrade = float(row[index])
                project_total = project_total + thisGrade
                total = total + project_total * .1
            total = total / 10
            total = round(total, 1)
            exam_mean = round(exam_mean, 1)
            lab_mean = round(lab_mean, 1)
            quiz_mean = round(quiz_mean, 1)
            reading_mean = round(reading_mean, 1)
            if total >= 90:
                letter_grade = "A"
            elif 80 <= total < 90:
                letter_grade = "B"
            elif 70 <= total < 80:
                letter_grade = "C"
            elif 60 <= total < 70:
                letter_grade = "D"
            else:
                letter_grade = "F"
            txt.write("Exams mean: {}\nLab mean: {}\nQuizzes mean: {}\nReading activites mean: {}\nScore: {}%\nLetter grade: {}\n".format(exam_mean, lab_mean, quiz_mean, reading_mean, total, letter_grade))	           
            #txt.write(total, lab_total, quiz_total, reading_total, exam_total, project_total)
            txt.close
            print("Your report has been created as a .txt file")
    #need to add score and letter grade
    
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

menu()