"""수치형 흉내내기"""
from math import hypot


class Vector:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector ({self.x}, {self.y})"

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other: 'Vector'):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar: int):
        return Vector(self.x * scalar, self.y * scalar)

    def __eq__(self, other: 'Vector'):
        return self.x == other.x and self.y == other.y


"""Test Codes"""

def test_repr():
    assert repr(Vector(3, 5)) == "Vector (3, 5)"


def test_eq():
    assert Vector(3, 5) == Vector(3, 5)


def test_abs():
    assert abs(Vector(3, 4)) == 5


def test_bool():
    assert bool(Vector(0, 0)) == False
    assert bool(Vector(0, 1)) == True


def test_add():
    a = Vector(3, 5)
    b = Vector(5, 2)
    assert a + b == Vector(8, 7)


def test_mul():
    v = Vector(3, 4)
    assert v * 3 == Vector(9, 12)
    assert abs(v * 3) == 15
