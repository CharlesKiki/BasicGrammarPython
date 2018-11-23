f = open("studMarks.txt","r")
print("%-18s %20s"%("Student Name","Average Work"+"\n-------------------------------"))
for line in f:
    words = line.split()
    sname = words[0]
    fname = words[1]
    grade1 = float(words[2])
    grade2 = float(words[3])
    grade3 = float(words[4])
    grade4 = float(words[5])
    average = round((grade1+grade2+grade3+grade4)/4)
    print("%-20s%10.2f"% (fname +" "+ sname,average))
f.close()


