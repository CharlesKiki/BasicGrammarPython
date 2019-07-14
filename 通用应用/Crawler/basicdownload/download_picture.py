'''
    commit:
            下载当前页面的所有图片。
    依赖：
        不使用BS模块。
'''



import urllib
import urllib.request
import re
import sys
import os

#获取当前的脚本路径

#打开网页，下载器
def open_html ( url):
 require=urllib.request.Request(url)
 reponse=urllib.request.urlopen(require)
 html=reponse.read()
 return html
#下载图片
def load_image(html):
 regx='http://[\S]*jpg'
 pattern=re.compile(regx)
 get_image=re.findall(pattern,repr(html))

 #文件命名从1开始
 num=1
 path = sys.path[0]+'/picture'
 if not os.path.exists(path):
  os.makedirs(path)
 for img in get_image:
  photo=open_html(img)
  with open(r'%s\%s.jpg'%(path,num),'wb') as f:
   print('开始下载图片')
   f.write(photo)
   print('正在下载第%s张图片'%num)
   f.close()
  num=num+1
 if num>1:
  print('下载成功！！！')
 else:
  print('下载失败！！！')

'''
    commit:
            创建保存资源的目录
'''
def _checkPath(foldername):
	#strip()方法用以消除字符串首尾的空格
	dirname = os.path.dirname(foldername.strip())

url='http://www.qiqipu.com/'
html=open_html(url)
load_image(html)
