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

def insertionSort(arr):
    # Traverse through 1 to len(arr)
    start = time.time()
    for i in range(1, len(arr)):

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    end = time.time()
    timetaken = end - start
    print("Sorted array:")
    print(arr)
    print("The time it took to sort was : ")
    print(str(timetaken) + "seconds")
    return arr


