# Card.py


class Card(object):
    """A simple playing card. A Card is characterized by two compoents:
    rank: an integer value in the range 1-13, inclusive(Ace-King)
    suit: a character in 'cdhs' for clubs, diamonds, hearts, and spades/"""

    _SUITS = 'cdhs'
    _SUIT_NAMES = ['clubs', 'diamonds', 'hearts', 'spades']

    _RANKS = range(1, 14)
    _RANK_NAMES = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six',
                   'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen',
                   'king']

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

    def __str__(card):
        return self.rankName() + " of " + self.suitName()
