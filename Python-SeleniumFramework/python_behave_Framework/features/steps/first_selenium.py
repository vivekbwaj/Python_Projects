from behave import *
from features.support import helperMethods as hm

# use_step_matcher("re")

@given('I open flipkart website')
def step_impl(context):
    context.browser.get("https://www.flipkart.com/")

@then('I print the title')
def step_impl(context):
   if hm.isExpectedTitleContains(context, "Shopping"):
       hm.element(context, "MainPage", "SearchProducts").send_keys("some text")
       hm.element(context,"MainPage","SellProducts").click()




