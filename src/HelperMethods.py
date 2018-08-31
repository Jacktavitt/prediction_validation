import decimal

def splitLine(line):
    '''splits |-delimeted line into values'''
    if line:
        line=line.split('|')
        return int(line[0]), line[1], decimal.Decimal(line[2])
    else:
        return None, None, None

def makeDictionary(allData):
    '''create dictionary, keys are hours, 
    values are dictionaries of values
    '''
    allData = allData.strip().split('\n')
    valDict = {}
    for el in allData:
        hour, name, value = splitLine(el)
        try:
            valDict[hour][name]=value
        except KeyError as e:
            valDict[hour]={name:value}
    return valDict

def sortedKeys(valDict):
    '''returns sorted list of keys.
    used only for predicted data'''
    # print("vd: {}".format())
    
    keyList = list(valDict.keys())
    # print("kl: {}".format(keyList))
    keyList.sort()
    return keyList
        
def diffDictionaries(d1,d2):
    '''compare two dictionaries. only use keys from d1'''
    totalDiff = 0
    numDiff = len(d1)
    for key in d1:
        totalDiff+=abs(d1[key]-d2[key])
    return totalDiff, numDiff