#this script generate some date data.
#Use re model to find specific data.

#!/usr/bin/env python

from random import randrange, choice
from string import ascii_lowercase as lc
from sys import maxsize
from time import ctime

tlds = ( 'com', 'edu', 'net', 'org', 'gov' )

for i in range(randrange(5, 11)):
    dtint = randrange(maxsize)  # pick date
    dtstr = ctime()        # date string
    llen = randrange(4, 7)      # login is shorter
    login = ''.join(choice(lc) for j in range(llen))
    dlen = randrange(llen, 13)  # domain is longer
    dom = ''.join(choice(lc) for j in range(dlen))
    print('%s::%s@%s.%s::%d-%d-%d' % (dtstr, login,
        dom, choice(tlds), dtint, llen, dlen))
