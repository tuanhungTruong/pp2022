import math
import curses
from domains.Student import *
from domains.Course import *
from domains.Mark import *

class input:

    def __init__(self, scr):
        self.__screen = scr

    def input_number_of_student(self, test_oop):
        self.__screen.addstr("Input the number of students\n")
        self.__screen.refresh()
        numStudent = int(self.__screen.getstr().decode())
        self.__screen.clear()
        test_oop.number_of_students = numStudent

    def input_number_of_course(self, test_oop):
        self.__screen.addstr("Input the number of courses\n")
        self.__screen.refresh()
        numCour = int(self.__screen.getstr().decode())
        self.__screen.clear()
        test_oop.number_of_courses = numCour

    def input_student_info(self):
            self.__screen.addstr("Input the id of student\n")
            self.__screen.refresh()
            sid = int(self.__screen.getstr().decode())
            self.__screen.clear()

            self.__screen.addstr("Input the name of student\n")
            self.__screen.refresh()
            student_Name = self.__screen.getstr().decode()
            self.__screen.clear()

            self.__screen.addstr("Input the date of birth of student\n")
            self.__screen.refresh()
            dob = self.__screen.getstr().decode()
            self.__screen.clear()

            Student(self, sid, student_Name, dob)


    def input_student_info(self):
        self.__screen.addstr("Input the id of student\n")
        self.__screen.refresh()
        sid = int(self.__screen.getstr().decode())
        self.__screen.clear()

        self.__screen.addstr("Input the name of student\n")
        self.__screen.refresh()
        student_Name = self.__screen.getstr().decode()
        self.__screen.clear()

        self.__screen.addstr("Input the date of birth of student\n")
        self.__screen.refresh()
        dob = self.__screen.getstr().decode()
        self.__screen.clear()

        Student(self, sid, student_Name, dob)

    def input_mark(self):
        self.__screen.addstr("Input the id of the student you want to give mark\n")
        self.__screen.refresh()
        sid1 = int(self.__screen.getstr().decode())
        self.__screen.clear()
            
        self.__screen.addstr("Input the id of the course you want to give mark\n")
        self.__screen.refresh()
        cid1 = int(self.__screen.getstr().decode())
        self.__screen.clear()

        self.__screen.addstr("Input the mark of the student you want to give\n")
        self.__screen.refresh()
        temp_Mark = int(self.__screen.getstr().decode())
        mark = math.floor(temp_Mark)
        self.__screen.clear()

        Mark(self, sid1, cid1, mark)
        self.__screen.addstr("Do you wish to continue ? Press 0 for yes, press 1 for no\n")
        self.__screen.refresh()
        x  = int(self.__screen.getstr().decode())



    