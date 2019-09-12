# Python Program to shuffle a given array
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
def print_CardArray(array,length):
    for i in range(length):
        print(array[i].value,"-",array[i].suit)

# The function for creating Card array
def create_CardArray(value_array,suit_array,card_array):
    for i,value in enumerate(value_array):
        for j,suit in enumerate(suit_array):
                card_array[i*4+j] = Card(value,suit)

#Creating Array
Value = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
Suit = ["H","D","C","S"]
card_array = [Card("1","1")] * 52#creat one array with 52 Card Object
create_CardArray(Value,Suit,card_array)

# shuffle array and output
print("shffling")
shuffle(card_array)
print("shuffle finished")
print_CardArray(card_array,len(card_array))

#sorting
print("sorting starts")
