import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
service = Service('C:/Users/fahmi/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe')
service.start()
driver = webdriver.Remote(service.service_url)
driver.get('http://www.google.com/')
time.sleep(5) # Let the user actually see something!
driver.quit()