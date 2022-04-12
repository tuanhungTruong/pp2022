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