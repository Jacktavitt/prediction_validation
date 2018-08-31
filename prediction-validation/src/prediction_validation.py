import sys
import time
from decimal import *
from collections import OrderedDict
import HelperMethods as HM


def main(argv):
    with open(argv[1],'r') as wf:
        window=int(wf.read())
    # stick data into memory since other way took too long and was wrong
    with open(argv[2],'r') as af:
        actualData = HM.makeDictionary(af.read())
    with open(argv[3],'r') as pf:
        predictedData = HM.makeDictionary(pf.read())
    # del predictedData[None]
    try:
        predictedKeys=HM.sortedKeys(predictedData)
    except TypeError as e:
        print(e)
        sys.exit()
    
    resultDict = {}
    for hour in predictedKeys:
        # gives us sequential access to hours
        # so have numbers n ... n+n
        # need to calculate diff between two dictionaries
        hourError, numError = HM.diffDictionaries(predictedData[hour], \
                                actualData[hour])
        resultDict[hour] = (hourError, numError)

    head = predictedKeys[0]
    tail = head+window-1

    with open(sys.argv[4],'w') as outFile:
        while tail <= predictedKeys[-1]:
            missingT, missingH = False, False
            try:
                headIndex = predictedKeys.index(head)
            except ValueError as e:
                missingH = True
            try:
                tailIndex = predictedKeys.index(tail)
            except ValueError as e:
                missingT = True

            errorTotal = sum([resultDict[e][0] for e in predictedKeys[headIndex:tailIndex+1]])
            numErrors = sum([resultDict[e][1] for e in predictedKeys[headIndex:tailIndex+1]])
            if missingT and missingH:
                windowError = 'NA'
                outFile.write("{}|{}|{}\n".format(head, tail, windowError))
                missingT, missingH = False, False
            else:
                windowError = errorTotal/numErrors
                outFile.write("{}|{}|{:.2f}\n".format(head, tail, windowError))
            head+=1
            tail+=1

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Please specify time window, actual data, predicted data, and output files")
        raise SystemExit(1)
    main(sys.argv)