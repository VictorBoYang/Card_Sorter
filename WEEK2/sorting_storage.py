from Card_class import *

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

# recursive bubble sorting
def recursive_bubble_sorting(array,len):
    if len == 0:
        return
    for j in range(len - 1):
        if array[j].value > array[j+1].value:#This if will sort by Card.value
            temp = array[j]
            array[j] = array[j+1]
            array[j+1] = temp
        if array[j].value == array[j+1].value:#This if will sorted by Card.suit
            if array[j].suit > array[j+1].suit:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
    recursive_bubble_sorting(array,len-1)
