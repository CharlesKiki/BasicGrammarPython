# -*- coding:utf-8 -*-
from spider import SpiderHTML
from multiprocessing import Pool
import sys,urllib,http,os,random,re,time

'''
依赖：
	第三方的类库 BeautifulSoup4，请自行安装
	目录下的spider.py文件
运行环境：
		python3
		windows10
使用方法：
	命令行下运行，例：sample.py 1 5   获取1到5页的数据
'''

#收藏夹的地址
url = 'https://Path'
'''
	commit：page参数改为代码添加
'''

#本地存放的路径,不存在会自动创建
store_path = 'E:\\Path'

'''
	commit：爬虫方法重载，继承
	方法：
		start 主方法
		_processAnswer 处理需要的目标数据
		_getImgFromAnswer 处理图片信息
		_getTextFromAnswer 处理文字信息
	参数：
		目标url
		开始页面
		结束页面
		赞同数量

'''
class CollectionSpider(SpiderHTML):
	def __init__(self,pageStart, pageEnd, url):
		self._url = url
		self._pageStart = int(pageStart)
		self._pageEnd = int(pageEnd)+1
		self.downLimit = 0
	#低于此赞同的答案不收录
	'''
		功能：爬虫主逻辑
	'''
	def start(self):
		# 收藏夹的页数
		for page in range(self._pageStart,self._pageEnd):
			#目标网页的第几页
			url = self._url + '?page='+str(page)
			#获取目标网页的实体对象
			content = self.getUrl(url)
			#BS方法，获取所有的回答div
			questionList = content.find_all('div',class_='')
			#遍历所有的问题	 收藏夹的每个问题
			for question in questionList:
				#问题的标题
				Qtitle = question.find('h2',class_='')
				if Qtitle is None:
					#被和谐了
					continue

				questionStr = Qtitle.a.string
				#形成对每个问题的URL
				Qurl = 'https://www.zhihu.com'+Qtitle.a['href']
				#问题题目 windows文件/目录名不支持的特殊符号
				Qtitle = re.sub(r'[\\/:*?"<>]','#',questionStr)

				print('-----正在获取问题:' + Qtitle + '-----')
				Qcontent = self.getUrl(Qurl)
				answerList = Qcontent.find_all('div', class_='')
				self._processAnswer(answerList, Qtitle)
				# 处理问题的答案
				time.sleep(5)

			try:
				print('-----正在获取问题:'+Qtitle+'-----')
				#获取到问题的链接和标题，进入抓取
			except UnicodeEncodeError:
				print(r'---问题含有特殊字符无法显示---')
			try:
				Qcontent = self.getUrl(Qurl)
			except:
				print('!!!!获取出错!!!!!')
				pass

			answerList = Qcontent.find_all('div',class_='')
			self._processAnswer(answerList,Qtitle)
			#处理问题的答案
            time.sleep(5)



	'''
		功能：处理需要的数据位置，例如某网页的特定部分
	'''
	def _processAnswer(self,answerList,Qtitle):
		j = 0
		for answer in answerList:
			j = j + 1

			upvoted = int(answer.find('span',class_='count').string.replace('K','000')) 	#获得此答案赞同数
			if upvoted < self.downLimit:
				continue
			authorInfo = answer.find('div',class_='zm-item-answer-author-info')
			#获取作者信息
			author = {'introduction':'','link':''}
			try:
				author['name'] = authorInfo.find('a',class_='author-link').string
				#获得作者的名字
				author['introduction'] = str(authorInfo.find('span',class_='bio')['title'])
				#获得作者的简介
				author['link'] = authorInfo.find('a',class_='author-link')['href']
			except AttributeError:
				author['name'] = '匿名用户'+str(j)
			except TypeError:  																#简介为空的情况
				pass 															#匿名用户没有链接

			file_name = os.path.join(store_path,Qtitle,'info',author['name']+'_info.txt')
			if os.path.exists(file_name):
				#已经抓取过
				continue

			self.saveText(file_name,'{introduction}\r\n{link}'.format(**author))#保存作者的信息
			print('正在获取用户`{name}`的答案'.format(**author))
			answerContent = answer.find('div',class_='zm-editable-content clearfix')
			if answerContent is None:
				#被举报的用户没有答案内容
				continue

			imgs = answerContent.find_all('img')
			if len(imgs) == 0:
				#答案没有上图
				pass
			else:
				self._getImgFromAnswer(imgs,Qtitle,**author)
	'''
		功能：收录图片
	'''
	def _getImgFromAnswer(self,imgs,Qtitle,**author):
		i = 0
		for img in imgs:
			if 'inline-image' in img['class']:
				#不抓取小图
				continue
			i = i + 1
			imgUrl = img['src']
			extension = os.path.splitext(imgUrl)[1]
			path_name = os.path.join(store_path,Qtitle,author['name']+'_'+str(i)+extension)
			try:
				self.saveImg(imgUrl,path_name)
				#捕获各种图片异常，流程不中断
			except:
				pass
	'''
		功能：收录文字
	'''
	def _getTextFromAnswer(self):
		pass

#命令行下运行，例：zhihu.py 1 5   获取1到5页的数据
if __name__ == '__main__':
	page, limit, paramsNum= 1, 0, len(sys.argv)
	if paramsNum>=3:
		page, pageEnd = sys.argv[1], sys.argv[2]
	elif paramsNum == 2:
		page = sys.argv[1]
		pageEnd = page
	else:
		page,pageEnd = 1,1

	spider = CollectionSpider(page,pageEnd,url)
	spider.start()