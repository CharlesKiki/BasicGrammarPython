#Variable initialization

class BasicCourse(object):
    def __init__(self,name,number):
        self._name = name
        self._number = number
    def Getname(self):
        return self._name
    def Getnumber(self):
        return self._number

class Cert(BasicCourse):
    #CertPrice = 400
    def __init__(self, name, number):
        BasicCourse.__init__(self, name, number)
        self._name = name
        self._number = number
    def GetPrice(self):
        return str(400)
    def GetTotalPrice(self):
        Num = str(int(self._number) * 400)
        return Num
    def Getname(self):
        return self._name
    def __str__(self):
        return "Fee calculation for " + Cert.Getname(self) +  "\nSingle subject cost =" + Cert.GetPrice(self) + "\nSubjects total cost = $" + Cert.GetTotalPrice(self)

class Diploma(BasicCourse):
    #DiplomaPrice = 500
    def __init__(self, name, number):
        BasicCourse.__init__(self, name, number)
        self._name = name
        self._number = number
    def GetPrice(self):
        return str(500)
    def GetTotalPrice(self):
        Num = str(int(self._number) * 500)
        return Num
    def Getname(self):
        return self._name
    def __str__(self):
        return "Fee calculation for " + Diploma.Getname(self) +  "\nSingle subject cost =" + Diploma.GetPrice(self) + "\nSubjects total cost = $" + Diploma.GetTotalPrice(self)

class HigherDiploma(BasicCourse):
    #HigherDiploma = 650
    def __init__(self, name, number):
        BasicCourse.__init__(self, name, number)
        self._name = name
        self._number = number
    def GetPrice(self):
        return str(650)
    def GetTotalPrice(self):
        Num = str(int(self._number) * 650)
        return Num
    def Getname(self):
        return self._name
    def __str__(self):
        return "Fee calculation for " + HigherDiploma.Getname(self) +  "\nSingle subject cost =" + HigherDiploma.GetPrice(self) + "\nSubjects total cost = $" + HigherDiploma.GetTotalPrice(self)


