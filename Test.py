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

alglist = {
    'bubble': bubbleSort,
    'selection': selectionSort,
    'insertion': insertionSort,
    'quick': quickSort,
    'comb': combSort
          }

oodef runTest(totest, testList):


    timeTakenList = []
    numOpList = []

    for testToRun in testList:
        unsortedArray = RandN(testToRun[0], testToRun[1], testToRun[2])

        sortedArray = unsortedArray.copy()
        start = time.time()
        sortedArray, numOp = alglist[totest](sortedArray)
        end = time.time()

        if not verify(unsortedArray, sortedArray):
            print('error in ' + totest + 'sort for ' + str(testToRun[2]))
            break
        else:
            print("working in " + totest + 'sort for ' + str(testToRun[2]))
            timeTaken = round((end-start), 4)
            timeTakenList.append(timeTaken)
            numOpList.append(numOp)
            print('it took ' + str(timeTaken) + ' seconds')
            print('it took ' + str(numOp) + ' operations')

    return timeTakenList, numOpList

if __name__ == '__main__':

    testList = [[1, 10000, 1000], [1, 10000, 5000], [1, 100000, 10000], [1, 1000000, 50000], [1, 10000000, 100000],
                [1, 1000000, 200000], [1, 1000000, 300000]]

    for key in alglist.keys():

        f = open('output ' + key + 'sort.txt', 'w')
        fOp = open('number of operations ' + key + 'sort.txt', 'w')
        s = ''
        for test in testList:
            text = str(test[2]) + ','

        f.write(text)
        fOp.write(text)
        f.write('\n')
        fOp.write('\n')

        for i in range(3):
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


