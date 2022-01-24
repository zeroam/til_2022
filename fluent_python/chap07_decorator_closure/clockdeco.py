import time
import functools


def clock(func):
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() - t0
        name = func.__name__

        arg_list = []
        if args:
            arg_list.append(", ".join(repr(arg) for arg in args))
        if kwargs:
            pairs = [f"{k!s}={w!r}" for k, w in kwargs.items()]
            arg_list.append(", ".join(pairs))
        arg_str = ", ".join(arg_list)

        print(f"[{elapsed:0.8f}] {name}({arg_str}) -> {result}")

        return result

    return clocked
