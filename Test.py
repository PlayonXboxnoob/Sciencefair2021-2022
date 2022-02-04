import random
import time
from time import sleep
import string
from RandModule import *
from selectionSort import *
from bubbleSort import *
from CombNumberSort import *
from quickSort import *
from insertionSort import *
from Verify import *
from datetime import datetime

alglist = {
#    'bubble': bubbleSort,
#    'selection': selectionSort,
#    'insertion': insertionSort,
    'quick': quickSort,
    'comb': combSort
          }

testList = [[1, 10000, 1000], [1, 10000, 5000], [1, 100000, 10000], [1, 1000000, 50000], [1, 10000000, 100000],
            [1, 1000000, 200000], [1, 1000000, 300000]]

testCount = 3

def runTest(totest, testList):


    timeTakenList = []
    numOpList = []

    for testToRun in testList:
        unsortedArray = RandN(testToRun[0], testToRun[1], testToRun[2])

        print("working in " + totest + 'sort for ' + str(testToRun[2]))
        print(datetime.now())
        sortedArray = unsortedArray.copy()
        start = time.time()
        sortedArray, numOp = alglist[totest](sortedArray)
        end = time.time()
        print("DONE " + totest + 'sort for ' + str(testToRun[2]))
        print(datetime.now())

        if not verify(unsortedArray, sortedArray):
            print('error in ' + totest + 'sort for ' + str(testToRun[2]))
            break
        else:
            timeTaken = round((end-start), 4)
            timeTakenList.append(timeTaken)
            numOpList.append(numOp)
            print('it took ' + str(timeTaken) + ' seconds')
            print('it took ' + str(numOp) + ' operations')

    return timeTakenList, numOpList

if __name__ == '__main__':

    for key in alglist.keys():

        f = open('output ' + key + 'sort.txt', 'w')
        fOp = open('number of operations ' + key + 'sort.txt', 'w')
        s = ''
        for test in testList:
            s = str(test[2]) + ','

        f.write(s)
        fOp.write(s)
        f.write('\n')
        fOp.write('\n')

        for i in range(testCount):
            timeArr, opArr = runTest(key, testList)
            s = ''
            for t in timeArr:
                s += str(t) + ', '
            f.write(s)
            f.write('\n')

            s = ''
            for p in opArr:
                s += str(t) + ', '
            f.write(s)
            f.write('\n')

        f.close()


