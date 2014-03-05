# Deck.py
from random import randrange
from Card import Card


class Deck(object):

    def __init__(self):
        cards = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                cards.append(Card(rank, suit))
        self.cards = cards

    def size(self):
        return len(self.card)

    def deal(self):
        return self.cards.pop()

    def shuffle(self):
        cards0 = self.cards
        cards1 = []
        while cards0 != []:
            pos = randrange(len(cards0))
            card = cards0.pop(pos)
            cards1.append(card)

        self.cards = cards1

    def sort(self):
        cards0 = self.cards
        cards1 = []
        while cards0 != []:
            next_card = max(cards0)
            cards0.remove(next_card)
            cards1.append(next_card)
        self.cards = cards1

        #self.cards.sort()
        #self.cards.reverse()

