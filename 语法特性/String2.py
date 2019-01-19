s = 'THis is a string of some words'
words = s.split()
print (words)
sentence = 'the cat sat on the mat'
worlist = sentence.split()
print (wordlist)

s = 'la-di-da-di-da'
s.split('-')

#---------------------------------------------------------------------------
def sayHello(name):
    return 'Hello' + name + 'Your name has ' + str(len(name)) + 'letters'
def main():
    name = input('Please enter a name to greet'  + '\n')
    greeting = sayHello(name)
    print(greeting)
    main()

def calcTot(lower ,upper ):
    answer = 0
    while lower <= upper :
        answer += lower
        lower += 1
        return answer
    def main()
        print(calcaTot(1,3))
        main()


def convertCtoF(celsius):
    fahrenheit = celsius * 9/5
    return fahrenheit

def main()
    temp = float(input('Please enter a temperature to convert:'))
    convert = input('Conver to celsius')
    if convert == 'c'
        print convert == 'F'
        elif convert


        #----------------------------------------------------------------------
def checkDigits(pswd)
count  = 0
for let in pswd:
    if let.isdigit();
    count += 1 ;
    return count
def checkUpper(pswd):
    count = 0
    for let in pswd:
        if let.usuper():
            count += 1
            return count

def main()
    print('A valid password must have at least 8 characters ')
