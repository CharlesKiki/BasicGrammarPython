# somescript.py
import sys
text = sys.stdin.read()
words = text.split()
wordcount = len(words) 
print 'Wordcournt:'.wordcount

#How to use this script?
#cat somefile.txt | Countsys.stdin.py