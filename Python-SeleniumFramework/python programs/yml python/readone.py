import yaml

stream = open('E:\Python-SeleniumFramework\python programs\yml python\one.YML', 'r')  
data=yaml.load(stream)

def hello(p1,p2,p3):
    print(data["Browser"])
    print(data["URL"])
    val=data[p1][p2][p3]
    print(val)

hello("MainPage","SellProducts","value")