#different rate
vs=0.03#vip staff
r=0.02#reg
#enter the data and detect
while True:
    try:
        amount=float(input("Enter the deposit amount: "))
    except ValueError:
        print('Incorrect date type. Please int a number!')
    else:
        break

type=input("Enter the deposit type (VIP/Staff/Reg): ")
a=type.lower()
x=1
while x==1:
    if a!='vip'and a!='staff' and a!='reg':
        type=input("Please Enter the correct type!")
        a=type.lower()
    else:
        break

while True:
    try:
        num=int(input("Enter the deposit term (number of years): "))
    except ValueError:
        print('Incorrect date type. Please int a number!')
    else:
        break
print("Year"+' '*8+'Interest\t\tEnding balance')
#cuculate and print
all=amount
for x in range(num):
    z=x+1
    if a == "vip" or a == "staff":
        value=all*vs
        all=all+value
        print("%4d %15.2f %21.2f" %(z,value,all))
    elif a == "reg":
        value=all*r
        all=all+value
        print("%4d %15.2f %21.2f" %(z,value,all))
if a == "vip" or a == "staff":
    print("Fixed deposit rate: $"+str(vs))
elif a == "reg":
    print("Fixed deposit rate: $"+str(r))
print("Ending balance: $%0.2f" %all)
all_interest=all-amount
print("Total interest earned: $%0.2f" %all_interest)



