"""
A "mirroring"" ``stdout`` context

While active, the context manager reverses text output to ``stdout``::

    >>> from mirror import LookingGlass
    >>> with LookingGlass() as what:
    ...     print('Alice, Kitty and Snowdrop')
    ...     print(what)
    ...
    pordwonS dna yttiK ,ecilA
    YKCOWREBBAJ
    >>> what
    'JABBERWOCKY'
    >>> print('Back to normal.')
    Back to normal.


This exposes the context manager operation::

    >>> from mirror import LookingGlass
    >>> manager = LookingGlass()
    >>> manager  # doctest: +ELLIPSIS
    <mirror.LookingGlass object at 0x...>
    >>> monster = manager.__enter__()
    >>> monster == 'JABBERWOCKY'
    eurT
    >>> monster
    'YKCOWREBBAJ'
    >>> manager  # doctest: +ELLIPSIS
    >... ta tcejbo ssalGgnikooL.rorrim<
    >>> manager.__exit__(None, None, None)
    >>> monster
    'JABBERWOCKY'



The context manager can handle and "swallow" exceptions.

    >>> from mirror import LookingGlass
    >>> with LookingGlass():
    ...     print('Humpty Dumpty')
    ...     x = 1/0
    ...     print('End')
    ytpmuD ytpmuH
    Please DO NOT divide by zero!
    >>> with LookingGlass():
    ...     print('Humpty Dumpty')
    ...     x = no_such_name
    ...     print('End')
    Traceback (most recent call last):
     ...
    NameError: name 'no_such_name' is not defined

"""
import sys


class LookingGlass:
    def __enter__(self):
        self.original_write = sys.stdout.write
        sys.stdout.write = self.reverse_write
        return "JABBERWOCKY"

    def reverse_write(self, text):
        self.original_write(text[::-1])

    def __exit__(self, exc_type, exc_value, traceback):
        sys.stdout.write = self.original_write
        if exc_type is ZeroDivisionError:
            print("Please DO NOT divide by zero!")
            return True
