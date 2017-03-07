# -*- coding: utf-8 -*-


from scrapy.http import Request



import time
from scrapy.item import Item, Field
from selenium import webdriver

from scrapy.spiders import CrawlSpider,Rule

from scrapy.selector import HtmlXPathSelector

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import json
import random


from bs4 import BeautifulSoup




class TbSpider(CrawlSpider):

	name="sb"

	allowed_domains=["xueqiu.com"]

	start_urls=["https://xueqiu.com/k?sort=time&page=1&source=all&q=%E6%9C%B1%E5%85%B1%E5%B1%B1"]




	User_Agent_List = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.10586',\
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36',\
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:25.0) Gecko/20100101 Firefox/25.0 "]

	dcap = dict(DesiredCapabilities.PHANTOMJS)
	dcap["phantomjs.page.settings.userAgent"] = (random.choice(User_Agent_List))




	def parse(self,response):


		driver=webdriver.PhantomJS(desired_capabilities=self.dcap)

		driver.get(response.url)

		

		# 等待3秒
		# driver.implicitly_wait(3)
		sleep(5)


		print 'url============>',response.url

		# print 'body========>',driver.page_source

		try:

			soup=BeautifulSoup(driver.page_source,'lxml')


			ul=soup.find('ul',{'class':'status-list'})#.find('span',{'class':'elems-l'}).find('a').get_text()

			print 'ul==================>',ul



		except Exception, e:
			raise e
		finally:
			driver.quit()









		