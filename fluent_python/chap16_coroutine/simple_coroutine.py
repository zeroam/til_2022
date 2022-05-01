import traceback


def simple_coroutine():
    print("-> coroutine started")
    x = yield
    print("-> coroutine received:", x)


if __name__ == "__main__":
    my_coro = simple_coroutine()
    print(my_coro)
    next(my_coro)  # equals to 'my_coro.send(None)'
    try:
        my_coro.send(42)
    except StopIteration:
        print(traceback.format_exc())

    my_coro = simple_coroutine()
    try:
        # error when generator is in state 'GEN_CREATED'
        my_coro.send(1729)
    except Exception:
        print(traceback.format_exc())
