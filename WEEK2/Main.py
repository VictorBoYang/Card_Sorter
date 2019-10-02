# Python Program to shuffle a given array
from function_storage import *
from sorting_storage import *
# The function for creating Card array
def create_CardArray(value_array,suit_array,card_array):
    for i,value in enumerate(value_array):
        for j,suit in enumerate(suit_array):
                card_array[i*4+j] = Card(value,suit)

#Creating Array
Value = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
Suit = ["H","D","C","S"]
card_array = [Card("","")] * 52#creat one array with 52 Card Object
create_CardArray(Value,Suit,card_array)

# shuffle array and output
print("shffling")
shuffle(card_array)
print("shuffle finished")
print_CardArray(card_array)

#convert JQKA,HDCS TO INT TYPE,EASY TO OPERATE
convert_to_int(card_array)
print("sorting by value starts:")
recursive_bubble_sorting_value(card_array,len(card_array))
convert_to_str(card_array)
print_CardArray(card_array)
print("sorting by value finished")
#sorting

print("sorting starts")
convert_to_int(card_array)
#bubble_sorting(card_array)
recursive_bubble_sorting(card_array,len(card_array))
print("sorting finsihed")
#print_CardArray(card_array)

#convert INT TYPE BACK TO JQKA,HDCS
convert_to_str(card_array)

#final result
print_CardArray(card_array)
