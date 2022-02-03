import sys
import random
import time
from time import sleep
import string
from RandModule import *
import RandModule
import threading as th
from Verify import *




def bubbleSort(arr):
    n = len(arr) # setting n to length of the list or arr
    numOp = 0
    for passes in range(n):  # until it has gone through the list as many times as numbers there are, repeat

        for i in range(n-passes-1): # Keep comparing until it has gone through the part of the list that the computer thinks is  "unsorted"

            numOp += 1
            if arr[i] > arr[i+1]: # if the first number is larger than the second, then swap, if not then don't
                arr[i], arr[i+1] = arr[i+1], arr[i]


    return arr, numOp


if __name__ == '__main__':  # Testing
    arr = RandN(1, 100, 10)
    print(arr)
    sorterdArray = arr.copy()
    sorterdArray, opNum = bubbleSort(sorterdArray)
    print(sorterdArray)
    print(str(verify(arr, sorterdArray)))
    print(arr)
    print(opNum)