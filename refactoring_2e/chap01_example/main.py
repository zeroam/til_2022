import os
import json
from statement_data import (
    Invoice,
    Play,
    Performance,
    StatementData,
    create_statement_data,
)


def load_data() -> tuple[list[Invoice], dict[str, Play]]:
    base_dir = os.path.abspath(os.path.dirname(__file__))
    invoice_path = os.path.join(base_dir, "invoices.json")
    plays_path = os.path.join(base_dir, "plays.json")

    with open(invoice_path) as invoice_fp, open(plays_path) as plays_fp:
        raw_invoices = json.load(invoice_fp)
        raw_plays = json.load(plays_fp)

    invoices = [
        Invoice(
            customer=invoice["customer"],
            performances=[
                Performance(**performance) for performance in invoice["performances"]
            ],
        )
        for invoice in raw_invoices
    ]
    plays = {k: Play(**v) for k, v in raw_plays.items()}

    return invoices, plays


def statement(invoice: Invoice, plays: dict[str, Play]) -> str:
    return render_plain_text(create_statement_data(invoice, plays))


def html_statement(invoice: Invoice, plays: dict[str, Play]) -> str:
    return render_html(create_statement_data(invoice, plays))


def render_plain_text(data: StatementData) -> str:
    result = f"청구 내역 (고객명: {data.customer})\n"

    for perf in data.performances:
        # 청구내역 출력
        result += f"  {perf.play.name}: {usd(perf.amount)} ({perf.audience}석)\n"

    result += f"총액: {usd(data.total_amount)}\n"
    result += f"적립 포인트: {data.total_volume_credits}\n"

    return result


def render_html(data: StatementData) -> str:
    result = f"<h1>청구 내역 (고객명: {data.customer})</h1>\n"
    result += "<table>\n"
    result += "<tr><th>연극</th><th>좌석 수</th><th>금액</th></tr>"
    for perf in data.performances:
        result += f"  <tr><td>{perf.play.name}</td><td>({perf.audience}석)</td>"
        result += f"<td>{usd(perf.amount)}</td></td>\n"
    result += "</table>\n"
    result += f"<p>총액: <em>{usd(data.total_amount)}</em></p>\n"
    result += f"<p>적립 포인트: <em>{data.total_volume_credits}</em>점</p>\n"
    return result


def usd(number: int):
    f = "${:.2f}"
    return f.format(number / 100)


def main():
    invoices, plays = load_data()
    for i, invoice in enumerate(invoices):
        print(f"청구서 #{i + 1}:\n{statement(invoice, plays)}\n")
        print(f"청구서 HTML #{i + 1}:\n{html_statement(invoice, plays)}")


if __name__ == "__main__":
    main()
