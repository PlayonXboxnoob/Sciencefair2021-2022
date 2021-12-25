import random
import time
from time import sleep

global low
global high
global nlimit

def RandN(low, high, nlimit):
    RandomI_ListOfIntegers = [random.randrange(low, high) for iter in range(nlimit)]
    print("The unsorted list is:")
    print(RandomI_ListOfIntegers)
    return RandomI_ListOfIntegers











