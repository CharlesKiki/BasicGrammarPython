#系统自带的urllib和urllib2都提供了功能强大的HTTP支持

import urllib.request
url = 'https://www.baidu.com'
response = urllib.request.urlopen(url)     #向百度服务器发送请求
response.code   # 2xx表示成功，3xx表示你应该去另一个地址，4xx表示你错了，5xx表示服务器错了
html = response.read()         # 获取到页面的源代码 # 读出得到的响应
print(html.decode('utf-8'))   # 转化为 utf-8 编码

#爬虫的一半工作——发送请求并得到响应
#接下来就是完成对HTML的解析