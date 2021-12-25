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



def combSort(arr):
    start = time.time()
    gap=len(arr)
    swapped = True
    temp=0
    while gap!=1 or swapped == True:
        swapped=False
        # reducing gap by a factor of 1.3
        gap = int(gap/1.3)
        if gap < 1:
            gap=1
        for i in range(0, len(arr)-gap):
            if arr[i] > arr[i + gap]:
                temp=arr[i]
                arr[i]=arr[i + gap]
                arr[i + gap]=temp
                swapped = True
    end = time.time()
    print("Sorted array: ")
    print(arr)
    timetaken = end - start
    print("The time it took to sort was: ")
    print(str(timetaken) + "seconds")
    return arr

combSort(RandN(1, ))