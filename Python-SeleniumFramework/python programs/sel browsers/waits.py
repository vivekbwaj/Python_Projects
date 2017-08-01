from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

driverLocation = "E:\Python-SeleniumFramework\python_behave_Framework\dependencies\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = driverLocation
       # Instantiate Chrome Browser Command
driver = webdriver.Chrome(driverLocation)
        # Open the provided URL
driver.get("http://www.letskodeit.com")


def isExpectedTitle():
    wait=WebDriverWait(driver,10,1)
    return wait.until(EC.title_is("Kode"))

def isExpectedTitleContains():
    wait=WebDriverWait(driver,10,1)
    return wait.until(EC.title_contains("Kode"))

if isExpectedTitle():
    driver.get("http://selenium-python.readthedocs.io/waits.html")

