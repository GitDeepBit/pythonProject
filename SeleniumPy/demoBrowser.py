from selenium import webdriver

from selenium.webdriver.chrome.service import Service

service_obj = Service("C:\Users\Modi\AppData\Local\Programs\Python\Python311\chromedriver.exe")

driver = webdriver.Chrome(service=service_obj)

driver.get("https://www.google.com/")
