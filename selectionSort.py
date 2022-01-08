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
    n = range(0, len(arr) - 1)

    for i in n:
        low = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[low]:
                low = j

        if low != i:
            arr[low], arr[i] = arr[i], arr[low]


    return arr

if __name__ == '__main__':
    arr = RandN(1, 100, 10)
    print(arr)
    sorterdArray = arr.copy()
    sorterdArray = selectionSort(sorterdArray)
    print(sorterdArray)
    print(str(verify(arr, sorterdArray)))
    print(arr)

