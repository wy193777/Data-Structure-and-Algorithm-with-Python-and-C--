# Rational.py
# demonstrates operator overloading


class Rational(object):

    def __init__(self, num=0, den=1):

        """creates a new Rational object
        pre: num and den are integers
        post: creates the Rational object num / den"""

        self.num = num
        self.den = den

    def __mul__(self, other):
        """* operator
        pre: self and other are Rational objects
        post: returns Rational product: self * self"""

        num = self.num * other.num
        den = self.den * other.den
        return Rational(num, den)

    def __str__(self):
        """return string for printing
        pre: self is Rational object
        post: returns a string representation of self"""
        return str(self.num) + "/" + str(self.den)