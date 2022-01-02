import random
from RandomWordGenerator import RandomWord
import time
from time import sleep
import string

def RandL(Llimit, Letters):
    rw = RandomWord(Letters, True)
    RandomI_ListOfLetters = rw.getList(Llimit)
    return RandomI_ListOfLetters

def LetGen(LetterLimit, WordLetters):
    datasetl = RandL(LetterLimit, WordLetters)



