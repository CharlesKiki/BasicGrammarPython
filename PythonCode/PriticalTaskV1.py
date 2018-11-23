salary = int(input('Please enter the current salary $: '))
while True:#check the inputting value
    try:
        level = int(input('Teacher level (1 - 5): '))
    except ValueError:
        print('input value is wrong!!!!!')
    else:
        if 1<=level<=5:
            break
        else:
            print('Please enter the level during 1-5')
year = int(input("Enter number of years for the schedule: "))
print('Year    Year Increment                Salary $')
rate = 0
if 1<=level<=3:
    rate = 0.05         #different level ,different rate
    for counts in range(1,year+1):
        Increment = salary * rate
        salary = salary + Increment
        if salary>70000:
            salary = 70000
            break
        print(str(counts) + "\t\t\t%10.2f"%Increment +"\t\t\t\t%10.2f"%salary)
elif level>3:
    rate = 0.07
    for counts in range(1,year+1):
        Increment = salary * rate
        salary = salary + Increment
        if salary>90000:
            salary = 90000
            break
        print(str(counts) + "\t\t\t%10.2f"%Increment +"\t\t\t\t%10.2f"%salary)
print("Salary increment rate: %.2f"%rate)
print('Final salary at the end of the scheduled period: $%.2f'%salary)
