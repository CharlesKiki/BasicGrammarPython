#4565152 Charles
from ChairClassExtension import Calculator
def main():
    print("------------Comfort Chair Hire - Hire Bookings-----------\n")
    Name = input("Please input Contact/Company name:")
    print("PS - (Packer Stacker Chair - $5.00), HB - (High Back Plastic Chairs $10.50),L - (Lecture Chairs $15.00)")
    Type = input("Prefered chair type :")
    Number = int(input("Number of chair required :"))
    Time = int(input("Please enter the duration of the hire (in days) :"))
    print("------------Chair Hire Quotaion --------------------------\n")
    Example = Calculator(Name,Number,Time,Type.lower()) #name,number,time,type
    print(Example)
main()

