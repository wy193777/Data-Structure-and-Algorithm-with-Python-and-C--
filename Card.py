# Card.py


class Card(object):
    """A simple playing card. A Card is characterized by two compoents:
    rank: an integer value in the range 1-13, inclusive(Ace-King)
    suit: a character in 'cdhs' for clubs, diamonds, hearts, and spades/"""

    SUITS = 'cdhs'
    SUIT_NAMES = ['clubs', 'diamonds', 'hearts', 'spades']

    RANKS = range(2, 15)
    RANK_NAMES = ['Two', 'Three', 'Four', 'Five', 'Six',
                   'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen',
                   'king', 'Ace']

    def __init__(self, rank, suit):
        """Constructor
        pre: rank in range(1, 14) and suit in 'cbhs'
        post: self has the given rank and suit"""
        self.rank_num = rank
        self.suit_char = suit

    def rank(self):
        return self.rank_num

    def suit(self):
        return self.suit_char

    def suitName(self):
        index = self.SUITS.index(self.suit_char)
        return self.SUIT_NAMES[index]

    def rankName(self):
        index = self.RANKS.index(self.rank_num)
        return self.RANK_NAMES[index]

    def __eq__(self, other):
        return (self.suit_char == other.suit_char and
                self.rank_num == other.rank_num)

    def __lt__(self, other):
        if self.suit_char == other.suit_char:
            return self.rank_num < other.rank_num
        else:
            return self.suit_char < other.suit_char

    def __ne__(self, other):
        return not(self == other)

    def __le__(self, other):
        return self < other or self == other

    def __str__(self):
        return self.rankName() + " of " + self.suitName()

from Card import *

c = Card(2, 'c')

print(str(c))