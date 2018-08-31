import sys
from decimal import *
getcontext().prec = 2

def parseValue(line, delim = '|'):
    ''' splits a line delimited by 'delim' into an integer, a name, and a float 
        Args:
            line: string, such as '1|CMWTQH|81.22'
            delim: delimeter, such as '|'
        Returns:
            hour, name, and value
    '''
    if line:
        line=line.split(delim)
        hour = int(line[0])
        name = line[1]
        value = Decimal(line[2])
        return (hour,name,value)
    else:
        return (None,None,None)


def slidingWindow(resultDict, window, outFile):
    ''' performs sliding window error calculations on
        a dictionary of error values
        Args:
            resultDict: dictionary or error values.
                keys are hours, values are tuples of
                (numberOfComparisons,totalError)
            window: size of sliding window
            outFile: output file object

        Must not break when an hour is missing!
    '''
    hours = list(resultDict.keys())
    hours.sort
    # print("rd: {}\nhours: {}".format(resultDict, hours))
    head=hours[0] # fisrt hour in sorted list
    tail=head+window-1 # window-th hour in sorted list
    while tail<=hours[-1]: # while we aren't over the last hour
        try:
            headIndex = hours.index(head)
        except ValueError as e:
            # print(e)
            # the next hour is not in the list.
            # skip it and keep going
            pass
        try:
            tailIndex = hours.index(tail)
        except ValueError as e:
            # print(e)
            # the next hour is not in the list.
            # skip it and keep going
            pass
        if headIndex == tailIndex: # we're missing more hours than the window
            head+=1 # increment head and tail
            tail+=1
            continue # don't write anything
        numErrors = sum([resultDict[e][0] for e in \
                hours[headIndex:tailIndex+1]])
        errorTotal = sum([resultDict[e][1] for e in \
                hours[headIndex:tailIndex+1]])
        windowError = errorTotal/numErrors
        # print("winerr: {}, sumerr: {}, numerr: {}"
        #         .format(windowError,errorTotal,numErrors))
        outFile.write("{}|{}|{:.2f}\n".format(head, tail, windowError))
        head+=1
        tail+=1





def loopWithBreaks(filename1, filename2):
    hour = 1
    f1 = open(filename1)
    line1 = f1.readline()
    f2 = open(filename2)
    line2 = f2.readline()
    while line1 or line2:
        f1l=[]
        f2l=[]
        # line1 = f1.readline()
        while True:
            rh = int(line1[0]) if line1 else None
            # print("{}".format(line1))
            if rh != hour or line1 == '':
                # we are done reading for this hour
                print("Done reading for predicted hour {}\n{}\n".format(hour,f1l))
                break
            f1l.append(line1)
            line1 = f1.readline()
        # line2 = f2.readline()
        while True:
            rh = int(line2[0]) if line2 else None
            # print("{}".format(line2))
            if rh != hour or line2 == '':
                print("Done reading for actual hour {}\n{}\n".format(hour,f2l))
                break
            f2l.append(line2)
            line2 = f2.readline()
        hour +=1
    f1.close()
    f2.close()

    if __name__ == "__main__":
        loopWithBreaks(sys.argv[1],sys.argv[2])