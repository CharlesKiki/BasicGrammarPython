import turtle
lazy = turtle.Turtle()
lazy.shape(‘turtle’)
lazy.color(‘red’)

class Student(object):
    def __init__(self,id,name,age):
        self._id = id
        self._name = name
        self_age = age
    def getID(self):
        return self.id
