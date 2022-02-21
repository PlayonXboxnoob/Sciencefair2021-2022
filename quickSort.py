import random
import time
from time import sleep
import string
from RandModule import *
from Verify import *

global numOperations
numOperations = 0

# Outer quicksort function, it is used only to calculate
# number of operations
def quickSort(arr):
    global numOperations
    numOperations = 0
    return quickSortInner(arr), numOperations

# Inner quicksort function, actual code
def quickSortInner(arr):
    global numOperations
    n = len(arr)
    if n < 1 or n == 1: # If this is array of size 1 then return
        return arr
    else:
        mid = arr.pop(int(n/2)) # else take the middle number

    higher = []
    lower = []

    # pivot the array into lower and higher arrays around middle number
    for num in arr: 
        if num > mid:
            higher.append(num)
            numOperations += 1
        else:
            lower.append(num)
            numOperations += 1
            
    # recursively call the same function until done
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



