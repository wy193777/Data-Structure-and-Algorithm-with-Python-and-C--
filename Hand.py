# Hand.py


class Hand(object):

    def __init__(self, label=""):
        self.label = label
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def dump(self):
        print(self.label + "'s Cards:")
        for c in self.cards:
            print("   ", c)


from Hand import Hand
from Card import Card


h = Hand("North")
h.add(Card(5, "c"))
h.add(Card(10, "d"))
h.add(Card(13, "s"))
h.dump()