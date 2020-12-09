#mainmenu

import csv
import sys
import os
import pathlib
import matplotlib.pyplot as plt
#import matplotlib.pyplot as plt;plt.rcdefaults()
import numpy as np

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
student_report = []
read_check = 0

def main():
    menu()

def menu():
    global read_check
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
        if read_check == "1":
            s_report()
        else: 
            print("Data has not been read")
            menu()
    elif choice == "3" or choice == "3.":
        if read_check == "1":
            s_charts()
        else: 
            print("Data has not been read")
            menu()
    elif choice == "4" or choice == "4.":
        if read_check == "1":
            c_report()
        else: 
            print("Data has not been read")
            menu()
    elif choice == "5" or choice == "5.":
        if read_check == "1":
            c_charts()
        else: 
            print("Data has not been read")
            menu()
    elif choice == "6" or choice == "6." or choice == "q" or choice == "quit":
        sys.exit
    else:
        print("You must select an option 1-6")
        print("Please try again")
        menu()

def read():
    global student_report, uin, lab_m, quiz_m, ra_m, exam_m, project, read_check, data, counter
    data = input("Please enter the path and name of your CSV file: ")
    # noah's path
    # C:\Users\noahw\OneDrive\Desktop\CSCE 110\Project\Data\grades.csv
    # eb's path
    # C:\Users\ebenezerz10\Documents\GitHub\CSCE110-Final-Project\grades.csv
    #other computer
    #C:\Users\15-aq267cl\OneDrive\Documents\GitHub\CSCE110-Final-Project/grades.csv
    with open(data) as f:
        read_check = "1"
        data_read = csv.reader(f)  # reads file
        next(data_read, None)
        for row in data_read:
            counter = counter + 1
            student_report.append(row[0:23])
            uin.append(row[0])
            lab_m.append(row[1:7])
            quiz_m.append(row[6:13])
            ra_m.append(row[12:19])
            exam_m.append(row[18:22])
            project.append(row[22:23])
        menu()
        return student_report, uin, lab_m, quiz_m, ra_m, exam_m, project, read_check, data, counter
def s_report():
    student = input("Please enter the UIN of the student you would like to general a report for: ")
    if student in uin:
        print("This is a valid UIN")
    else:
        print("This is not valid")
    txt = open(f"{student}.txt", "w+")
    print("Text file opened")
    for row in student_report:
        if student == row[0]:
            # uin_for_row = row[0]
            total = 0
            lab_total = 0
            quiz_total = 0
            reading_total = 0
            exam_total = 0
            project_total = 0
            for index in range(1, 6):
                thisGrade = float(row[index])
                lab_total = lab_total + thisGrade
                total = total + lab_total * .25
                lab_mean = lab_total / 6
            for index in range(7, 12):
                thisGrade = float(row[index])
                quiz_total = quiz_total + thisGrade
                total = total + quiz_total * .1
                quiz_mean = quiz_total / 6
            for index in range(13, 19):
                thisGrade = float(row[index])
                reading_total = reading_total + thisGrade
                total = total + reading_total * .1
                reading_mean = reading_total / 6
            for index in range(20, 22):
                thisGrade = float(row[index])
                exam_total = exam_total + thisGrade
                total = total + exam_total * .45
                exam_mean = exam_total / 3
            for index in range(20, 22):
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
            txt.write(
                "Exams mean: {}\nLab mean: {}\nQuizzes mean: {}\nReading activites mean: {}\nScore: {}%\nLetter grade: {}\n".format(
                    exam_mean, lab_mean, quiz_mean, reading_mean, total, letter_grade))
            txt.close
            print("Your report has been created as a .txt file")
            menu()
    print(total)

def s_charts():
    student = input("Please enter the UIN of the student you would like to general a report for: ")
    if student in uin:
        print("This is a valid UIN")
    else: 
        print("This is not valid")
    for row in student_report:
        if student == row[0]:
            current_directory = os.getcwd()
            uin_directory = os.path.join(current_directory, f"{student}")
            if not os.path.exists(uin_directory):
                os.makedirs(uin_directory)
            #bar chart of labs
            x_label = ['Lab 1', 'Lab 2', 'Lab 3', 'Lab 4', 'Lab 5', 'Lab 6']
            y_amount = row[1:7]
            new_y_amount = [int(float(num)) for num in y_amount]
            y_pos = np.arange(len(x_label))
            print("Labs")
            print(row)
            print(y_amount)
            #plt.bar(y_pos, y_amount, align='center', alpha=0.5)
            plt.bar(x_label, new_y_amount)#, color='blue', align='center', alpha=0.5)
            plt.xticks(y_pos, x_label)
            plt.ylabel('Grade')
            plt.xlabel('Lab Assignments')
            plt.title('Bar chart of labs')
            plt.show()
            plt.savefig(f"{uin_directory}/Labs Bar Chart.png")
            print('Lab Bar Chart Saved')
            plt.clf()

            #bar chart of quizzes
            x_label = ('Quiz 1', 'Quiz 2', 'Quiz 3','Quiz 4','Quiz 5','Quiz 6')
            y_amount = row[7:13]
            new_y_amount = [int(float(num)) for num in y_amount]
            y_pos = np.arange(len(x_label))
            print("Quizes")
            print(row)
            print(y_amount)
            #plt.bar(y_pos, y_amount, align='center', alpha=0.5)
            plt.bar(x_label, new_y_amount)#, color='blue', align='center', alpha=0.5)
            plt.xticks(y_pos, x_label)
            plt.ylabel('Grade')
            plt.xlabel('Quiz Assignments')
            plt.title('Bar chart of quizs')
            plt.show()
            plt.savefig(f"{uin_directory}/Quizs Bar Chart.png")
            print('Lab Bar Chart Saved')
            plt.clf()

            #bar chart of reading activties
            x_label = ('RA 1', 'RA 2', 'RA 3','RA 4','RA 5','RA 6')
            y_amount = row[13:19]
            new_y_amount = [int(float(num)) for num in y_amount]
            y_pos = np.arange(len(x_label))
            print("RA")
            print(row)
            print(y_amount)
            #plt.bar(y_pos, y_amount, align='center', alpha=0.5)
            plt.bar(x_label, new_y_amount)#, color='blue', align='center', alpha=0.5)
            plt.xticks(y_pos, x_label)
            plt.ylabel('Grade')
            plt.xlabel('Reading Activities')
            plt.title('Bar chart of Reading Activties')
            plt.show()
            plt.savefig(f"{uin_directory}/Reading Activities Bar Chart.png")
            print('Lab Bar Chart Saved')
            plt.clf()

            #bar chart of exams
            x_label = ('Exam 1', 'Exam 2', 'Exam 3')
            y_amount = row[19:22]
            new_y_amount = [int(float(num)) for num in y_amount]
            y_pos = np.arange(len(x_label))
            print("Exams")
            print(row)
            print(y_amount)
            #plt.bar(y_pos, y_amount, align='center', alpha=0.5)
            plt.bar(x_label, new_y_amount)#, color='blue', align='center', alpha=0.5)
            plt.xticks(y_pos, x_label)
            plt.ylabel('Grade')
            plt.xlabel('Exam #')
            plt.title('Bar chart of Exams')
            plt.show()
            plt.savefig(f"{uin_directory}/Exams Bar Chart.png")
            print('Lab Bar Chart Saved')
            plt.clf()
    menu()

def c_report():
    res = []
    for row in student_report:
        score_total = 0

        # uin_for_row = row[0]
        total = 0
        lab_total = 0
        quiz_total = 0
        reading_total = 0
        exam_total = 0
        project_total = 0
        for index in range(1, 7):
            thisGrade = float(row[index])
            lab_total = lab_total + thisGrade
            res_total = lab_total/600
            sub_total = res_total*100
            sub_total = round(sub_total,1)
            total = sub_total * .25
            lab_mean = lab_total / 6
        l_total = total
        for index in range(7, 13):
            thisGrade = float(row[index])
            quiz_total = quiz_total + thisGrade
            res_total = quiz_total/600
            sub_total = res_total*100
            sub_total = round(sub_total,1)
            total = sub_total * .1
            quiz_mean = quiz_total / 6
        q_total = total
        for index in range(13, 19):
            thisGrade = float(row[index])
            reading_total = reading_total + thisGrade
            res_total = reading_total/600
            sub_total = res_total*100
            sub_total = round(sub_total,1)
            total = sub_total * .1
            reading_mean = reading_total / 6
        r_total = total
        for index in range(19, 22):
            thisGrade = float(row[index])
            exam_total = exam_total + thisGrade
            res_total = exam_total/300
            sub_total = res_total*100
            sub_total = round(sub_total,1)
            total = sub_total * .45
            exam_mean = exam_total 
        e_total = total
        for index in range(22,23):
            thisGrade = float(row[index])
            project_total = project_total + thisGrade
            res_total = project_total/100
            sub_total = res_total*100
            sub_total = round(sub_total,1)
            total = sub_total * .1
            #print(thisGrade)
        p_total = total
        new_total = l_total+q_total+r_total+e_total+p_total
        score_total = "%.1f" % new_total
        res.append(score_total)
    res_min = min(float(sub) for sub in res) 
    res_max = max(float(sub) for sub in res) 
    n = len(res) 
    res.sort() 
    
    if n % 2 == 0: 
        median1 =float(res[n//2])
        median2 = float(res[n//2 - 1])
        median = (median1 + median2)/2
    else: 
        median = res[n//2] 
    get_sum = sum(map(float,res))
    mean = get_sum / n
    #std =
    print("Total numebr of students: {}".format(counter))
    print("Minimum score: {}".format(res_min))
    print("Maximum score: {}".format(res_max))
    print("Medium score: {}".format(median))
    print("Mean score: {}".format(round(mean,1)))
    print("Standard deviation: {}")

def c_charts():
    pass

menu()

"""  
l = 477.5  79.6  19.9
q = 422    70.3  7.03
r = 464.25   77.4  7.74
e = 170.5    56.8  25.56
p = 88       8.8   .88"""