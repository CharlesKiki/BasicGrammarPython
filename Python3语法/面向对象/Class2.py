class VenueType(object):
    def __init__(self,type,hour):
        if type.lower() == 's':
            self._type  = 1400.00
        elif type.lower() == 'm':
            self._type = 1500.00
        elif type.lower() == 'l':
            self._type = 1650.00
        self._hour = hour
    def GetPrice(self):
        return self._type
    def GetTotalPrice(self):
        TotalPrice = (self._type * self._hour)
        return str(TotalPrice)
    def GetHour(self):
        return self._hour
    def __str__(self):
        return "Hourly booking cost $" + str(self._type) + "\nTotal booking cost = $ " + VenueType.GetTotalPrice(self) + " for " + str(self._hour) + "hours"
