from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

optobj = Options()
optobj.add_experimental_option("detach", True)

serobj = Service(r"C:\Users\deepmodi\AppData\Local\Programs\Python\Python311\Scripts\chromedriver.exe")

driver = webdriver.Chrome(service=serobj, options=optobj)

driver.get("https://rahulshettyacademy.com")

assert(driver.current_url == "https://rahulshettyacademy.com/")

# Maximising the window
driver.maximize_window()

print(driver.title)

print(driver.current_url)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

# Minimizing the window
#driver.minimize_window()

# Going back to previous web page
driver.back()

# Refreshing the webpage
driver.refresh()

# Going forward
driver.forward()

driver.close()


