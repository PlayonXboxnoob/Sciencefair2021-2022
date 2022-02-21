import random
import time
from time import sleep
import string
from datetime import datetime
from RandModule import *
from selectionSort import *
from bubbleSort import *
from CombNumberSort import *
from quickSort import *
from insertionSort import *
from Verify import *

alglist = {
    'quick': quickSort,
    'comb': combSort,
    'bubble': bubbleSort,
    'selection': selectionSort,
    'insertion': insertionSort
}

testList = [[1, 10000, 1000], [1, 10000, 5000], [1, 100000, 10000], [1, 1000000, 50000], [1, 10000000, 100000],
            [1, 1000000, 200000], [1, 1000000, 300000]]

testCount = 10

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

    for key in alglist.keys(): # run for each sorting method

        f = open('output ' + key + 'sort.txt', 'w') # file to store the time
        fOp = open('number of operations ' + key + 'sort.txt', 'w') # files to store number of comparisons
        s = ''
        for test in testList:   # first write the test number in the files
            s += str(test[2]) + ','

        f.write(s)
        fOp.write(s)
        f.write('\n')
        fOp.write('\n')

        for i in range(testCount):  # write test data in the files
            timeArr, opArr = runTest(key, testList)
            s = ''
            for t in timeArr:   # write time for sorting in the file
                s += str(t) + ', '
            f.write(s)
            f.write('\n')

            s = ''
            for p in opArr: # write number of comparisons in the file
                s += str(p) + ', '
            fOp.write(s)
            fOp.write('\n')

        f.close()
        fOp.close()


