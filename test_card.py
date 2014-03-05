# test_card.py
# unittest card

import sys
import unittest

sys.path.insert(0, '..')
from Card import *


class CardTest(unittest.TestCase):

    def testStr(self):
        c = Card(1, 'c')
        self.assertEqual(str(c), 'Ace of clubs')

    def testRank(self):
        c = Card(1, 'c')
        self.assertEqual(c.rank(), 1)

    def testSuit(self):
        c = Card(1, 'c')
        self.assertEqual(c.suit(), 'c')

    def testsuitName(self):
        c = Card(1, 'c')
        self.assertEqual(c.suitName(), 'clubs')


def main(argv):
    unittest.main()

if __name__ == '__main__':
    main(sys.argv)