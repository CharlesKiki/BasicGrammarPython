print('Student Name ' + "                     " + 'Average Mark')
print('------------------------------------------------')
file = open("studMarks.txt", "r")
for line in file:
    Words = line.split()
    Firstname = Words[0]
    Secondname = Words[1]
    Score = float(float(Words[2]) + float(Words[3]) + float(Words[4]) + float(Words[5])) / 4
    print("%-20s%10.2f" % (Firstname + " " + Secondname, Score))
file.close() #关闭文件接口

