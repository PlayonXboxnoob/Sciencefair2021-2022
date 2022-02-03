import sys
import random
import time
from time import sleep
import string
from RandModule import *


import RandModule
import threading as th
from Verify import *

def selectionSort(arr):
    n = range(0, len(arr) - 1) # the range meant to sort
    numOp = 0
    for i in n: # it is done sorting/going through the list the correct amount of times repeat
        low = i # first considers the lowest val as the first

        for j in range(i + 1, len(arr)):
            numOp += 1
            if arr[j] < arr[low]: # finds the actual lowest val
                low = j

        if low != i: # is the lowest val was changed then swap the two
            arr[low], arr[i] = arr[i], arr[low]


    return arr, numOp

if __name__ == '__main__':
    arr = RandN(1, 100, 10) # generate array
    print(arr) # print unsorted
    sorterdArray = arr.copy()
    sorterdArray, opNum = selectionSort(sorterdArray) # sort the list
    #print(sorterdArray)
    print(str(verify(arr, sorterdArray))) # verify if sorted list was correct
    print(arr) # print sorted list
    print(opNum)

