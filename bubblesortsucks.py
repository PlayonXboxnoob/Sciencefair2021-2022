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


def bubblesort(arr, ascendio=True):
    n = len(arr)
    Truearr = []
    Falsearr = []

    for passes in range(n):

        for i in range(n-passes-1):

            if ascendio:
                if arr[i] > arr[i+1]:
                    arr[i], arr[i+1] = arr[i+1], arr[i]
                Truearr = arr
            else:
                if arr[i] < arr[i+1]:
                    arr[i], arr[i+1] = arr[i+1], arr[i]
                Falsearr = arr
    if ascendio:
        return Truearr
    else:
        return Falsearr

bruh = RandN(1, 10, 5)
x = bubblesort(bruh)
y= bubblesort(bruh, False)

print()
print(x)
print()
print(y)


