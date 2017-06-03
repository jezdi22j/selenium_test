#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
import csv

## Goes to website, opens up the table
driver = webdriver.Firefox()
driver.get('http://bondaccountability.resources.ca.gov/p1.aspx')
driver.find_element_by_partial_link_text('Project Search').click()
time.sleep(2)
driver.find_element_by_id('ctl00_ContentPlaceHolder1_btnAssocCountySearch').click()
time.sleep(2)
driver.find_element_by_id('ctl00_ContentPlaceHolder1_btnSearch').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_MetricSearchGrid_ctl00_ctl03_ctl01_PageSizeComboBox"]/span/button').click()
time.sleep(2)
driver.find_element_by_xpath('//ul[@class="rcbList"]/li[4]').click()
time.sleep(2)

## prints table project hyperlinks
links = driver.find_elements_by_css_selector("a[href*='ProjectPK']")
for link in links:
    print link.get_attribute("href")
