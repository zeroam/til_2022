"""
Sentence: access words by index

    >>> text = 'To be, or not to be, that is the question'
    >>> s = Sentence(text)
    >>> len(s)
    10
    >>> s[1], s[5]
    ('be', 'be')
    >>> s
    Sentence('To be, or no... the question')

"""
import re
import reprlib

RE_WORD = re.compile(r"\w+")


class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __getitem__(self, index):
        return self.words[index]

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return f"Sentence({reprlib.repr(self.text)})"
