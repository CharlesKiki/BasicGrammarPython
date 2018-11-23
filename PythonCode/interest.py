money = float(input('Please enter How much you want to save ?'))
OldMoney=money
time = 0
interest = float(input('Please enter the interest in one year:'))
while True:
    money=money*(1+interest)
    time = time + 1
    if money/OldMoney >= 2 :
        print("When the " + str(time) + "th year you can have the double mooney")
        break
