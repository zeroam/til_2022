from ctypes import sizeof
from dataclasses import dataclass


@dataclass
class SimplePosition:
    name: str
    lon: float
    lat: float


@dataclass
class SlotPosition:
    __slots__ = ["name", "lon", "lat"]
    name: str
    lon: float
    lat: float


if __name__ == "__main__":
    from pympler import asizeof

    # check size
    simple = SimplePosition("London", -0.1, 51.5)
    slot = SlotPosition("Madrid", -3.7, 40.4)
    print("-- Size --")
    print("simple:", asizeof.asizeof(simple))
    print("slot:", asizeof.asizeof(slot))
    print()

    # check performance
    from timeit import timeit

    print(timeit("slot.name", setup="slot=SlotPosition('Oslo', 10.8, 59.9)", globals=globals()))
    print(timeit("simple.name", setup="simple=SimplePosition('Oslo', 10.8, 59.9)", globals=globals()))
