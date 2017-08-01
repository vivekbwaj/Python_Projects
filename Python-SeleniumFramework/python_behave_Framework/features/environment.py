from selenium import webdriver
import yaml

stream = open('E:\Python-SeleniumFramework\python_behave_Framework\Params.YML', 'r')
data=yaml.load(stream)

URL=data["URL"]

if data["Browser"]=="firefox":
    browser = webdriver.Firefox()

elif data["Browser"]=="chrome":
    browser=webdriver.Ie()
elif data["Browser"] == "chrome":
    browser=webdriver.Edge()
else:
    browser=webdriver.Chrome()

def before_all(context):
     print("Executing before all")
     context.browser=browser


def before_feature(context, feature):
     print("Before feature")
     context.browser.get(URL)

#Scenario level objects are popped off context when scenario exits
def before_scenario(context,scenario):
    print("Before scenario")

def after_scenario(context,scenario):
    print("After scenario")

def after_feature(context,feature):
     print("After feature")
     # context.browser.quit()

def after_all(context):
     print("Executing after all")


