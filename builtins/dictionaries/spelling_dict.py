from collections import UserDict


UK_TO_US = {"colour": "color", "flavour": "flavor", "behaviour": "behavior"}


class EnglishSpelledDict(UserDict):
    def __getitem__(self, key):
        try:
            return super().__getitem__(key)
        except KeyError:
            pass
        try:
            return super().__getitem__(UK_TO_US[key])
        except KeyError:
            pass
        raise KeyError(key)

    def __setitem__(self, key, value):
        try:
            key = UK_TO_US[key]
        except KeyError:
            pass
        super().__setitem__(key, value)


def test_likes():
    likes = EnglishSpelledDict({"color": "blue", "flavour": "vanilla"})

    assert likes == {"color": "blue", "flavor": "vanilla"}
    assert likes["flavour"] == "vanilla"
    assert likes["flavor"] == "vanilla"

    likes["behaviour"] = "polite"
    assert likes == {"color": "blue", "flavor": "vanilla", "behavior": "polite"}

    assert likes.get("colour") == "blue"
    assert likes.get("color") == "blue"

    likes.update({"behaviour": "gentle"})
    assert likes == {"color": "blue", "flavor": "vanilla", "behavior": "gentle"}
