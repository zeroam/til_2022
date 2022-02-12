from dataclasses import dataclass


@dataclass
class Position:
    name: str
    lon: float
    lat: float


@dataclass
class Capital(Position):
    country: str


if __name__ == "__main__":
    print(Capital("Oslo", 10.8, 59.9, "Norway"))
