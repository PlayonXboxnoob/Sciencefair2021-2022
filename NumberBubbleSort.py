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

    for i in range(n): # n is the length of the array
        swapped = False #It has not swapped anything yet

        for j in range(0, n-i-1):

            if arr[j] > arr[j+1]: # comparing the first value to the second, and swapping if greater than
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if swapped == False:
            break
    end = time.time()

    print("Sorted array:")
    print(arr)
    timetaken = end-start
    print("The time it took to sort was: ")
    print(str(timetaken) + "seconds")
    return arr

bubbleSort(RandN(1, 10, 5))




