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

#Bubble sorting
def bubble_sorting(array):
    for i in range(len(array)):
        for j in range(len(array)-1):
            if array[j].value > array[j+1].value:#This if will sort by Card.value
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
            if array[j].value == array[j+1].value:#This if will sorted by Card.suit
                if array[j].suit > array[j+1].suit:
                    temp = array[j]
                    array[j] = array[j+1]
                    array[j+1] = temp
