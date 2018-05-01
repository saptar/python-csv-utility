import csv
import sys

def writeDictToCSV(a,b):
    tempDict = {}
    ## create a temp Dict
    for k in a:
        tempList = a[k].insert(0,k)
        tempDict[k] = tempList
        a[k].extend(b[k])
    with open('testData/testCSV.csv','w+') as f:
        w = csv.writer(f)
        w.writerow(['SYMBOL','OPEN','CLOSE','HIGH','LOW','POPEN','PCLOSE','PHIGH','PLOW'])
        w.writerows(a.values())
