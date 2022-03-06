import re
import reprlib

RE_WORD = re.compile(r"\w+")


class Sentence:
    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return f"Sentence({reprlib.repr(self.text)})"

    def __iter__(self):
        word_iter = RE_WORD.finditer(self.text)
        return SentenceIterator(word_iter)


class SentenceIterator:
    def __init__(self, word_iter):
        self.word_iter = word_iter

    def __next__(self):
        match = next(self.word_iter)
        return match.group()

    def __iter__(self):
        return self
