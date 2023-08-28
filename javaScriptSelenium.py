from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

ser = Service(r"C:\Users\deepmodi\AppData\Local\Programs\Python\Python311\Scripts\chromedriver.exe")

opo = Options()
opo.add_experimental_option("detach", True)

# How to run browser window "headless". Meaning browser will not open when script is executed
chrome_options = webdriver.ChromeOptions()

# add_argument takes argument in string as headless
chrome_options.add_argument("headless")

# If there is any warning on chrome as website is not safe or anything like that
# we will use an argument --ignore-certificate-errors
chrome_options.add_argument("--ignore-certificate-errors")

driver = webdriver.Chrome(service=ser, options=chrome_options)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

assert(driver.current_url == "https://rahulshettyacademy.com/AutomationPractice/")

# Scrolling down is only allowed via javascript
# To scroll down we will be using javascript code which will be executed by Selenium
# There are many other things that selenium can't do on a web page. But it can be achieved using JS
# For Scrolling we have a code as window.scroll(arg1,arg2)
# arg1 is usually top of the page or 0th pixel on your screen. So it is generally 0
# arg2 can be anything, basically to which position user wants to scroll. So it is generally the target value
# arg2 can be any pixel value like: 300, 500, 700 etc. or bottom of the page
# To reach bottom of the page we will use a method i.e. document.body.scrollHeight
# document.body.scrollHeight gets automatically generated during run time and takes bottom of the page as value

# Selenium code calling JS
# scrollTo or scroll or scrollBy is JS event
driver.execute_script("window.scroll(0,document.body.scrollHeight);")

# How to take screenshot
driver.get_screenshot_as_file("Kichich.png")
