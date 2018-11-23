from nntplib import NNTP
from time import strftime, time, localtime
from email import message_from_string
from urllib.request import urlopen
import textwrap
import re


def wrap(string, max=70):
    return '\n'.join(textwrap.wrap(string)) + '\n'
class NewsAgent:
    def __init__(self):
        self.sources = []
        self.destinations = []

    def addSource(self, source):
        self.sources.append(source)

    def addDestination(self, dest):
        self.destinations.append(dest)

    def distribute(self):
        items = []
        for source in self.sources:
            items.extend(source.getItems())

        for dest in self.destinations:
            dest.receiveItems(items)


class NewsItem:
    def __init__(self, title, body):
        self.title = title
        self.body = body


class NNTPSource:
    def __init__(self, servername, group, window):
        self.servername = servername
        self.group = group
        self.window = window

    def getItems(self):
        server = NNTP(self.servername)
        groupInfo = server.group(self.group)
        for num in range(5):
            id = str(int(groupInfo[2]) + num)
            articleinfo = server.article(id)[1]
            articleinfoStrings = []
            for line in articleinfo.lines:
                articleinfoStrings.append(line.decode())
            message = message_from_string('\n'.join(articleinfoStrings))

            title = message['subject']
            body = message.get_payload()

            if message.is_multipart():
                body = body[0]

            yield NewsItem(title, body)

        server.quit()


class SimpleWebSource:
    def __init__(self, url, titlePattern, bodyPattern):
        self.url = url
        self.titlePattern = re.compile(titlePattern)
        self.bodyPattern = re.compile(bodyPattern)

    def getItems(self):
        text = urlopen(self.url).read()
        textString = text.decode('utf-8')
        title = self.titlePattern.findall(textString)
        print(title)
        body = self.bodyPattern.findall(textString)
        # print(body[0])
        for line in body:
            if len(line) > 30:
                yield NewsItem(title[0], wrap(line))
                break


class PlainDestination:
    def receiveItems(self, items):
        for item in items:
            print(item.title)
            print('-' * len(item.title))
            print(item.body)


class HTMLDestination:
    def __init__(self, filename):
        self.filename = filename

    def receiveItems(self, items):
        out = open(self.filename, 'w', encoding='utf-8')
        print("""
        <html>
            <head>
            <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
                <title>Today's New</title>
            </head>
            <body>
            <h1>Today's News</h1>
        """, file=out)

        print('<ul>', file=out)
        id = 0
        for item in items:
            id += 1
            print('<li><a href="#%i">%s</a></li>' % (id, item.title), file=out)
        print('</ul', file=out)

        id = 0
        for item in items:
            id += 1
            print('<h2><a name="%i">%s</a></h2>' % (id, item.title), file=out)
            print('<pre>%s</pre>' % item.body, file=out)

        print("""
            </body>
        </html>
        """, file=out)


def runDefaultSetup():
    agent = NewsAgent()

    bbc_url = 'http://m.cnr.cn/news'
    bbc_title = '<title>(.+?)</title>'
    bbc_body = '<p.*>(.+?)</p>'
    bbc = SimpleWebSource(bbc_url, bbc_title, bbc_body)

    agent.addSource(bbc)

    clpa_server = 'nntpswitch.blueworldhosting.com'
    clpa_group = 'comp.lang.python.announce'
    clpa_window = 1
    clpa = NNTPSource(clpa_server, clpa_group, clpa_window)

    agent.addSource(clpa)

    agent.addDestination(PlainDestination())
    agent.addDestination(HTMLDestination('news.html'))

    agent.distribute()


if __name__ == '__main__': runDefaultSetup()
