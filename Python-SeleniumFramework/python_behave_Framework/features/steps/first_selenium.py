from behave import *
from features.support import helperMethods as hm
import yaml

p_stream = open('E:\Python-SeleniumFramework\python_behave_Framework\Params.YML', 'r')
p_data=yaml.load(p_stream)

# use_step_matcher("re")

@when('the user enters the credentials and logs in')
def step_impl(context):
    hm.element(context,"LoginPage","username").send_keys(p_data["UserName"])
    hm.element(context, "LoginPage", "password").send_keys(p_data["Password"])
    hm.element(context,"LoginPage","loginButton").click()

@when('user clicks the user profile icon')
def step_impl(context):
    hm.element(context,"Dashboard","profileUserIcon").click()



