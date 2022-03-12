def f():
    def do_yield(n):
        yield n
    x = 0
    while True:
        x += 1
        yield from do_yield(x)


if __name__ == "__main__":
    print("Invoking f() now produces a generator")
    g = f()
    print(next(g))
    print(next(g))
    print(next(g))
