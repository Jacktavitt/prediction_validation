import decimal

class StockData():
    '''Class to wrap data read from a file of actual
    or predicted stock prices by hour.
    '''
    def __init__(allData):
        self.allData = allData
        self.makeDictionary()

    def __getitem__(self, key):
        '''allows access to dicitonary'''
        return self.valDict[key]

    def splitLine(self, line):
        '''splits |-delimeted line into values'''
        if line:
            line=line.split('|')
            return int(line[0]), line[1], decimal.Decimal(line[2])
        else:
            return None, None, None

    def makeDictionary(self):
        '''create dictionary, keys are hours, 
        values are dictionaries of values
        '''
        self.allData = self.allData.split('\n')
        self.valDict = {}
        for el in self.allData:
            hour, name, value = self.splitLine(el)
            try:
                self.valDict[hour][name]=value
            except KeyError as e:
                self.valDict[hour]={name:value}

    def sortedKeys(self):
        '''returns sorted list of keys.
        used only for predicted data'''
        self.keyList = list(self.valDict.keys())
        self.keyList.sort()
        return self.keyList
        