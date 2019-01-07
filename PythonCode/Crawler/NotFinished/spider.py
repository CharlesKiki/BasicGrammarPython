#!/url/bin/env python
# -*- coding: utf-8 -*-

'''
	作用：
		SpiderHTML类
		方法：
			获取URL，保存文本，保存图片，创建保存目录
	Commit：
			不包含特定的爬虫逻辑。
'''


__author__ = 'waiting'
import os,re,codecs,urllib,io,gzip,zlib
from urllib import request
from bs4 import BeautifulSoup
import chardet

#打开页面
class SpiderHTML(object):
	#返回BeautifulSoup对象
	def getUrl(self, url, coding='utf-8'):
		req = request.Request(url)
		req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 UBrowser/5.5.9703.2 Safari/537.36')
		req.add_header('Accept-encoding', 'gzip')
		with request.urlopen(req) as response:
			gzipd = response.headers.get('Content-Encoding')
			if gzipd == 'gzip':
				data = zlib.decompress(response.read(), 16+zlib.MAX_WBITS)

			else:
				data = response.read()
			#return BeautifulSoup(data.decode("lxml"))
			return BeautifulSoup(data,"lxml")

	'''
		Commit：以下方法可能是利用BS对象做参数
	'''
	'''
		功能：保存文本内容到本地
		commit:该方法创建文件夹并将内容写入文件内
		用例：
		saveText(self,用户评论.txt,“垃圾爬虫”,mode='w'):
	'''
	def saveText(self,filename,content,mode='w'):
		#创建该文件的对应文件夹
		self._checkPath(filename)
		#打开该文件并写入内容
		with codecs.open(filename, encoding='utf-8', mode=mode) as f:
			f.write(content)


	'''
		功能：保存图片内容到本地
		commit:该方法为每个传入的文件创建相对应的文件夹
		将图片数据写入imgname对象中
	'''
	def saveImg(self, imgUrl, imgName):
		#获取URL的图片对象
		data=request.urlopen(imgUrl).read()
		#创建imgName为命名的文件夹
		self._checkPath(imgName)
		#打开该文件
		with open(imgName,'wb') as f:
			f.write(data)

	'''
		功能：创建目录
		Commit：该方法接受一个文件名作为参数，检查某绝对路径下的文件夹是否存在
		如果不存在则创建该文件夹
	'''
	def _checkPath(self, foldername):
		#strip()方法用以消除字符串首尾的空格
		dirname = os.path.dirname(foldername.strip())
		if not os.path.exists(dirname):
			os.makedirs(dirname)
