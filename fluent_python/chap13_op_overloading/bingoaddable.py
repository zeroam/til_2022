"""
======================
AddableBingoCage tests
======================


Tests for __add__:

    >>> vowels = 'AEIOU'
    >>> globe = AddableBingoCage(vowels)
    >>> globe.inspect()
    ('A', 'E', 'I', 'O', 'U')
    >>> globe.pick() in vowels
    True
    >>> len(globe.inspect())
    4
    >>> globe2 = AddableBingoCage('XYZ')
    >>> globe3 = globe + globe2
    >>> len(globe3.inspect())
    7
    >>> void = globe + [10, 20]
    Traceback (most recent call last):
    ...
    TypeError: unsupported operand type(s) for +: 'AddableBingoCage' and 'list'


Tests for __iadd__:

    >>> globe_orig = globe
    >>> len(globe.inspect())
    4
    >>> globe += globe2
    >>> len(globe.inspect())
    7
    >>> globe += ["M", "N"]
    >>> len(globe.inspect())
    9
    >>> globe is globe_orig
    True
    >>> globe += 1
    Traceback (most recent call last):
    ...
    TypeError: right operand in += must be 'Tombola' or an iterable

"""
from tombola import Tombola
from bingo import BingoCage


class AddableBingoCage(BingoCage):
    def __add__(self, other):
        if isinstance(other, Tombola):
            return AddableBingoCage(self.inspect() + other.inspect())
        else:
            return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, Tombola):
            other_iterable = other.inspect()
        else:
            try:
                other_iterable = iter(other)
            except TypeError:
                msg = "right operand in += must be 'Tombola' or an iterable"
                raise TypeError(msg)
        self.load(other_iterable)
        return self
