from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

optv = Options()
optv.add_experimental_option("detach", True)

serv = Service(r"C:\Users\deepmodi\AppData\Local\Programs\Python\Python311\Scripts\chromedriver.exe")
driver = webdriver.Chrome(service=serv, options=optv)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

assert(driver.current_url == "https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element(By.XPATH, "//input[@class='search-keyword']").send_keys("ber")