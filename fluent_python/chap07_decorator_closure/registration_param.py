registry = set()


def register(active=True):
    def decorator(func):
        print(f"running register(active={active}) -> decorator({func})")
        if active:
            registry.add(func)
        else:
            registry.discard(func)

        return func
    return decorator


@register(active=False)
def f1():
    print("running f1()")


@register(active=True)
def f2():
    print("running f2()")


def f3():
    print("running f3()")


def main():
    print("running main()")
    print("registry ->", registry)
    f1()
    f2()
    f3()


if __name__ == "__main__":
    main()
