num = int(input('Please enter a number to print'))
print(num)
num2 = float(input('Please enter a decimal number print'))
print(num2)
print('Hello' + '\n' + 'How are you?')
sum = num + num2

#else sentence
name = input('What is your name')
if name.endswith('Zhang'):
    print ('Hello,Zhang')
else:
    print ('Hello,stranger')

number = input('Enter a number:')
if number >0 :
    print ('The number is positive')
elif number<0:
    print('The number is negative')
else:
    print('The number is zero')
