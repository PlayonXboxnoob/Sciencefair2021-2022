import random
import time
from time import sleep
from RandomWordGenerator import RandomWord
import string
from RandModule import *
from RandLetterModule import *
import RandLetterModule
import RandModule
import threading as th


global rw
global low
global high
global nlimit



def bubbleSort(arr):
    start = time.time()
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):
        swapped = False

        # Last i elements are already
        #  in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to
            # n-i-1. Swap if the element
            # found is greater than the
            # next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # IF no two elements were swapped
        # by inner loop, then break
        if swapped == False:
            break
    end = time.time()

    print("Sorted array:")
    print(arr)
    timetaken = end-start
    print("The time it took to sort was : ")
    print(str(timetaken) + "seconds")
    return arr

bubbleSort(RandN(1, 1000, 100000))
