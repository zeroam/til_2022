from functools import singledispatch
from collections import abc
import numbers
import html


@singledispatch
def htmlize(obj):
    content = html.escape(repr(obj))
    return f'<pre>{content}</pre>'


@htmlize.register(str)
def _(text):
    content = html.escape(text).replace('\n', '<br>\n')
    return f'<p>{content}</p>'


@htmlize.register(numbers.Integral)
def _(n):
    return f'<pre>{n} (0x{n:x})</pre>'


@htmlize.register(tuple)
@htmlize.register(abc.MutableSequence)
def _(seq):
    inner = '</li>\n</li>'.join(htmlize(item) for item in seq)
    return '<ul>\n<li>' + inner + '</li>\n</ul>'


if __name__ == "__main__":
    print(htmlize({1, 2, 3}))
    print()
    print(htmlize(abs))
    print()
    print(htmlize('Heimlich & Co.\n- a game'))
    print()
    print(htmlize(42))
    print()
    print(htmlize(['alpha', 66, {3, 2, 1}]))
    print()
