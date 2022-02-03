import random
import time
from time import sleep

import string
from RandModule import *

import RandModule
import threading as th
from Verify import *

def insertionSort(arr):
    n = range(1, len(arr))
    numOp = 0
    for i in n:

        sortval = arr[i]

        while arr[i-1] > sortval and i > 0:
            numOp += 1
            arr[i], arr[i-1] = arr[i-1], arr[i]
            i = i-1

    return arr, numOp

if __name__ == '__main__':
    arr = RandN(1, 100, 10)
    print(arr)
    sorterdArray = arr.copy()
    sorterdArray, opNum = insertionSort(sorterdArray)
    print(sorterdArray)
    print(str(verify(arr, sorterdArray)))
    print(arr)
    print(opNum)



