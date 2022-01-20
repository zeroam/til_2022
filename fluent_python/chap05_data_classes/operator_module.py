import operator
from functools import reduce
from operator import mul, itemgetter, methodcaller


def fact(n):
    # return reduce(lambda a, b: a * b, range(1, n + 1))
    return reduce(mul, range(1, n + 1))


if __name__ == "__main__":
    ### mul ###
    print("fact(5):", fact(5))
    print()

    ### itemgetter ###
    metro_data = [
        ("Tokyo", "JP", 36.933),
        ("Delhi NCR", "IN", 21.935),
        ("Mexico City", "MX", 20.142),
        ("New York-Newark", "US", 20.104),
        ("Sao Paulo", "BR", 19.694),
    ]
    # for city in sorted(metro_data, key=lambda x: x[1]):
    for city in sorted(metro_data, key=itemgetter(1)):
        print(city)
    print()

    cc_name = itemgetter(1, 0)
    for city in metro_data:
        print(cc_name(city))
    print()

    ### methodcaller ###
    s = "The time has come"
    upcase = methodcaller("upper")
    print(upcase(s))
    hiphenate = methodcaller("replace", " ", "-")
    print(hiphenate(s))


    # operator funcs
    print([name for name in dir(operator) if not name.startswith("_")])
    print()
