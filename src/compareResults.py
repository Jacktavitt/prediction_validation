import sys
import HelperMethods as HM
import decimal

def main(argv):
    '''compares my results with documented results, checking for +-0.01 difference'''
    with open(argv[1],'r') as uf:
        userResults = uf.read()
    with open(argv[2],'r') as cf:
        referenceResults = cf.read()
    with open(argv[3],'w') as outFile:
        outFile.write("Comparing {} and {}".format(argv[1],argv[2]))
        print("Comparing {} and {}".format(argv[1],argv[2]))
        userResults = userResults.strip().split('\n')
        referenceResults = referenceResults.strip().split('\n')

        for u,r in zip(userResults,referenceResults):
            if u != r:
                if abs( (decimal.Decimal(u.split('|')[2])) - (decimal.Decimal(r.split('|')[2])) ) > 0.1 :
                    outFile.write("User: {}, Reference: {}".format(u,r))
                    print("User: {}, Reference: {}".format(u,r))

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Please specify user-created output, reference output, and file for comparison output. ")
        raise SystemExit(1)
    main(sys.argv)