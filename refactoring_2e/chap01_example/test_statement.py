import pytest
from main import statement


@pytest.fixture
def plays():
    return {
        "hamlet": {"name": "Hamlet", "type": "tragedy"},
        "as-like": {"name": "As You Like It", "type": "comedy"},
        "othello": {"name": "Othello", "type": "tragedy"},
    }


@pytest.fixture
def invoice():
    return {
        "customer": "BigCo",
        "performances": [
            {"playID": "hamlet", "audience": 55},
            {"playID": "as-like", "audience": 35},
            {"playID": "othello", "audience": 40},
        ],
    }


def test_statement(invoice, plays):
    result = statement(invoice, plays)

    assert result == (
"""청구 내역 (고객명: BigCo)
  Hamlet: $650.00 (55석)
  As You Like It: $580.00 (35석)
  Othello: $500.00 (40석)
총액: $1730.00
적립 포인트: 47
"""
    )
