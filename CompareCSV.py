import configparser
import WriteCSV as wtUtil
## file level global vars
dictToWriteDL = {}
dictToWriteDH = {}
## read config file
##Read from the config file
config = configparser.ConfigParser()
config.read('config.ini')
## code to compare two list
def compareEachSymbol(a, b):
    try:
        delta = 0
        ## the list contains following value in order
        ## OPEN-CLOSE-HIGH-LOW
        if float(a[1]) < float(config['SLAB-RATE']['RATE-A']):
            delta =float(config['SLAB-RATE']['RATE-A-DELTA'])
            returnVal = ''
            if(abs(float(a[2])-float(b[2])) <= delta):
                ## consider for DH
                returnVal = 'DH'
            if (abs(float(b[3])-float(a[3])) <= delta):
                ## consider for DL
                returnVal +='DL'
            else:
                return 'PASS'
            return returnVal
        elif float(a[1]) < float(config['SLAB-RATE']['RATE-B']) and float(a[1])>float(config['SLAB-RATE']['RATE-A']):
            delta = float(config['SLAB-RATE']['RATE-B-DELTA'])
            returnVal = ''
            if(abs(float(a[2])-float(b[2])) <= delta):
                ## consider for DH
                returnVal = 'DH'
            if (abs(float(b[3])-float(a[3])) <= delta):
                ## consider for DL
                returnVal += 'DL'
            else:
                return 'PASS'
            return returnVal
        elif float(a[1]) < float(config['SLAB-RATE']['RATE-C']) and float(a[1])>float(config['SLAB-RATE']['RATE-B']):
            delta = float(config['SLAB-RATE']['RATE-C-DELTA'])
            returnVal = ''
            if(abs(float(a[2])-float(b[2])) <= delta):
                ## consider for DH
                returnVal ='DH'
            if (abs(float(b[3])-float(a[3])) <= delta):
                ## consider for DL
                returnVal +='DL'
            else:
                return 'PASS'
            return returnVal
        elif float(a[1]) < float(config['SLAB-RATE']['RATE-D']) and float(a[1])>float(config['SLAB-RATE']['RATE-C']):
            delta = float(config['SLAB-RATE']['RATE-D-DELTA'])
            returnVal = ''
            if(abs(float(a[2])-float(b[2])) <= delta):
                ## consider for DH
                returnVal +='DH'
            if (abs(float(b[3])-float(a[3])) <= delta):
                ## consider for DL
                returnVal += 'DL'
            else:
                return 'PASS'
            return returnVal
        elif float(a[1]) < float(config['SLAB-RATE']['RATE-E']) and float(a[1])>float(config['SLAB-RATE']['RATE-D']):
            delta = float(config['SLAB-RATE']['RATE-E-DELTA'])
            returnVal = ''
            if(abs(float(a[2])-float(b[2])) <= delta):
                ## consider for DH
                returnVal = 'DH'
            if (abs(float(b[3])-float(a[3])) <= delta):
                ## consider for DL
                returnVal += 'DL'
            else:
                return 'PASS'
            return returnVal
    except ValueError:
        print('''Value error encountered in compareEachSymbol method''')
    except IndexError:
        print('''Index error encountered in compareEachSymbol method''')
## code to compare two set of dictionaries
## and create a new csv with DL and DH
def createResultCSV(first,second):
    try:
        if len(first.keys()) != len(second.keys()):
            raise ValueError('MISMATCH-KEYS')
        print('''Number of keys in the incoming files '''+str(len(first.keys())))
        for key in first:
            result = compareEachSymbol(first[key], second[key])
            if result == 'DH':
                ## write to DH dict
                dictToWriteDH[key] = first[key]
            elif result == 'DL':
                ## write to DL dict
                dictToWriteDL[key] = first[key]
            elif result == 'DHDL':
                ## write to both the dict
                dictToWriteDH[key] = first[key]
                dictToWriteDL[key] = first[key]
            else:
                continue
        wtUtil.writeDictToCSV(dictToWriteDL, second)
        print('''Number of keys in the outgoing files '''+str(len(dictToWriteDL.keys())))
    except ValueError:
        print('''Value error encountered in createResultCSV''')
    except KeyError:
        print('''Key error encountered in createResultCSV''')