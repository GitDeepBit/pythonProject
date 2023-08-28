from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opt = Options()
opt.add_experimental_option("detach", True)

ser = Service(r"C:\Users\deepmodi\AppData\Local\Programs\Python\Python311\Scripts\chromedriver.exe")

driver = webdriver.Chrome(service=ser, options=opt)

driver.get("https://rahulshettyacademy.com/loginpagePractise/")

assert(driver.current_url == "https://rahulshettyacademy.com/loginpagePractise/")

driver.find_element(By.LINK_TEXT, "Free Access to InterviewQues/ResumeAssistance/Material").click()

# All windows captured here
windowsOP = driver.window_handles

# Switching to new window
driver.switch_to.window(windowsOP[1])

# Capturing Text
textDetails = driver.find_element(By.XPATH, "//p[@class='im-para red']").text

# Printing whole text
print(textDetails)

emailID = textDetails.split("at")[1].strip().split(" ")[0]

# Printing extracted text
print(emailID)

# Switching back
driver.switch_to.window(windowsOP[0])

# Sending Email ID, fetched email ID
driver.find_element(By.XPATH, "//input[@id='username']").send_keys(emailID)

# Sending Password
driver.find_element(By.XPATH, "//input[@name='password']").send_keys("Password123")

# Clicking
driver.find_element(By.XPATH, "//input[@type='checkbox']").click()

# Clicking on Sign in
driver.find_element(By.XPATH, "//input[@class='btn btn-info btn-md']").click()

# Explicit wait
# EC here stands for expected conditions. Syntax is changed and we have to import the class mentioned in line 6
expWait = WebDriverWait(driver, 10)
expWait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='alert alert-danger col-md-12']")))

print(driver.find_element(By.CSS_SELECTOR, ".alert-danger").text)