from collections import UserDict


class UpperCaseDict(UserDict):
    def __setitem__(self, key, value):
        key = key.upper()
        super().__setitem__(key, value)


def test_init():
    numbers = UpperCaseDict({"one": 1, "two": 2, "three": 3})

    assert numbers == {"ONE": 1, "TWO": 2, "THREE": 3}


def test_set_item():
    numbers = UpperCaseDict()

    numbers["one"] = 1
    numbers["two"] = 2
    numbers["three"] = 3

    assert numbers == {"ONE": 1, "TWO": 2, "THREE": 3}


def test_update():
    numbers = UpperCaseDict({"one": 1, "two": 2, "three": 3})

    numbers.update({"four": 4})

    assert numbers == {"ONE": 1, "TWO": 2, "THREE": 3, "FOUR": 4}


def test_set_default():
    numbers = UpperCaseDict({"one": 1, "two": 2, "three": 3})

    numbers.setdefault("four", 4)

    assert numbers == {"ONE": 1, "TWO": 2, "THREE": 3, "FOUR": 4}
