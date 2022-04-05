import curses
import math
import numpy as np

class Student:
    def __init__(self, test, sid, name, dob, gpa = 0):
        self.__sid = sid
        self.__name = name
        self.__dob = dob
        self.__gpa = gpa 
        test.students.append(self)

    def get_sid(self):
        return self.__sid

    def get_name(self):
        return self.__name

    def get_dob(self):
        return self.__dob
    def get_gpa(self):
        return self.__gpa

    def set_gpa(self, gpa):
        self.gpa = gpa 

class Course:
    def __init__(self, test, cid, name, credit):
        self.__cid = cid
        self.__name = name
        self.__credit = credit
        test.courses.append(self)

    def get_cid(self):
        return self.__cid

    def get_name(self):
        return self.__name
    def get_credit(self):
        return self.__credit


class Mark:
    def __init__(self, test, sid, cid, mark):
        self.__sid = sid
        self.__cid = cid
        self.__mark = mark
        test.marks.append(self)

    def get_sid(self):
        return self.__sid

    def get_cid(self):
        return self.__cid

    def get_mark(self):
        return self.__mark

class test_oop:
    students = []
    courses = []
    marks = []
    
    def listStudent (self) :
        print(students)

    def listCourse (self) :
        print(courses)
    
    def listMark (self):
        print(marks)
    
    def calculate_student_gpa(self, numStudent, numCour):
        screen.addstr("Input the id of the student you want to calculate gpa")
        screen.refresh()
        sid_temp = int(screen.getstr().decode())
        total_credit = 0
        total_mark = 0
        for students in self.students:
            if students.get_sid() == sid_temp:
                for marks in self.marks:
                    if marks.get_sid() == sid_temp:
                        for courses in self.courses:
                            if courses.get_cid() == marks.get_cid():
                                total_credit = total_credit + courses.get_credit()
                                total_mark = total_mark + courses.get_mark()*courses.get_credit()
                gpa = float(total_mark/total_credit)
                students.set_gpa(gpa)

    def start (self):  
        screen.addstr("Input the number of students\n")
        screen.refresh()
        numStudent = int(screen.getstr().decode())
        screen.clear()

        for i in range (numStudent) :
            screen.addstr("Input the id of student\n")
            screen.refresh()
            sid = int(screen.getstr().decode())
            screen.clear()

            screen.addstr("Input the name of student\n")
            screen.refresh()
            student_Name = screen.getstr().decode()
            screen.clear()

            screen.addstr("Input the date of birth of student\n")
            screen.refresh()
            dob = screen.getstr().decode()
            screen.clear()

            temp_Student = Student(self, sid, student_Name, dob)
            
            
        screen.addstr("Input the number of course\n")    
        numCour = int(screen.getstr().decode())
        screen.cleer()

        for y in range (numCour):
            screen.addstr("Input the id of the course\n")
            screen.refresh()
            cid = int(screen.getstr().decode())
            screen.clear()

            screen.addstr("Input the number of credit of this course")
            screen.refresh()
            credit = int(screen.getstr().decode())
            screen.clear()

            screen.addstr("Input the name of the course\n")
            screen.refresh()
            course_Name = screen.getstr().decode()
            temp_Course = Course(self, cid, course_Name, credit)
            screen.clear()
        
        x = 0    
        while x == 0:
            screen.addstr("Input the id of the student you want to give mark\n")
            screen.refresh()
            sid1 = int(screen.getstr().decode())
            screen.clear()
            
            screen.addstr("Input the id of the course you want to give mark\n")
            screen.refresh()
            cid1 = int(screen.getstr().decode())
            screen.clear()

            screen.addstr("Input the mark of the student you want to give\n")
            screen.refresh()
            temp_Mark = int(screen.getstr().decode())
            mark = math.floor(temp_Mark)
            screen.clear()

            Mark(self, sid1, cid1, mark)
            screen.addstr("Do you wish to continue ? Press 0 for yes, press 1 for no\n")
            screen.refresh()
            x  = int(screen.getstr().decode())
        calculate_student_gpa(numStudent, numCour)




if __name__ == '__main__':
    screen = curses.initscr()
    t = test_oop()
    t.start()
