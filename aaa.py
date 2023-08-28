from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

ser = Service(r"C:\Users\deepmodi\AppData\Local\Programs\Python\Python311\Scripts\chromedriver.exe")

opo = Options()
opo.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=ser, options=opo)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

assert(driver.current_url == "https://rahulshettyacademy.com/AutomationPractice/")