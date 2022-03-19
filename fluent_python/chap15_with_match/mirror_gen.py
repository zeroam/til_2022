"""
A "mirroring" ``stdout`` context manager.

While active, the context manager reverses text output to ``stdout``::

    >>> from mirror_gen import looking_glass
    >>> with looking_glass() as what:
    ...     print('Alice, Kitty and Snowdrop')
    ...     print(what)
    pordwonS dna yttiK ,ecilA
    YKCOWREBBAJ
    >>> what
    'JABBERWOCKY'
    >>> print('back to normal')
    back to normal


This exposes the context manager operation::

    >>> from mirror_gen import looking_glass
    >>> manager = looking_glass()
    >>> manager  # doctest: +ELLIPSIS
    <contextlib._GeneratorContextManager object at 0x...>
    >>> monster = manager.__enter__()
    >>> monster == 'JABBERWOCKY'
    eurT
    >>> monster
    'YKCOWREBBAJ'
    >>> manager  # doctest: +ELLIPSIS
    >...x0 ta tcejbo reganaMtxetnoCrotareneG_.biltxetnoc<
    >>> manager.__exit__(None, None, None)
    False
    >>> monster
    'JABBERWOCKY'


The decorated generator also works as a decorator:

    >>> @looking_glass()
    ... def verse():
    ...     print('The time has come')
    ...
    >>> verse()
    emoc sah emit ehT
    >>> print('back to normal')
    back to normal

"""
import contextlib
import sys


@contextlib.contextmanager
def looking_glass():
    original_write = sys.stdout.write

    def reverse_write(text):
        original_write(text[::-1])

    sys.stdout.write = reverse_write
    yield 'JABBERWOCKY'
    sys.stdout.write = original_write
