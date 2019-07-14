
class Calculator(object):
    def __init__(self,name,number,time,type):
        self._name = name
        self._number = number
        self._time = time
        self._type = type
    def Getfee(self):
        if self._type == 'ps':
            return 5.00
        if self._type == 'hb':
            return 10.50
        if self._type == 'l':
            return 15.00
    def GetType(self): #The cost per chair
        return "The cost per chair (type -" + self._type + " ) : $" + Calculator.TemFee
    def Getname(self):
        return self._name
    def Getnumber(self):
        return (self._number - int(self._number/20))
    def GetCost(self):
        return str(Calculator.TemFee * self._time * self._number)
    def Getfreenumber(self):
        return int(self._number/20)
    def __str__(self):
        return "Customer name:" + self._name + "\nThe cost per chair (type - " + self._type + " ) : $" + str(Calculator.Getfee(self)) + "\nNumber of chairs :" + str(self._number) + "\nLength of the hire: " + str(self._time) + " days" + "\nQuoted Amount = $" + str(Calculator.Getfee(self) * self._time * Calculator.Getnumber(self)) + "\nNumver of free chairs included:" + str(Calculator.Getfreenumber(self))
