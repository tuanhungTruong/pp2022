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