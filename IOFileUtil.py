##import requests
##import zipfile
##import StringIO
import configparser
from datetime import datetime as dt
from datetime import timedelta as delta


config = configparser.ConfigParser()
config.read('config.ini')

## global variables
todayUrl = ''
yesterdayUrl = ''

## generate the url
## eg url https://www.nseindia.com/content/historical/DERIVATIVES/2018/APR/fo19APR2018bhav.csv.zip
def generateUrlForCSV():
    urlString = config['DOWNLOAD-URL']['CSV-DOWNLOAD-URL']
    todayDateString = dt.now().strftime('%b/%d/%Y')
    ystDate = dt.now()+ delta(days=-1)
    ystDateString = ystDate.strftime('%b/%d/%Y')
    dateComponent = todayDateString.split('/')
    todayUrl = urlString .format(year=dateComponent[2], month=dateComponent[0].upper(),filename=(dateComponent[1]+dateComponent[0]+dateComponent[2]))
    print(todayUrl)



## code to download and extract the csv file.
def downloadAndExtractCSV():
    r = requests.get(zip_file_url, stream=True)
    z = zipfile.ZipFile(StringIO.StringIO(r.content))
    z.extractall()