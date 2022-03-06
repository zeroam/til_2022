import pytest
from main import load_data, statement, Invoice, Play, html_statement


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
    return Invoice.from_dict(data)


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


def test_html_statement(invoice, plays):
    result = html_statement(invoice, plays)

    assert result == (
        """
<h1>청구 내역 (고객명: BigCo)</h1>
<table>
<tr><th>연극</th><th>좌석 수</th><th>금액</th></tr>  <tr><td>Hamlet</td><td>(55석)</td><td>$650.00</td></td>
  <tr><td>As You Like It</td><td>(35석)</td><td>$580.00</td></td>
  <tr><td>Othello</td><td>(40석)</td><td>$500.00</td></td>
</table>
<p>총액: <em>$1730.00</em></p>
<p>적립 포인트: <em>47</em>점</p>
""".lstrip()
    )
