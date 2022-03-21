import math
import pytest

from main import Province


@pytest.fixture
def asia() -> Province:
    return Province(
        {
            "name": "Asia",
            "producers": [
                {"name": "Byzantium", "cost": 10, "production": 9},
                {"name": "Attalia", "cost": 12, "production": 10},
                {"name": "Sinope", "cost": 10, "production": 6},
            ],
            "demand": 30,
            "price": 20,
        }
    )


@pytest.fixture
def no_producers() -> Province:
    return Province(
        {
            "name": "No Producers",
            "producers": [],
            "demand": 30,
            "price": 20,
        }
    )


def test_shortfall(asia: Province):
    assert asia.shortfall == 5


def test_profit(asia: Province):
    assert asia.profit == 230


def test_change_production(asia: Province):
    asia.producers[0].production = 20
    assert asia.shortfall == -6
    assert asia.profit == 292


def test_no_producers_shortfall(no_producers: Province):
    assert no_producers.shortfall == 30


def test_no_producers_profit(no_producers: Province):
    assert no_producers.profit == 0


def test_zero_demand(asia: Province):
    asia.demand = 0
    assert asia.shortfall == -25
    assert asia.profit == 0


def test_negative_demand(asia: Province):
    asia.demand = -1
    assert asia.shortfall == -26
    assert asia.profit == -10


def test_empty_string_demand(asia: Province):
    with pytest.raises(ValueError):
        asia.demand = ""
        assert asia.shortfall == math.nan
        assert asia.profit == math.nan


def test_string_for_producers():
    prov = Province(
        {"name": "String producers", "producers": "", "demand": 30, "price": 20}
    )
    assert prov.shortfall == 30
