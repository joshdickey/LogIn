"""
this is just a basic script that can be run to go to a single website and log in. 
It is going to use Firefox


"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

	

fox.implicitly_wait(10)

fox.get('https:// ')#the website that you want to go to 


username = fox.find_element_by_id('username')
password = fox.find_element_by_id('password')
login = fox.find_element_by_class_name('btnLogin')

username.clear()
username.send_keys(' ')#your Userame goes here
password.clear()
password.send_keys(' ')#your password goes here. 
login.click()


