# Deck.py
import random
from Card import Card


class Deck(object):

    def __init__(self):
        cards = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                cards.append(Card(rank, suit))
        self.cards = cards

    def size(self):
        return len(self.cards)

    def deal(self):
        return self.cards.pop()

    def shuffle(self):
        #cards0 = self.cards
        #cards1 = []
        #while cards0 != []:
            #pos = randrange(len(cards0))
            #card = cards0.pop(pos)
            #cards1.append(card)

        #self.cards = cards1
        random.shuffle(self.cards)

    def sort(self):
        cards0 = self.cards
        cards1 = []
        while cards0 != []:
            next_card = max(cards0)
            cards0.remove(next_card)
            cards1.append(next_card)
        self.cards = cards1

    def addTop(self, card):
        self.cards.insert(0, card)

    def addBottom(self, card):
        self.cards.append(card)

    def addRandom(self, card):
        card.insert(random.randrange(len(card), card))

    def __str__(self):
        deck = []
        for card in self.cards:
            deck.append(card.rankName() + " of " + card.suitName())
        return "\n".join(deck)


d = Deck()
print(d)
print(d.size())
d.shuffle()
print(d)