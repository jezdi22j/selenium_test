#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Firefox()
driver.get('http://bondaccountability.resources.ca.gov/p1.aspx')
# driver.get('http://bondaccountability.resources.ca.gov/AssociatedCountySearch.aspx')
driver.find_element_by_partial_link_text('Project Search').click()
# driver.manage().timeouts().pageLoadTimeout(15, TimeUnit.SECONDS);
# wait = WebDriverWait(driver, 10)
# button = wait.until(EC.elementToBeClickable(By.id("ctl00_ContentPlaceHolder1_btnAssocCountySearch")))
time.sleep(2)
driver.find_element_by_id('ctl00_ContentPlaceHolder1_btnAssocCountySearch').click()
time.sleep(2)
driver.find_element_by_id('ctl00_ContentPlaceHolder1_btnSearch').click()
time.sleep(2)
driver.find_element_by_partial_link_text('./Project.aspx?ProjectPK=').click()
# driver.find_element_by_xpath('//*[@title="Next Page"]').click()
# print element.page_source
# print(project.__class__.__name__)

# driver2 = webdriver.Firefox()
# driver2.get(raw_input('http://bondaccountability.resources.ca.gov/p1.aspx'))
# print driver2.page_source

# wait = WebDriverWait(driver, 10)
# button = wait.until(EC.presence_of_element_located((By.ID, "'ctl00_ContentPlaceHolder1_btnAssocCountySearch'")))
# button.click()
# #
# wait2 = WebDriverWait(driver, 30)
# button2 = wait2.until(EC.presence_of_element_located((By.ID, "ctl00_ContentPlaceHolder1_btnSearch")))
# button2.submit()


# county = project.find_element_by_id("ctl00_ContentPlaceHolder1_btnAssocCountySearch").click()
#
# other = wait.until(EC.presence_of_element_located((By.ID,'ctl00_ContentPlaceHolder1_btnSearch')))
# other.click()
