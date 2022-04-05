import curses
import numpy as np
import math


class Output:
    def __init__(self, scr):
        self.__screen = scr
    
    def list_courses(self, test_oop):
        self.__screen.addstr("Courses existing:")
        self.__screen.refresh()
        for course in test_oop.courses:
            self.__screen.addstr("\n\t\t[%s]   %-20s%d credits" % (course.get_cid(), course.get_name(), course.get_credit()))
            self.__screen.refresh()

    # List all the students
    def list_students(self, test_oop):
        self.__screen.addstr("Students in class:")
        self.__screen.refresh()
        for student in test_oop.students:
            self.__screen.addstr("\n\t\t[%s]    %-20s%s" % (student.get_sid(), student.get_name(), student.get_dob()))
            self.__screen.refresh()


    def list_course_marks(self, test_oop, cid):
        for mark in test_oop.marks:
            if mark.get_cid() == cid:
                sid = mark.get_sid()
                for student in test_oop.students:
                    if student.get_sid() == sid:
                        self.__screen.addstr(f"\n\t\t[%s]    %-20s%s" % (student.get_sid(), student.get_name(),mark.get_value()))
                        self.__screen.refresh()



    def calculate_student_gpa(self, numStudent, numCour):
        self.__screen.addstr("Input the id of the student you want to calculate gpa")
        self.__screen.refresh()
        sid_temp = int(self.__screen.getstr().decode())
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