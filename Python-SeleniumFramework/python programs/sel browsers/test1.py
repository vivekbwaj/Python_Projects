from selenium import webdriver
import os
from selenium.webdriver.common.by import By

driverLocation = "E:\Python-SeleniumFramework\python_behave_Framework\dependencies\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = driverLocation
#
driver = webdriver.Chrome(driverLocation)




# driverLocation = "E:\Python-SeleniumFramework\python_behave_Framework\dependencies"

# os.environ["webdriver.gecko.driver"] = driverLocation
# driver = webdriver.Firefox()



driver.get("https://www.google.com.au/")
driver.implicitly_wait(10)
srchField=driver.find_element(By.ID,"lst-ib")
srchBtn=driver.find_element(By.ID,"_fZl")

srchField.send_keys("learn python and selenium")
# srchBtn.click()
# driver.find_element(By.PARTIAL_LINK_TEXT,"lynda").click()
driver.quit()

