from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "C:\Drivers\chromedriver.exe"
website_url = "http://secure-retreat-92358.herokuapp.com/"

chrome_driver = webdriver.Chrome(executable_path=chrome_driver_path)

chrome_driver.get(website_url)

first_name = chrome_driver.find_element_by_name("fName")
first_name.send_keys("Nithin")


last_name = chrome_driver.find_element_by_name("lName")
last_name.send_keys("KM")


first_name = chrome_driver.find_element_by_name("email")
first_name.send_keys("nithinkm@hulkmania.com")

sign_up = chrome_driver.find_element_by_class_name("btn-lg")
sign_up.send_keys(Keys.ENTER)


time.sleep(3)

chrome_driver.quit()