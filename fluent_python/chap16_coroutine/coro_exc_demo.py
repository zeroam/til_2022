"""
# Activating and closing without an exception
>>> exc_coro = demo_exc_handling()
>>> next(exc_coro)
-> coroutine started
>>> exc_coro.send(11)
-> coroutine received: 11
>>> exc_coro.send(22)
-> coroutine received: 22
>>> exc_coro.close()
>>> from inspect import getgeneratorstate
>>> getgeneratorstate(exc_coro)
'GEN_CLOSED'

# Throwing DemoException does not break it
>>> exc_coro = demo_exc_handling()
>>> next(exc_coro)
-> coroutine started
>>> exc_coro.send(11)
-> coroutine received: 11
>>> exc_coro.throw(DemoException)
*** DemoException handled. Continuing...
>>> getgeneratorstate(exc_coro)
'GEN_SUSPENDED'

# Coroutine terminates if it can't handle an exception thrown into it
>>> exc_coro = demo_exc_handling()
>>> next(exc_coro)
-> coroutine started
>>> exc_coro.send(11)
-> coroutine received: 11
>>> exc_coro.throw(ZeroDivisionError)
Traceback (most recent call last):
    ...
ZeroDivisionError
>>> getgeneratorstate(exc_coro)
'GEN_CLOSED'
"""


class DemoException(Exception):
    """An exception type for the demonstration."""


def demo_exc_handling():
    print("-> coroutine started")
    while True:
        try:
            x = yield
        except DemoException:
            print("*** DemoException handled. Continuing...")
        else:
            print("-> coroutine received: {!r}".format(x))
    raise RuntimeError("This line should never run.")
