from selenium import webdriver
import os

# driverLocation = "E:\Python-SeleniumFramework\python_behave_Framework\dependencies\chromedriver.exe"
# os.environ["webdriver.chrome.driver"] = driverLocation
#        # Instantiate Chrome Browser Command
# driver = webdriver.Chrome(driverLocation)
#         # Open the provided URL
# driver.get("http://www.letskodeit.com")

# driverLocation = "E:\Python-SeleniumFramework\python_behave_Framework\dependencies"
# os.environ["webdriver.gecko.driver"] = driverLocation
#        # Instantiate Chrome Browser Command
# driver = webdriver.Firefox(driverLocation)
        # Open the provided URL

driver = webdriver.Chrome(driverLocation)
driver.get("http://www.letskodeit.com")