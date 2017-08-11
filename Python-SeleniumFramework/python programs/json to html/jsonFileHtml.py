import pandas as pd
import numpy as np

#json read object
my_read_json=pd.read_json("results.json")

#json to html
pdhtml=pd.DataFrame.to_html(my_read_json)

#create html file
my_html = open('myHtml.html','w')
my_html.write(pdhtml)
my_html.close()