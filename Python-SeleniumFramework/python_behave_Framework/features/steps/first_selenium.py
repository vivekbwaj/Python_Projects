from behave import *
from behave import step
from features.support import helperMethods as hm
import yaml
import ipdb
import logging
import features.support.custom_logger as cl

log = cl.customLogger(logging.DEBUG)
p_stream = open('E:\Python-SeleniumFramework\python_behave_Framework\Params.YML', 'r')
p_data=yaml.load(p_stream)

# use_step_matcher("re")

@when('the user enters the credentials and logs in')
def step_impl(context):
    hm.enterText(context,"LoginPage","username",p_data["UserName"])
    hm.enterText(context, "LoginPage", "password", p_data["Password"])
    hm.clickOn(context,"LoginPage","loginButton")
    log.info("[the user enters the credentials and logs in] > Done")

@when('user clicks the user profile icon')
def step_impl(context):
    hm.clickOn(context,"Dashboard","profileUserIcon")



