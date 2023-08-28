from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser = Service(r"C:\Users\deepmodi\AppData\Local\Programs\Python\Python311\Scripts\chromedriver.exe")

opo = Options()
opo.add_experimental_option("detach", True)

chrome_options = webdriver.ChromeOptions()

# Run browser in maximized mode
chrome_options.add_argument("--start-maximized")

# Headless Behaviour
chrome_options.add_argument("headless")

# Certification errors and making the browser to accept/ignore those certificates
chrome_options.add_argument("--ignore-certificate-errors")


driver = webdriver.Chrome(service=ser, options=chrome_options)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

assert(driver.current_url == "https://rahulshettyacademy.com/seleniumPractise/#/offers")