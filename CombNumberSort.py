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
from Verify import *

def combSort(arr):
    gap=len(arr)
    swapped = True
    temp=0
    while gap != 1 or swapped == True:
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
    return arr

if __name__ == '__main__':
    arr = RandN(1, 100, 10)
    print(arr)
    sorterdArray = arr.copy()
    sorterdArray = combSort(sorterdArray)
    print(sorterdArray)
    print(str(verify(arr, sorterdArray)))
    print(arr)