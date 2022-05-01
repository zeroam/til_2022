import traceback


def simple_coro2(a):
    print("-> Started: a =", a)
    b = yield a
    print("-> Received: b =", b)
    c = yield a + b
    print("-> Received: c =", c)


if __name__ == "__main__":
    from inspect import getgeneratorstate

    my_coro2 = simple_coro2(14)
    print(getgeneratorstate(my_coro2))  # 'GEN_CREATED'
    print(next(my_coro2))
    print(getgeneratorstate(my_coro2))  # 'GEN_SUSPENDED'
    print(my_coro2.send(28))  # b

    try:
        print(my_coro2.send(99))  # c
    except StopIteration:
        print(traceback.format_exc())

    print(getgeneratorstate(my_coro2))  # 'GEN_CLOSED'
