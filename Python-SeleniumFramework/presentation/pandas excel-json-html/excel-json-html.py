import pandas as pd
import numpy as np

#excel to json
myExcel=pd.read_excel("test.xls")
print(myExcel)
my_json=myExcel.to_json("my.json")

#json read object
my_read_json=pd.read_json("my.json")

#json to html
pdhtml=pd.DataFrame.to_html(my_read_json)

#create html file
my_html = open('myHtml.html','w')
my_html.write(pdhtml)
my_html.close()


# pd.read_json(fileName,orient="values")._get_values[1][1]
# pd.read_json(fileName).keys()[2]