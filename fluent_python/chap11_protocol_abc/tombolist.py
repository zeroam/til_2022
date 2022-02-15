from random import randrange

from tombola import Tombola


@Tombola.register
class TomboList(list):
    def pick(self):
        if self:
            position = randrange(len(self))
            return self.pop(position)
        else:
            raise LookupError("pop from empty TomboList")

    load = list.extend

    def loaded(self):
        return bool(self)

    def inspect(self):
        return tuple(self)


def test_issubclass():
    assert issubclass(TomboList, Tombola)


def test_isinstance():
    t = TomboList(range(100))
    assert isinstance(t, Tombola)


def test_mro():
    # not exist <Tombola> class in TomboList.__mro__
    assert TomboList.__mro__ == (TomboList, list, object)
