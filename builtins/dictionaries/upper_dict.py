class UpperCaseDict(dict):
    def __init__(self, mapping=None, /, **kwargs):
        if mapping is not None:
            mapping = {str(key).upper(): value for key, value in mapping.items()}
        else:
            mapping = {}
        if kwargs:
            mapping.update({str(key).upper(): value for key, value in kwargs.items()})
        super().__init__(mapping)

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


def test_update_not_working():
    numbers = UpperCaseDict({"one": 1, "two": 2, "three": 3})

    numbers.update({"four": 4})

    assert numbers == {"ONE": 1, "TWO": 2, "THREE": 3, "four": 4}


def test_set_default_not_working():
    numbers = UpperCaseDict({"one": 1, "two": 2, "three": 3})

    numbers.setdefault("four", 4)

    assert numbers == {"ONE": 1, "TWO": 2, "THREE": 3, "four": 4}
