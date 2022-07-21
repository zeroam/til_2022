from collections import UserDict


class ExtendedDict_dict(dict):
    def apply(self, action):
        for key, value in self.items():
            self[key] = action(value)

    def remove(self, key):
        del self[key]

    def is_empty(self):
        return len(self) == 0


class ExtendedDict_UserDict(UserDict):
    def apply(self, action):
        for key, value in self.items():
            self[key] = action(value)

    def remove(self, key):
        del self[key]

    def is_empty(self):
        return len(self) == 0


if __name__ == "__main__":
    import timeit

    init_data = dict(zip(range(1000), range(1000)))

    dict_initialization = min(
        timeit.repeat(stmt="ExtendedDict_dict(init_data)", number=1000, repeat=5, globals=globals())
    )

    user_dict_initialization = min(
        timeit.repeat(stmt="ExtendedDict_UserDict(init_data)", number=1000, repeat=5, globals=globals())
    )

    print(f"UserDict is {user_dict_initialization / dict_initialization:.3f} times slower than dict")
