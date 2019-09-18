import random
from Card_class import *

#Fisher-Yates Algorithm
def shuffle(ary):
    a = len(ary)
    b = a - 1
    for d in range(b,0,-1):
      e = random.randint(0,d)
      if e == d:
            continue
      ary[d],ary[e] = ary[e],ary[d]
    return ary

#The function can print all 52 Card object in card array
def print_CardArray(array):
    for i in range(len(array)):
        print(array[i].value,"-",array[i].suit)

def convert_to_int(array):
    for i in range(len(array)):
        array[i].str_to_int()

def convert_to_str(array):
    for i in range(len(array)):
        array[i].int_to_str()
