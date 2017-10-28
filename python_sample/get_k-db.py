# -*- coding: utf-8 -*-
import os
import time
import glob
import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class k_db_webdriver(object):
	def __init__(self):
		self.driver = webdriver.Chrome('/usr/local/bin/chromedriver')  # Optional argument, if not specified will search path.
		# self.wait = WebDriverWait(self.driver, 5)

	def _get_k_db_page(self, url_date):
		self.driver.get('http://k-db.com/stocks/%s'%(url_date))
		#元のサイトのデータが歯抜けだった。。。
		self.driver.find_element_by_link_text(u"CSVダウンロード").click()
		time.sleep(1) # Let the user actually see something!
		
	def _driver_quit(self):
		self.driver.quit()	

if __name__ == '__main__':
	#Normal----------------------------------->
	_k_db_webdriver = k_db_webdriver()
	_pd_dates = pd.date_range('2014-01-07',periods=1300,freq='D')
	for pd_date in _pd_dates:
		print(str(pd_date)[:10])
		k_db_utl = "http://k-db.com/stocks/%s"%(str(pd_date)[:10])
		print(k_db_utl)
		_k_db_webdriver._get_k_db_page(str(pd_date)[:10])	
	_k_db_webdriver._driver_quit()








