import sys
import csv
import configparser
from datetime import datetime as dt
from datetime import timedelta as td

## custom file
import CompareCSV as cmprUtil
import IOFileUtil as fileUtil

##Read from the config file
config = configparser.ConfigParser()
config.read('config.ini')

## Instruments filter
filterInstrument= config['CSV-FILTER']['INSTRUMENTS']
filterDateTime = int(config['CSV-FILTER']['EXPIRY-DATE-DELTA'])
filepath1 = "testData/fo13APR2018bhav.csv";
filepath2 = "testData/fo12APR2018bhav.csv"
tempDict1 = {}
tempDict2 = {}

## Iterate on every row of csv
## to create an associated list
def readCSV(filepath):
    try:
        with open(filepath) as file:
            reader = csv.DictReader(file)
            tempDict = {}
            for idx,row in enumerate(reader):
                if(idx != 0 and row['INSTRUMENT'] == filterInstrument
                and dt.strptime(row['EXPIRY_DT'],"%d-%b-%Y") < dt.now()+td(days=filterDateTime)):
                    list = [row['OPEN'],row['CLOSE'],row['HIGH'],row['LOW']]
                    if row['SYMBOL'] not in row.keys() :
                        tempDict[row['SYMBOL']] = list
                    else:
                        raise ValueError('MULTIPE-IDENTICAL-SYMBOLS')
            return tempDict
    except IOError:
        print(''' The program encountered an IO error \n Please check the input file '''+ filepath);
        sys.exit();
    except ValueError:
        if ValueError.args == 'MULTIPE-IDENTICAL-SYMBOLS':
            print('''The program has encountered an value error. \n Multiple identical symbols encountered.\n
            The program will consider the last value of the symbol''')
        else:
            print(''' The program encountered an Value error \n Please check the column name in the CSV file '''+ filepath)
            sys.exit();
    except KeyError:
        print(''' The program encountered a Key error. \n Please check the column names in the CSV file. '''+ filepath)
        sys.exit();


## Call read file utility with the path of the csv file
## filePath1 is the latest
tempDict1=readCSV(filepath1)
tempDict2 = readCSV(filepath2)
## call compare utility
cmprUtil.createResultCSV(tempDict1, tempDict2)
fileUtil.generateUrlForCSV();
