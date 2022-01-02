import random
import time
from time import sleep
import string
from RandModule import *
from Verify import *

def quickSort(arr):
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

        else:
            lower.append(num)



    return quickSort(lower) + [mid] + quickSort(higher)

if __name__ == '__main__':
    arr = RandN(1, 100, 10)
    print(arr)
    sorterdArray = arr.copy()
    sorterdArray = quickSort(sorterdArray)
    print(sorterdArray)
    print(str(verify(arr, sorterdArray)))
    print(arr)



