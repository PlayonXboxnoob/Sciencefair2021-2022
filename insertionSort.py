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
    for i in n:

        sortval = arr[i]

        while arr[i-1] > sortval and i > 0:

            arr[i], arr[i-1] = arr[i-1], arr[i]
            i = i-1

    return arr

if __name__ == '__main__':
    arr = RandN(1, 100, 10)
    print(arr)
    sorterdArray = arr.copy()
    sorterdArray = insertionSort(sorterdArray)
    print(sorterdArray)
    print(str(verify(arr, sorterdArray)))
    print(arr)



