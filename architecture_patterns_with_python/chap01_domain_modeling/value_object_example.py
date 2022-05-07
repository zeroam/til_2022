from collections import namedtuple
from dataclasses import dataclass
from typing import NamedTuple


@dataclass
class Name:
    first_name: str
    surname: str


class Money(NamedTuple):
    currency: str
    value: int


Line = namedtuple("Line", ["sku", "qty"])


def test_equality():
    assert Money("gdp", 10) == Money("gdp", 10)
    assert Name("Harry", "Percival") != Name("Bob", "Gregory")
    assert Line("RED-CHAIR", 5) == Line("RED-CHAIR", 5)
