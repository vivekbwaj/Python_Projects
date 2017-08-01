import csv
import  pandas as pd

def getJSONData(fileName):
    # create an empty list to store rows
    rows = []
    # open the CSV file
    # myJson = pd.read_json(fileName)
    myJson=pd.read_json(fileName,orient="values")._get_values
    for row in myJson:
        rows.append(row)
    return rows

# print(getJSONData("E:\Python-SeleniumFramework\pytest\dataDriven\json\\myjson.json"))
# print(getJSONData("E:\Python-SeleniumFramework\pytest\dataDriven\json\\myjson.json").__len__())
# print(getJSONData("E:\Python-SeleniumFramework\pytest\dataDriven\json\\myjson.json")[0])
# print(getJSONData("E:\Python-SeleniumFramework\pytest\dataDriven\json\\myjson.json")[1])

# print(getJSONData("E:\Python-SeleniumFramework\pytest\dataDriven\json\\myjson.json"))