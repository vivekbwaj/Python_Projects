from selenium import webdriver
import yaml
import os
import logging
import ipdb
import time
from termcolor import colored
import features.support.custom_logger as cl


log = cl.customLogger(logging.DEBUG)
stream = open('E:\Python-SeleniumFramework\python_behave_Framework\Params.YML', 'r')
data=yaml.load(stream)

URL=data["URL"]

if data["Browser"]=="firefox":
    browser = webdriver.Firefox()
elif data["Browser"]=="ie":
    browser=webdriver.Ie()
elif data["Browser"] == "chrome":
    browser=webdriver.Chrome()
else:
    browser=webdriver.Chrome()


def before_all(context):
     context.browser=browser
     context.artifacts_dir = 'screenshots'

def before_feature(context, feature):
    context.browser.get(URL)
    log.info("loaded browser and Starting feature: "+feature.name)

def before_scenario(context,scenario):
    # log.info("Scenario started: "+scenario.name)
    log.info("Starting scenario: " +scenario.name)

def before_step(context, step,):
    # print(colored('the step behave is on is: ', 'blue'), colored(step.name, 'grey'))
    log.info("Starting step: "+step.name)

def after_step(context, step):
    # print(colored('the step behave is on is: ', 'blue'), colored(step.name, 'grey'))
    log.info("Executed Step: "+step.name)
    if step.status == "failed":
       print(colored("FAILED:"+context.scenario.name +">"+step.name,'red'))

def after_scenario(context, scenario):
    log.info("Executed scenario: "+scenario.name +": " + scenario.status)
    if scenario.status == "passed":
        scenario_error_dir = os.path.join(context.artifacts_dir, 'feature_errors')
        make_dir(scenario_error_dir)
        scenario_file_path = os.path.join(scenario_error_dir, scenario.name.replace(' ', '_')
                                          + '_' + time.strftime("%H%M%S_%d_%m_%Y")
                                          + '.jpg')
        context.browser.save_screenshot(scenario_file_path)

def make_dir(dir):
    """
    Checks if directory exists, if not make a directory, given the directory path
    :param: <string>dir: Full path of directory to create
    """
    if not os.path.exists(dir):
      os.makedirs(dir)

def after_feature(context,feature):
    log.info("Executed feature is: "+feature.name)

def after_all(context):
     log.info("Shutting down browser...")
     context.browser.quit()





