class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
    def getname(self):
        return self._name
    def getgender(self):
        return self._gender

class Student(Person):
    def __init__(self, name, gender, score):
        Person.__init__(self, name, gender)
        self.score = score
    def getscore(self):
        return self.score
    def __str__(self):
        return str(self.getscore())

test = Student('test','man',0)
print(test.getscore())
