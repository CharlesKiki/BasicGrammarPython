count = 0
while (count < 9):
   print ('The count is:'),count
   #Python的语句分割由，进行
   count = count + 1
print ("Good bye!")
#由缩进造成的循环语句块

#分割线------------------------------------------
for count in range(5):
#in的作用：判断左值是否在右值内
   print(count)
for count in range(3)
   print(count +1)

#分割线------------------------------------------------------
psWord = input ("Please input your paaword:")
while psWord != "koala":
   print("Sorry ,wrong pass word!")
   psWord = input ("Please input your paaword:")
print("Welcome!!")
#分割线--------------------------------------------------------
psWord = input ("Please input your paaword:")
attempt = 1
while psWord != "koala":
   print("Sorry ,wrong password!")
   psWord = input ("Please input your paaword:")
   attempt += 1
else:
   break
if psWord == 'koala':
    print('Welcome! You have logged in successfully!')
else:
   print('No more attemptt left ! Please try some other time!')

#分割线______________________________________________________________

Lower = 1
Upper = 10
while Ture:
   try:
      num = int(input("Please input a number between 1 and 10:"))
   except ValureError:
      print('Incoorect data type.Please enter whole number!')
   else:
      if Lower<= num <= Upper:
         break
      else:
         print('Wrong range! number shoule be between a and 10 - inclusive')

if num == Upper:
   print('Upper limit!')
elif num == Lower:
   print('Lower limit ')
else:
   print('in range')

#------------------------------------------------------------------
import random
for count in range(1,8)
   number = random.randint(1,20)
   print('This is a string' + str(number))

#-----------------------------------------------------------------
stringname = 'This  is a sentence'
len(stringname)
stringname [0:3]
