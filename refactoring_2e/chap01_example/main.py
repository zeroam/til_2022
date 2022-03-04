from dataclasses import dataclass
import os
import json


@dataclass
class Play:
    name: str
    type: str


@dataclass
class Performance:
    playID: str
    audience: int


@dataclass
class Invoice:
    customer: str
    performances: list[Performance]


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


def statement(invoice: Invoice, plays: dict[str, Play]):
    statement_data = {}
    statement_data["customer"] = invoice.customer
    statement_data["performances"] = invoice.performances
    return render_plain_text(statement_data, plays)


def render_plain_text(data: dict, plays: dict[str, Play]):
    def amount_for(performance: Performance):
        result = 0

        if play_for(performance).type == "tragedy":
            result = 40000
            if performance.audience > 30:
                result += 1000 * (performance.audience - 30)
        elif play_for(performance).type == "comedy":
            result = 30000
            if performance.audience > 20:
                result += 10000 + 500 * (performance.audience - 20)
            result += 300 * performance.audience
        else:
            raise Exception(f"알 수 없는 장르: {play_for(performance)['type']}")

        return result

    def play_for(performance: Performance):
        return plays[performance.playID]

    def volume_credits_for(performance: Performance):
        # 포인트 적립
        result = 0

        result += max(performance.audience - 30, 0)
        if play_for(performance).type == "comedy":
            result += performance.audience // 5

        return result

    def usd(number: int):
        f = "${:.2f}"
        return f.format(number / 100)

    def total_amount():
        result = 0

        for perf in data['performances']:
            result += amount_for(perf)

        return result

    def total_volume_credits():
        result = 0
        for perf in data['performances']:
            result += volume_credits_for(perf)

        return result

    result = f"청구 내역 (고객명: {data['customer']})\n"

    for perf in data['performances']:
        # 청구내역 출력
        result += (
            f"  {play_for(perf).name}: {usd(amount_for(perf))} ({perf.audience}석)\n"
        )

    result += f"총액: {usd(total_amount())}\n"
    result += f"적립 포인트: {total_volume_credits()}\n"

    return result


def main():
    invoices, plays = load_data()
    for i, invoice in enumerate(invoices):
        result = statement(invoice, plays)
        print(f"청구서 #{i + 1}:\n{result}\n")


if __name__ == "__main__":
    main()
