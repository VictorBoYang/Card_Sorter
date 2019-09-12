# Python Program to shuffle a given array
import random
from Card_class import *

def shuffle(ary):
    a=len(ary)
    b=a-1
    for d in range(b,0,-1):
      e=random.randint(0,d)
      if e == d:
            continue
      ary[d],ary[e]=ary[e],ary[d]
    return ary

#Creating Array
Value = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
Suit = ["H","D","C","S"]
card_array = [Card("1","1")] * 52#creat one array with 52 Card Object
for i,value in enumerate(Value):
    for j,suit in enumerate(Suit):
            card_array[i*4+j] = Card(value,suit)
# shuffle array and output
shuffle(card_array)
for x in range(len(card_array)):
    print(card_array[x].value,"-",card_array[x].suit)
