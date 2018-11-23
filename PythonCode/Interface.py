#4565152 Charles
from VenueBookings import VenueType
def main():
    Name = input("Please input customer name:")
    Date = input("Please input booking data:")
    print("Booking cost depends on the venue capacity and the booking period \nS - (50 - 100 guests),M - (100 - 200 guests),L - (200 - 300 guests)")
    Type = input("Please select your venue capacity option:")
    Hour = int(input("Booking period?"))
    print("********* Booking Fee Calculations *********")
    print("Booking fee calculation for " + Name + "on" + Date)

    Example = VenueType(Type,Hour)
    print(Example)
main()

