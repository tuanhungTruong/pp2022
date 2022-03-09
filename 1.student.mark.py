numStud = 0
studentList = []
numCour = 0
courseList = []
mark = []

def addMark () :
    markInfo = {}
    listCourse()
    markInfo['course id'] = input('Input the course id :')
    listStudent()
    markInfo['student id'] = input('Input the student id :')
    markInfo['mark'] = input('Input the mark of this student in this course :')
    mark.append(markInfo)
    
    
def inputNumberOfStudents () :
    numStudent = int(input('Input the number of students : '))
    return numStudent
    

def studentIn4 ():
    global studentList
    studentInfo = {} 
    studentInfo['id'] = input('Input the id of student : ')
    studentInfo['name'] = input('Input the name of student : ')
    studentInfo['DoB'] = input('Input the date of birth of student : ')
    studentList.append(studentInfo)
    
    
    
def numberOfCourses () :
    numCourse = int(input('Input the number of courses : '))
    return numCourse
    
    

def courseIn4 () :
    courseInfo = {}
    courseInfo['id'] = input('Input the id of course : ')
    courseInfo['name'] = input('Input the name of course : ')
    courseList.append(courseInfo)
    return courseList
    
def listStudent () :
    print(studentList)
    
    
def listCourse () :
    print(courseList)
    
    
def listMark () :
    print(mark)
    
if __name__ == "__main__" :
    numStud = inputNumberOfStudents()
    for x in range(numStud):
        studentIn4()
    
    numCour = numberOfCourses()
    for y in range (numCour):
        courseIn4()
    addMark()
    listMark()
