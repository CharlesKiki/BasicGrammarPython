print('The program need you enter some of your informaiton')
Username = input("Now, What's is you name?")
Userage = input("How old are you ")
Usermajor = input("What's is your major?")

File = open("TuteEx3Format.txt","w")
File.write('This is the line 1 \n This is the line 2 \n')
File.write(Username + " your major " + Usermajor + "is very popular")
File.close()

File = open("TuteEx3Format.txt","r")
for line in f:
    print(line)
    

