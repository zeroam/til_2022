import collections

class StrKeyDict(collections.UserDict):
    def __missing__(self, key):
        if isinstance(key ,str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, key: object) -> bool:
        return str(key) in self.data

    def __setitem__(self, key, item) -> None:
        self.data[str(key)] = item


"""
transformdict:
- https://github.com/fluentpython/example-code-2e/blob/master/03-dict-set/transformdict.py
"""
