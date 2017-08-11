from behave import *
from features.support import helperMethods as hm


@given('I put {item_thing} in a blender,')
def step_impl(context,item_thing):
    print(item_thing)

@when(u'I switch the blender on')
def step_impl(context):
    print("Blender On..")

@then(u'it should transform into {item_other}')
def step_impl(context,item_other):
    print(item_other)
