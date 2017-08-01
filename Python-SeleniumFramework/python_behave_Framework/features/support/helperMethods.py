from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import yaml

stream = open('E:\Python-SeleniumFramework\python_behave_Framework\pageObjects\pageObjects.YML', 'r')
data=yaml.load(stream)

def getByType(locatorType):
    locatorType = locatorType.lower()
    if locatorType == "id":
        return By.ID
    elif locatorType == "name":
        return By.NAME
    elif locatorType == "xpath":
        return By.XPATH
    elif locatorType == "css":
        return By.CSS_SELECTOR
    elif locatorType == "classname":
        return By.CLASS_NAME
    elif locatorType == "link_text":
        return By.LINK_TEXT
    else:
        print("Locator type " + locatorType + " not correct/supported")
    return False


def isExpectedTitle(context):
    wait=WebDriverWait(context.browser,10,1)
    return wait.until(EC.title_is("Kode"))

def isExpectedTitleContains(context,expectedText):
    wait=WebDriverWait(context.browser,10,1)
    return wait.until(EC.title_contains(expectedText))

def element(context,page,object):
    locatorType=(data[page][object]["locator"]).lower()
    val=data[page][object]["value"]
    byType = getByType(locatorType)
    return context.browser.find_element(byType, val)

