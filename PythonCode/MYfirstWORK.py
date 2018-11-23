Cost = float(input('What is the current cost of the car?'))
Age = int(input('What is the age of the car?'))
Value = int(input('Value calculation after how many years?'))
print('Year      Value')
print('***************')
for count in range(Age):
    #Focus here : the count begin from 0 not 1
    #even you defind it start as 1
    if Age <= 3:
        Cost = Cost*0.99
    else:
        Cost = Cost*0.98
    print("%d %15.2f" %(count+1 , Cost))
    count += 1
print('Value of the car after ' + str(Age) + ' year ' + str(Cost))
