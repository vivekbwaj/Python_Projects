import yaml

stream = open('E:\Python-SeleniumFramework\pytest\dataDriven\yaml\\dd_1.YML', 'r')
data=yaml.load(stream)
row=[]

def hello(p1):
    row.append(data[p1])

def getValues():
    return row
def getDt():
    return data["Language"]




