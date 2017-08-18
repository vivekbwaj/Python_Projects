import requests
from pprint import pprint
# units=metric is used for temp in celsius
loc="3149,aus"
api_key="f0b5be6d019423d8251b9d6614df8ef9"
temp_units="metric"
res=requests.get("http://api.openweathermap.org/data/2.5/weather?q="+loc+"&APPID="+api_key+"&units="+temp_units+"")

respJ=res.json()
# pprint(respJ)
print("Current temp: {},  Min temp:{}, Max temp:{}".format(respJ["main"]['temp'],respJ["main"]['temp_min'],respJ["main"]['temp_max']))
print(respJ["name"])
print(respJ["weather"][0]["description"])



