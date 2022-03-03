import pytest
from main import load_data, statement, Invoice, Performance, Play


@pytest.fixture
def plays():
    data = {
        "hamlet": {"name": "Hamlet", "type": "tragedy"},
        "as-like": {"name": "As You Like It", "type": "comedy"},
        "othello": {"name": "Othello", "type": "tragedy"},
    }
    return {k: Play(**v) for k, v in data.items()}


@pytest.fixture
def invoice():
    data = {
        "customer": "BigCo",
        "performances": [
            {"playID": "hamlet", "audience": 55},
            {"playID": "as-like", "audience": 35},
            {"playID": "othello", "audience": 40},
        ],
    }
    return Invoice(
        customer=data["customer"],
        performances=[
            Performance(**performance) for performance in data["performances"]
        ],
    )


def test_load_data(invoice, plays):
    i, p = load_data()

    assert i == [invoice]
    assert p == plays


def test_statement(invoice, plays):
    result = statement(invoice, plays)

    assert result == (
        """
청구 내역 (고객명: BigCo)
  Hamlet: $650.00 (55석)
  As You Like It: $580.00 (35석)
  Othello: $500.00 (40석)
총액: $1730.00
적립 포인트: 47
""".lstrip()
    )
