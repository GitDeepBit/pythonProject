from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

optionsobj = Options()
optionsobj.add_experimental_option("detach", True)

serivceobj = Service(r"C:\Users\deepmodi\AppData\Local\Programs\Python\Python311\Scripts\chromedriver.exe")

driver = webdriver.Chrome(service=serivceobj, options=optionsobj)

driver.get("https://rahulshettyacademy.com")

assert(driver.current_url == "https://rahulshettyacademy.com/")

print(driver.title)

driver.maximize_window()

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.back()

driver.refresh()

driver.forward()

driver.minimize_window()

driver.close()


