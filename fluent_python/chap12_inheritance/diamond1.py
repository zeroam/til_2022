"""
diamond1.py: Demo of diamond-shaped class graph

>>> Leaf.__mro__  # doctest:+NORMALIZE_WHITESPACE
(<class 'diamond1.Leaf'>, <class 'diamond1.A'>, <class 'diamond1.B'>, <class 'diamond1.Root'>, <class 'object'>)

>>> leaf1 = Leaf()
>>> leaf1.ping()
<instance of Leaf>.ping() in Leaf
<instance of Leaf>.ping() in A
<instance of Leaf>.ping() in B
<instance of Leaf>.ping() in Root

>>> leaf1.pong()
<instance of Leaf>.pong() in A
<instance of Leaf>.pong() in B

"""


class Root:
    def __init__(self):
        self.count = 0

    def ping(self):
        print(f"{self}.ping() in Root")

    def pong(self):
        print(f"{self}.pong() in Root")

    def __repr__(self):
        cls_name = type(self).__name__
        return f"<instance of {cls_name}>"


class A(Root):
    def ping(self):
        print(f"{self}.ping() in A")
        super().ping()

    def pong(self):
        print(f"{self}.pong() in A")
        super().pong()


class B(Root):
    def ping(self):
        print(f"{self}.ping() in B")
        super().ping()

    def pong(self):
        print(f"{self}.pong() in B")


class Leaf(A, B):
    def ping(self):
        print(f"{self}.ping() in Leaf")
        super().ping()


if __name__ == "__main__":
    l = Leaf()
    print("ping::")
    l.ping()
    print(l.count)
    print("pong::")
    l.pong()
    print("mro::")
    print(Leaf.__mro__)
