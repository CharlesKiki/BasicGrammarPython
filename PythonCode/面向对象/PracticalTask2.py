VIPSTAs=0.03#vip and staff
REGs=0.02#reg
while True:
    try:
        Deposit = float(input('Enter the deposit amount:'))
    except ValueError:
        print('Incorrect date type. Please int a number!')
    else:
        break
Type = input('Enter the deposit  type (VIP/Staff/Regular)')
Test = Type.upper()
#the Test is used to detect the type if user input
while True:
    if Test =='VIP' or Test == 'REGULAR' or Test =='STAFF':
        break
    else:
        print('Enter the right type')
Type = Test
Term = int(input("Enter the deposit term (number of years): "))

print('Year        Interest    Ending balance')
#cuculate and print
all=Deposit
for count in range(Term):
    number =  count +1
    #here the number is used to show the right year
    if Type == "VIP" or Type == "STAFF":
        value=all*VIPSTAs
        all=all+value
        #the value is each year your got the extra money
        print("%4d %15.2f %17.2f" %(number,value,all))
    elif Type == 'REGULAR' :
        value=all*REGs
        all=all+value
        print("%4d %15.2f %17.2f" %(number,value,all))
if Type == "vip" or Type == "staff":
    print("Fixed deposit rate: $"+str(VIPSTAs))
elif Type == "REG":
    print("Fixed deposit rate: $"+str(REGs))
print("Ending balance: $%0.2f" %all)
all_interest=all-Deposit
print("Total interest earned: $%0.2f" %all_interest)
