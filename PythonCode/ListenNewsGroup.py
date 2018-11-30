#This file used to get NewGroup information.
from nntplib import NNTP
from time import strftime, time, localtime
day = 24 * 60 * 60
'''All seconds in a day'''

yesterday = localtime(time() - day)
#date = strftime('%y%m%d', yesterday)
hour = strftime('%H%M%S', yesterday)

servername = 'web.aioe.org'
group = 'comp.lang.python.announce'
server = NNTP(servername)
class datetime.date(2017, 9, 16)
ids = server.newnews(group, date, *IDS, file=None)[1]

for Newsid in ids:
    head = server.head(Newsid)[3]
    for line in head:
        if line.lower().starswith('subject:'):
            subject = line[9:]
            break
        
        body = server.body(Newsid)[3]

        print(subject)
        print('-'*len(subject))
        print('\n'.join(body))
    server.quit()
'''This is a fucking NewsToday program
and I swire to finish it today'''
