import input
import output
import math
import curses
import zipfile

class test_oop:
    students = []
    courses = []
    marks = []
    
    number_of_students = 0
    def __init__(self, scr):
        self.__screen = scr
        self.__input = input.Input(scr)
        self.__output = output.Output(scr)


    def listStudent (self) :
        print(students)

    def listCourse (self) :
        print(courses)
    
    def listMark (self):
        print(marks)
    
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


    def start (self):  
        self.__screen.addstr("Input the number of students\n")
        self.__screen.refresh()
        numStudent = int(self.__screen.getstr().decode())
        self.__screen.clear()

        if os.path.isfile('students.dat'): 
            zip_file = zipfile.ZipFile('students.dat', 'r')
            zip_file.extractall()  
            if os.path.isfile('students.txt'):  
                sf = open('students.txt', 'r').read().splitlines()
                self.number_of_students = int(len(sf)/3)
                for i in range(self.number_of_students):
                    input.input_student(self, sf[i*3], sf[i*3 + 1], sf[i*3 + 2])

	file_list = ['students.txt', 'courses.txt', 'marks.txt']
	with zipfile.ZipFile('students.dat', 'w') as new_zip:
		for file_name in file_list:
			new_zip.write(file_name)
	for file_name in file_list:
		os.remove(file_name)

        for i in range (numStudent) :
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

            temp_Student = Student(self, sid, student_Name, dob)
            
            
        self.__screen.addstr("Input the number of course\n")    
        numCour = int(self.__screen.getstr().decode())
        self.__screen.cleer()

        for y in range (numCour):
            self.__screen.addstr("Input the id of the course\n")
            self.__screen.refresh()
            cid = int(self.__screen.getstr().decode())
            self.__screen.clear()

            self.__screen.addstr("Input the number of credit of this course")
            self.__screen.refresh()
            credit = int(self.__screen.getstr().decode())
            self.__screen.clear()

            self.__screen.addstr("Input the name of the course\n")
            self.__screen.refresh()
            course_Name = self.__screen.getstr().decode()
            temp_Course = Course(self, cid, course_Name, credit)
            self.__screen.clear()
        
        x = 0    
        while x == 0:
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
        calculate_student_gpa(numStudent, numCour)
