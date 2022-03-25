class Student:
    def __init__(self, test, sid, name, dob):
        self.__sid = sid
        self.__name = name
        self.__dob = dob
        student_Info = {'id' : sid, 'name' : name, 'dob' : dob}
        test.students.append(student_Info)

    def get_sid(self):
        return self.__sid

    def get_name(self):
        return self.__name

    def get_dob(self):
        return self.__dob

class Course:
    def __init__(self, test, cid, name):
        self.__cid = cid
        self.__name = name
        course_Info = {'id' : cid, 'name' : name}
        test.courses.append(course_Info)

    def get_cid(self):
        return self.__cid

    def get_name(self):
        return self.__name

class Mark:
    def __init__(self, test, sid, cid, mark):
        self.__sid = sid
        self.__cid = cid
        self.__mark = mark
        mark_Info = {'Student id' : sid, 'Course id' : cid, 'mark' : mark}
        test.marks.append(mark_Info)

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
    
    def start (self):  
        numStudent = int(input('Input the number of students : '))
        for i in range (numStudent) :
            sid = input('Input the id of student : ')
            student_Name = input('Input the name of student : ')
            dob = input('Input the date of birth of student : ')
            temp_Student = Student(self, sid, student_Name, dob)
            
            
        numCour = int(input('Input the number of course'))
        for y in range (numCour):
            cid = input('Input the id of the course: ')
            course_Name = input('Input the name of the course: ')
            temp_Course = Course(self, cid, course_Name)
        
        x = 0    
        while x == 0:
            sid1 = int(input('Input the id of the student you want to give mark'))
            cid1 = int(input('Input the id of the course'))
            mark = int(input('Input the mark for the chosen student'))
            Mark(self, sid1, cid1, mark)
            print('Do you wish to continue ? Press 0 for yes, press 1 for no')
            x  = int(input())

if __name__ == '__main__':
    t = test_oop()
    t.start()
