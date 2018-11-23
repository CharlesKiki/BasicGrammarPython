VIPSTAs=0.03#vip staff
REGs=0.02#reg
while True :
    try:
        Deposit = float(input('Enter the deposit amount'))
        break
    except ValueError:
        peint("Error,try again")
        
Type = input('Enter the deposit  type (VIP/Staff/Reg)')
Type = Type.upper()
if(Type !='VIP' or Type != 'REGULAR' or Type !='STAFF'):
    print('Error ,try again')

Term = int(input('Enter the deposit term (number of year)?'))
print('Year        Interest    Ending balance')
#cuculate and print
all=Deposit
for count in range(Term):
    number =  count +1
    #here the number is used to show the right year 
    if Type == "VIP" or Type == "STAFF":
        value=all*VIPSTAs
        all=all+value
        print("%4d %15.2f %21.2f" %(number,value,all))
    elif Type == "REG":
        value=all*REGs
        all=all+value
        print("%4d %15.2f %21.2f" %(number,value,all))
if a == "vip" or a == "staff":
    print("Fixed deposit rate: $"+str(VIPSTAs))
elif a == "reg":
    print("Fixed deposit rate: $"+str(REGs))
print("Ending balance: $%0.2f" %all)
all_interest=all-Deposit
print("Total interest earned: $%0.2f" %all_interest)

