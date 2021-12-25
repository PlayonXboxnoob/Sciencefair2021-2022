import sys
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


def SelectionSort(arr):
    start = time.time()

    #SortedList = [0]
    for i in range(len(arr)):

        # Find the minimum element in remaining
        # unsorted array
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j

        # Swap the found minimum element with
        # the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    end = time.time()

    # Driver code to test above
    print("Sorted array: ")
    print(arr)
    timetaken = end - start
    print("The time it took to sort was : ")
    print(str(timetaken) + "seconds")
    return arr

