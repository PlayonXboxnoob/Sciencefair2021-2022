import random
import time
from time import sleep
import string
from RandModule import *
from Verify import *

global numOperations
numOperations = 0

def quickSort(arr):
    global numOperations
    return quickSortInner(arr), numOperations

def quickSortInner(arr):
    global numOperations
    n = len(arr)
    if n < 1 or n == 1:
        return arr
    else:
        mid = arr.pop(int(n/2))

    higher = []
    lower = []

    for num in arr:
        if num > mid:
            higher.append(num)
            numOperations += 1
        else:
            lower.append(num)
            numOperations += 1



    return quickSortInner(lower) + [mid] + quickSortInner(higher)

if __name__ == '__main__':
    arr = RandN(1, 100, 10)
    print(arr)
    sorterdArray = arr.copy()
    sorterdArray, opNum = quickSort(sorterdArray)
    print(sorterdArray)
    print(str(verify(arr, sorterdArray)))
    print(arr)
    print(opNum)



