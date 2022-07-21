from click import pass_obj


class ValueDict(dict):
    def key_of(self, value):
        for k, v in self.items():
            if v == value:
                return k
        raise ValueError(value)

    def keys_of(self, value):
        for k, v in self.items():
            if v == value:
                yield k


def test_value_dict():
    inventory = ValueDict()
    inventory["apple"] = 2
    inventory["banana"] = 3
    inventory.update({"orange": 2})

    assert inventory == {"apple": 2, "banana": 3, "orange": 2}
    assert inventory.key_of(2) == "apple"
    assert inventory.key_of(3) == "banana"
    assert list(inventory.keys_of(2)) == ["apple", "orange"]
