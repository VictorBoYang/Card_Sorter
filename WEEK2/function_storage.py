import random
from Card_class import *

#Fisher-Yates Algorithm
def shuffle(ary):
    a=len(ary)
    b=a-1
    for d in range(b,0,-1):
      e=random.randint(0,d)
      if e == d:
            continue
      ary[d],ary[e]=ary[e],ary[d]
    return ary

#The function can print all 52 Card object in card array
def print_CardArray(array):
    for i in range(len(array)):
        print(array[i].value,"-",array[i].suit)


def convert_to_int(array):
    for i in range(len(array)):
        if array[i].value == "J":
            array[i].value = "11"
        elif array[i].value == "Q":
            array[i].value = "12"
        elif array[i].value == "K":
            array[i].value = "13"
        elif array[i].value == "A":
            array[i].value = "14"
        if array[i].suit == "C":
            array[i].suit = "1"
        elif array[i].suit == "D":
            array[i].suit = "2"
        elif array[i].suit == "H":
            array[i].suit = "3"
        elif array[i].suit == "S":
            array[i].suit = "4"

def convert_to_str(array):
    for i in range(len(array)):
        if array[i].value == "11":
            array[i].value = "J"
        elif array[i].value == "12":
            array[i].value = "Q"
        elif array[i].value == "13":
            array[i].value = "K"
        elif array[i].value == "14":
            array[i].value = "A"
        if array[i].suit == "1":
            array[i].suit = "C"
        elif array[i].suit == "2":
            array[i].suit = "D"
        elif array[i].suit == "3":
            array[i].suit = "H"
        elif array[i].suit == "4":
            array[i].suit = "S"


#Bubble sorting
def bubble_sorting(array):
    for i in range(len(array)):
        for j in range(len(array)-1):
            if int(array[j].value) > int(array[j+1].value):#This if will sort by Card.value
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
            if int(array[j].value) == int(array[j+1].value):#This if will sorted by Card.suit
                if int(array[j].suit) > int(array[j+1].suit):
                    temp = array[j]
                    array[j] = array[j+1]
                    array[j+1] = temp
