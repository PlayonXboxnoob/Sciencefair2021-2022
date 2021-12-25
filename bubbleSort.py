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



def BubbleSort(arr):
    start = time.time()
    n = len(arr)

    for passes in range(n):
        swapped = False

        for i in range(n-passes-1):

            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True

        if swapped == False:
            break
    end = time.time()
    timetaken = end-start
    print(timetaken)
    return arr

x= BubbleSort(RandN(1, 1000, 1000))
print()
print("The sorted array is: ")
print(x)
