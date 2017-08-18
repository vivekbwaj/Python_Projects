from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import yaml
import ipdb
from traceback import print_stack
import logging
import features.support.custom_logger as cl
from termcolor import colored


log = cl.customLogger(logging.DEBUG)
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
    elif locatorType == "class":
        return By.CLASS_NAME
    elif locatorType == "link_text":
        return By.LINK_TEXT
    elif locatorType == "tag":
        return By.TAG_NAME
    else:
        print("Locator type " + locatorType + " not correct/supported")
    return False


def isExpectedTitle(context,keyword):
    wait=WebDriverWait(context.browser,10,1)
    return wait.until(EC.title_is(keyword))

def isExpectedTitleContains(context,expectedText):
    wait=WebDriverWait(context.browser,10,1)
    return wait.until(EC.title_contains(expectedText))

def element(context,page,object):
    element = None
    try:
        locatorType = (data[page][object]["locator"]).lower()
        val = data[page][object]["value"]
        byType = getByType(locatorType)
        element = context.browser.find_element(byType, val)
        log.info("Element found with locatorValue: " + val +
                      " and  locatorType: " + locatorType)
    except:
        log.info("Element not found with locatorValue: " + val +
                      " and  locatorType: " + locatorType)
        print(colored("Element not found with locatorValue: " + val +
                      " and  locatorType: " + locatorType,'white','on_yellow'))
    return element

def enterText(context,page,object,textToBeEntered):
    textField=element(context,page,object)
    if textField is not None:
       textField.send_keys(textToBeEntered)
    else:
       log.info("Failed to enter text at :"+page+">"+object)
       print(colored("Failed to enter text at :"+page+">"+object,'white','on_yellow'))
       assert False

def clickOn(context,page,object):
    clickable=element(context,page,object)
    if clickable is not None:
        clickable.click()
    else:
        log.info("Failed to click on element :" + page + ">" + object)
        print(colored("Failed to click on element :" + page + ">" + object, 'white', 'on_yellow'))
        assert False
