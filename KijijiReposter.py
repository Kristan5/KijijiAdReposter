'''
Will repost all currently active ads on a Kijiji Profile
'''

from selenium import webdriver
from time import sleep
from AdProfile import *

class KijijiReposter:
	def __init__(self, username, password):
		self.openBrowser()
		sleep(1)
		self.signIn(username, password)
		sleep(1)

		# Go to profile and get info for each ad 
		self.clickButton('//*[@id="MainContainer"]/div[1]/div/header/div[3]/div/div[3]/div/div[4]/div/button')
		self.clickButton('//*[@id="MainContainer"]/div[1]/div/header/div[3]/div/div[3]/div/div[4]/div/div/ul/a[1]/li')
		sleep(1)

		# Array of all the user's currently posted ads
		adArray = 0
		# loop through each ad on profile, 
		items = self.driver.find_elements_by_class_name('item-1723786765')
		for item in items:
			item.find_element_by_xpath('//div[2]/div/div[1]/a').click()
			#self.clickButton(item);
			
			# Get the ad's title
			# title = 

			# Get the ad's description
			# description = 

			# Go through each ad and scrape title and description
			# ad = AdProfile(title, description)

			# adArray.append(ad)
			# Go back 
			self.driver.execute_script("window.history.go(-1)")

		# Posts each of the ads stored in the array
		for ad in adArray:
			# Go through array of all the user's ad and post them 
			title = ad.title
			description = ad.description
			
			break 


	def openBrowser(self):
		self.driver = webdriver.Chrome()
		self.driver.get("https://www.kijiji.ca")


	def signIn(self, username, password):
		self.clickButton('//*[@id="MainContainer"]/div[1]/div/div[2]/div/header/div[3]/div/div[3]/div/div/div/a[2]')
		self.enterText('//*[@id="emailOrNickname"]', username);
		self.enterText('//*[@id="password"]', password);
		self.clickButton('//*[@id="mainPageContent"]/div/div/div/div/form/button')


	def clickButton(self, XPath):
		self.driver.find_element_by_xpath(XPath).click()

	def enterText(self, XPath, text):
		self.driver.find_element_by_xpath(XPath).send_keys(text)


test = KijijiReposter("username", "password")
