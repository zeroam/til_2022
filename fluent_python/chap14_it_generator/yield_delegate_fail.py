def f():
    def do_yield(n):
        yield n
    x = 0
    while True:
        x += 1
        do_yield(x)


if __name__ == "__main__":
    print("Invoking f() results in an infinite loop")
    f()
