from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, os, ConfigParser

config = ConfigParser.RawConfigParser()
config.read('app.cfg')
companys = config.get('section', 'company').split(',')
driver_download_path = config.get('section', 'driver_download_path')

driver = webdriver.Chrome()
for c in companys:
    driver.get("https://www.google.com.tw/trends/explore?date=all&q=" + c)
    time.sleep(3)
    driver.find_element_by_class_name('widget-actions-menu').click()
    driver.find_element_by_xpath('//*[@title="CSV"]').click()
    downloaded_file_name = driver_download_path + 'multiTimeline.csv'
    new_file_name = driver_download_path + c +'.csv'
    time.sleep(1)
    os.rename(downloaded_file_name, new_file_name)

driver.close()