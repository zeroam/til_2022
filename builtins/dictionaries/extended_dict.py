class ExtendedDict(dict):
    def apply(self, action):
        for key, value in self.items():
            self[key] = action(value)

    def remove(self, key):
        del self[key]

    def is_empty(self):
        return len(self) == 0


def test_extended_dict():
    numbers = ExtendedDict({"one": 1, "two": 2, "three": 3})

    assert numbers == {"one": 1, "two": 2, "three": 3}


def test_extended_dict_apply():
    numbers = ExtendedDict({"one": 1, "two": 2, "three": 3})

    numbers.apply(lambda x: x**2)

    assert numbers == {"one": 1, "two": 4, "three": 9}


def test_extended_dict_remove():
    numbers = ExtendedDict({"one": 1, "two": 2, "three": 3})

    numbers.remove("two")

    assert numbers == {"one": 1, "three": 3}


def test_extended_dict_is_empty():
    numbers = ExtendedDict({"one": 1, "two": 2, "three": 3})

    assert numbers.is_empty() == False
