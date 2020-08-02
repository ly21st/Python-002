# -*- coding: utf-8 -*-

from selenium import webdriver
import time
import traceback


try:
    browser = webdriver.Chrome()
    browser.get('https://shimo.im')
    time.sleep(1)

    btm1 = browser.find_element_by_xpath(
        '//*[@id="homepage-header"]/nav/div[3]/a[2]/button')
    btm1.click()
    time.sleep(1)

    browser.find_element_by_xpath(
        '//input[@name="mobileOrEmail"][@type="text"]').send_keys('15800012319')
    browser.find_element_by_xpath(
        '//input[@name="password"][@type="password"]').send_keys('123456')
    time.sleep(1)

    browser.find_element_by_xpath(
        '//button[contains(@class,"sm-button")][@type="black"]').click()
    time.sleep(3)
except Exception as e:
    print(traceback.format_exe())
finally:    
    browser.close()
