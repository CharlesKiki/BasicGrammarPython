#Practicak Task1
Large = 0.1
Small = 0.08
Depreciation = 0
CurrentValue = 25000
RightYear = 0
while True:
    try:
        Cost = int(input("Please enter the total cost to furnish $:"))
    except ValueError:
        print('Incorrect date type. Please int a number!')
    else:
        break
Value = Cost # the Value is the origiena cost
Type = input("Large or Small apartment? (L - larges/S - Small:)")
if Type.lower() != 's' and Type.lower() != 'l':
    print("Incorrect date type. Please int a number!")
while True:
    try:
        Year = int(input("Enter number of years for the schedule:"))
    except ValueError:
        print('Incorrect date type. Please int a number!')
    else:
        break

#Caculate Part
print("Year        Depreciation         Current Value at $")
for count in range(Year):
    number =  count +1 #here the number is used to show the right year
    if Type.lower() == "l" :
        Depreciation = Cost * 0.1
    elif Type.lower() == "s" :
        Depreciation = Cost * 0.08
    CurrentValue =  Cost - Depreciation
    Cost = CurrentValue
    print("%4d %19.2f %30.2f" %(number,Depreciation,CurrentValue))
    if Type.lower() == "l" :
        if (CurrentValue - CurrentValue * 0.1) < 20000 :
            break
    if Type.lower() == "s" :
        if (CurrentValue - CurrentValue * 0.08) < 15000 :
            break
RightYear = number
print("Refurnish after " + str(number) + " Years")
if Type.lower() == "l" :
    print("Content depreciation rate: " +  str(Large))
elif Type.lower() == "s":
    print("Content depreciation rate: " +  str(Small))
print("Total depreciation at the end of schedule: " + str(Value - Cost))

