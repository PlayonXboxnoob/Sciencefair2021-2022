import sys
import random
import time
from time import sleep

import string
from RandModule import *

import RandModule
import threading as th
from Verify import *


def bubbleSort(arr, ascendio=True):
    n = len(arr)

    for passes in range(n):

        for i in range(n-passes-1):

            if ascendio:
                if arr[i] > arr[i+1]:
                    arr[i], arr[i+1] = arr[i+1], arr[i]
            else:
                if arr[i] < arr[i+1]:
                    arr[i], arr[i+1] = arr[i+1], arr[i]

    return arr

if __name__ == '__main__':
    arr = RandN(1, 100, 10)
    print(arr)
    sorterdArray = arr.copy()
    sorterdArray = bubbleSort(sorterdArray)
    print(sorterdArray)
    print(str(verify(arr, sorterdArray)))
    print(arr)