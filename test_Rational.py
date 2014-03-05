# test_Rational.py
# unittest example

import sys
import unittest

sys.path.insert(0, '..')
from Rational import *


class RationalTest(unittest.TestCase):

    def testConstructorOneInt(self):
        r = Rational(-3)
        self.assertEqual(str(r), '-3/1')

    def testConstructorTwoInt(self):

        r = Rational(3, 4)
        self.assertEqual(str(r), '3/4')

    def testMul(self):

        r1 = Rational(2, 3)
        r2 = Rational(3, 4)
        r3 = r1 * r2
        self.assertEqual(str(r3), '6/12')


def main(argv):
    unittest.main()

if __name__ == '__main__':
    main(sys.argv)