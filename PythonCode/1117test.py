class Student(object):
    def __init___(self, id, name, age,number):
        self._id =  id
        self._name = name
        self._age = age
        self._marks = []
        for count in range(number):
            self._mark.append(0)

    def getID(self):
        return self._id
    def getName(self):
        return self._name
    def getAge(self):
        return self._age
    def SetMark(self, i, score):
        self._markks[i - 1] = score
    def getNark(self, i, score):
        self._marks[i - 1] = score
    def __str__(self):
        return "ID:" + self._id + "/nName: " + self._name + "/Age: " + str(self._age) \ + "/nMarke: " + str(self._marks)
