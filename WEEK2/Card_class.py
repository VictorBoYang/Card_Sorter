class Card:
    def __init__(self,value_in,suit_in):
        self.value = value_in
        self.suit = suit_in

    def get_value(self):
        return self.value

    def get_suit(self):
        return self.suit

    def str_to_int(self):
        if self.value == "J":
            self.value = "11"
        elif self.value == "Q":
            self.value = "12"
        elif self.value == "K":
            self.value = "13"
        elif self.value == "A":
            self.value = "14"
        if self.suit == "C":
            self.suit = "1"
        elif self.suit == "D":
            self.suit = "2"
        elif self.suit == "H":
            self.suit = "3"
        elif self.suit == "S":
            self.suit = "4"
        self.value = int(self.value)
        self.suit = int(self.suit)

    def int_to_str(self):
        if self.value == 11:
            self.value = "J"
        elif self.value == 12:
            self.value = "Q"
        elif self.value == 13:
            self.value = "K"
        elif self.value == 14:
            self.value = "A"
        if self.suit == 1:
            self.suit = "C"
        elif self.suit == 2:
            self.suit = "D"
        elif self.suit == 3:
            self.suit = "H"
        elif self.suit == 4:
            self.suit = "S"
        self.value = str(self.value)
        self.suit = str(self.suit)
