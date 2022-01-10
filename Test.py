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
               'insertion': insertionSort

               #'comb': combSort
        }
#'quick': quickSort,

def test(totest):


    timeTakenList = []

    testList = [[1, 10000, 1000], [1, 100000, 10000], [1, 1000000, 100000]]#, [1, 10000000, 1000000], [1, 2000000000, 100000000]]
    for testToRun in testList:
        unsortedArray = RandN(testToRun[0], testToRun[1], testToRun[2])

        sortedArray = unsortedArray.copy()
        start = time.time()
        sortedArray = alglist[totest](sortedArray)
        end = time.time()

        if not verify(unsortedArray, sortedArray):
            print('error in ' + totest + 'sort for ' + str(testToRun[2]))
            break
        else:
            print("working in " + totest + 'sort for ' + str(testToRun[2]))
            timeTaken = round((end-start), 4)
            timeTakenList.append(timeTaken)
            print('it took ' + str(timeTaken) + ' seconds')

    return timeTakenList

if __name__ == '__main__':

    for key in alglist.keys():

        f = open('output ' + key + 'sort.txt', 'w')

        for i in range(10):
            timeArr = test(key)
            s = ''
            for t in timeArr:
                s += str(t) + ', '
            f.write(s)
            f.write('\n')

        f.close()


