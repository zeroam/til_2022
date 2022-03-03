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
    def amount_for(perf, play):
        result = 0

        if play.type == "tragedy":
            result = 40000
            if perf.audience > 30:
                result += 1000 * (perf.audience - 30)
        elif play.type == "comedy":
            result = 30000
            if perf.audience > 20:
                result += 10000 + 500 * (perf.audience - 20)
            result += 300 * perf.audience
        else:
            raise Exception(f"알 수 없는 장르: {play['type']}")

        return result


    total_amount = 0
    volume_credits = 0
    result = f"청구 내역 (고객명: {invoice.customer})\n"
    format = "${:.2f}"

    for perf in invoice.performances:
        play = plays[perf.playID]
        this_amount = amount_for(perf, play)

        # 포인트 적립
        volume_credits += max(perf.audience - 30, 0)
        if play.type == "comedy":
            volume_credits += perf.audience // 5

        # 청구내역 출력
        result += (
            f"  {play.name}: {format.format(this_amount / 100)} ({perf.audience}석)\n"
        )
        total_amount += this_amount

    result += f"총액: {format.format(total_amount / 100)}\n"
    result += f"적립 포인트: {volume_credits}\n"

    return result


def main():
    invoices, plays = load_data()
    for i, invoice in enumerate(invoices):
        result = statement(invoice, plays)
        print(f"청구서 #{i + 1}:\n{result}\n")


if __name__ == "__main__":
    main()
