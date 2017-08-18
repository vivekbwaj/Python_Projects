from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from behave import *
from termcolor import colored
from features.support import helperMethods as hm
import ipdb
import yaml
import logging
import features.support.custom_logger as cl


log = cl.customLogger(logging.DEBUG)
p_stream = open('E:\Python-SeleniumFramework\python_behave_Framework\Params.YML', 'r')
p_data=yaml.load(p_stream)

@given('the user is on login page')
def step_impl(context):
    if hm.isExpectedTitleContains(context,"Mahara"):
        log.info("Landed on correct login page")
        assert True
    else:
        log.info("This is not login page")
        assert False

@then('he should land on the correct page')
def step_impl(context):
    if hm.isExpectedTitleContains(context,"Dashboard"):
        log.info("Landed on correct dashboard page")
        assert True
    else:
        log.info("This is not the desired dashboard page")
        assert False


@given('the user is on dashboard page')
def step_impl(context):
    if hm.isExpectedTitleContains(context,"Dashboard"):
        log.info("On dashboard page")
        assert True
    else:
        log.info("This is not dashboard page")
        assert False

@then('he should land on the correct profile page')
def step_impl(context):
    if hm.element(context,"ProfilePage","editProfilelink") is not None:
        log.info("[he should land on the correct profile page]> Done")
        assert True
    else:
        log.info("[he should land on the correct profile page]> Failed")
        assert False