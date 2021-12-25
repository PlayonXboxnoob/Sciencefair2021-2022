import random
import time
from time import sleep
from RandomWordGenerator import RandomWord
import string
from RandModule import *
from RandLetterModule import *
import RandLetterModule
import RandModule
from SelectionNumberSort import *
from NumberBubbleSort import *
from CombNumberSort import *
from InsertionSort import *
from MergeNumberSort import *

global rw
global low
global high
global nlimit

def Verify():
    inputrecog = False

    while inputrecog == False:
        alg = input("Which Algorithm? ")
        ListofNumbers = RandN(1, 1000, 10)

        if alg == "bubbleSort":
            testarr = bubbleSort(ListofNumbers)
            inputrecog = True
        if alg == "selectionSort":
            testarr = SelectionSort(ListofNumbers)
            inputrecog = True
        if alg == "combSort":
            testarr = combSort(ListofNumbers)
            inputrecog = True
        if alg == "insertionSort":
            testarr = insertionSort(ListofNumbers)
            inputrecog = True
        if alg == "mergeSort":
            testarr = mergeSort(ListofNumbers, len(ListofNumbers)/2, len(ListofNumbers)/2)
            inputrecog = True

    reallist = ListofNumbers
    reallist = reallist.sort()
    print(reallist)