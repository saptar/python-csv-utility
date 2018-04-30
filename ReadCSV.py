import sys
import csv
import configparser
from datetime import datetime as dt
from datetime import timedelta as td


##Read from the config file
config = configparser.ConfigParser()
config.read('config.ini')

## Instruments filter
filterInstrument= config['CSV-FILTER']['INSTRUMENTS']
filterDateTime = int(config['CSV-FILTER']['EXPIRY-DATE-DELTA'])
filepath="testData/fo13APR2018bhav.csv";

## Iterate on every row of csv
## to create an associated list
def readCSV(filepath):
    try:
        with open(filepath) as file:
            reader = csv.DictReader(file)
            for idx,row in enumerate(reader):
                if(idx != 0 and row['INSTRUMENT'] == filterInstrument
                and dt.strptime(row['EXPIRY_DT'],"%d-%b-%Y") < dt.now()+td(days=filterDateTime)):
                    print(row['SYMBOL'] + "  "+row['OPEN']+"  "+row['CLOSE']+"  "+row['HIGH']
                    +"  "+row['LOW'])
    except IOError:
        print(''' The program encountered an IO error \n Please check the input file '''+ filepath);
        sys.exit();
    except ValueError:
        print(''' The program encountered an Value error \n Please check the column name in the CSV file '''+ filepath)
        sys.exit();
    except KeyError:
        print(''' The program encountered a Key error. \n Please check the column names in the CSV file. '''+ filepath)
        sys.exit();

## Call read file utility with the path of the csv file
readCSV(filepath)