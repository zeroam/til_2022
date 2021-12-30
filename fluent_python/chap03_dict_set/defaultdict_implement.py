class DefaultDict(dict):
    def __init__(self, func):
        self.func = func

    def __missing__(self, key):
        if key not in self:
            self[key] = self.func()
        return self[key]


def test_defaultdict_list():
    d = DefaultDict(list)

    assert d["a"] == []

    d["b"].append(5)
    assert d["b"] == [5]


def test_defaultdict_dict():
    d = DefaultDict(dict)

    assert d["a"] == {}

    d["b"]["c"] = 5
    assert d["b"] == {"c": 5}
