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