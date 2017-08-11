from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from behave import *
from features.support import helperMethods as hm
import yaml
import ipdb

p_stream = open('E:\Python-SeleniumFramework\python_behave_Framework\Params.YML', 'r')
p_data=yaml.load(p_stream)

@given('the user is on login page')
def step_impl(context):
    if hm.isExpectedTitleContains(context,"Mahara"):
        print("Landed on correct login page")
        assert True
    else:
        print("This is not login page")
        assert False

@then('he should land on the correct page')
def step_impl(context):
    if hm.isExpectedTitleContains(context,"Dashboard"):
        assert True
        print("Landed on correct page")
    else:
        print("This is not the desired page")
        assert False


@given('the user is on dashboard page')
def step_impl(context):
    if hm.isExpectedTitleContains(context,"Dashboard"):
        print("Landed on correct login page")
        assert True
    else:
        print("This is not login page")
        assert False

@then('he should land on the correct profile page')
def step_impl(context):
    # ipdb.set_trace()
    if hm.element(context,"ProfilePage","userTitleSection").text=="About me":
    # if context.browser.find_element_by_tag_name("h3").text=="About me":
        print("Landed on correct page")
        assert True
    else:
        print("This is not the desired page")
        assert False