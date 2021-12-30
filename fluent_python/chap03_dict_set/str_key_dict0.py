import pytest


class StrKeyDict0(dict):
    def __missing__(self, key):
        if isinstance(key, str):
            # 비교를 안하면 무한 재귀로 돌게 됨
            raise KeyError(key)
        return self[str(key)]

    def get(self, key, default=None):
        try:
            # missing 메서드는 __contains__ 메서드에는 영향을 미치지 않기 때문에
            # if key in self 으로 비교하면 안됨
            return self[key]  # 만약 없으면 우선 __missing__ 호출
        except KeyError:
            return default

    def __contains__(self, key):
        # 만약 str(key) in self 으로 호출하게 되면 무한 재귀
        return key in self.keys() or str(key) in self.keys()


def test_str_key():
    d = StrKeyDict0([("2", "two"), ("4", "four")])

    assert d["2"] == "two"
    assert d[4] == "four"

    with pytest.raises(KeyError):
        d[1]


def test_str_key_get():
    d = StrKeyDict0([("2", "two"), ("4", "four")])

    assert d.get("2") == "two"
    assert d.get(4) == "four"
    assert d.get(1, "N/A") == "N/A"


def test_str_key_in():
    d = StrKeyDict0([("2", "two"), ("4", "four")])

    assert 2 in d
    assert 1 not in d
