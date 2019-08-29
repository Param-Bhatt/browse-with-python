#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import requests
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from mysql.connector import mysql.connector as db
#connecting to db
HOST = "172.16.100.66/phpmyadmin"
PORT = 3306
USER = "root"
PASSWORD = "@)!&swd2NUC!*"
DB = "swd"

conn = mysql.connector.connection(host=HOST, port=PORT,
                        user=USER, passwd=PASSWORD, db=DB)

cursor=conn.cursor()
cursor.execute("SELECT * from 2014batch;")
row=cursor.fetchone()
#connecting to website, opening browser in a new page
browser = webdriver.Firefox()
#browser.set_preference("browser.privatebrowsing.autostart", True)


browser.get('http://172.16.100.66/office_login.php')


#time.sleep(10)


select = Select(browser.find_element_by_name("id"))

# select by visible text
select.select_by_visible_text('SWD')

# select by value 
#select.select_by_value('1')

#now putting in the password
password = browser.find_element_by_id("inputPassword")
password.send_keys("swd_office")
login_attempt = browser.find_element_by_xpath("//*[@type='submit']")
login_attempt.submit()

#successfully logged in now
browser.maximize_window() 
browser.implicitly_wait(10) 

#doc = driver.find_element_by_class_name('container')
html_list = browser.find_element_by_id("tabula")
#items = html_list.find_elements_by_tag_name("li")
doc = (browser.find_element_by_partial_link_text('Document Generation')).click()
doc=browser.find_element_by_id("sell")
doc.click()
#print(doc)
#doc.click()

myid="f20180862"
while(row is not None):
    id = browser.find_element_by_id("enterid")
    id.send_keys(myid)
    generate=browser.find_element_by_name("fee_rec_sem1")
    generate.click()
    browser.implicitly_wait(30) 
    print(row[0])
    generate=browser.find_element_by_name("fee_rec_sem2")
    generate.click()
    row=cursor.fetchone()

cursor.close()