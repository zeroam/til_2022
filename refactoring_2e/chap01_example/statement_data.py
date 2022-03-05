from dataclasses import dataclass
from typing import Optional


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


@dataclass
class EnrichedPerformance(Performance):
    play: Optional[Play] = None
    amount: Optional[int] = None
    volume_credits: Optional[int] = None


@dataclass
class StatementData:
    customer: str
    performances: list[EnrichedPerformance]
    total_amount: Optional[int] = None
    total_volume_credits: Optional[int] = None


def create_statement_data(invoice: Invoice, plays: dict[str, Play]) -> StatementData:
    def enrich_performance(performance: Performance) -> EnrichedPerformance:
        result = EnrichedPerformance(
            playID=performance.playID,
            audience=performance.audience,
        )
        result.play = play_for(result)
        result.amount = amount_for(result)
        result.volume_credits = volume_credits_for(result)
        return result

    def play_for(performance: Performance):
        return plays[performance.playID]

    def amount_for(performance: EnrichedPerformance):
        result = 0

        if performance.play.type == "tragedy":
            result = 40000
            if performance.audience > 30:
                result += 1000 * (performance.audience - 30)
        elif performance.play.type == "comedy":
            result = 30000
            if performance.audience > 20:
                result += 10000 + 500 * (performance.audience - 20)
            result += 300 * performance.audience
        else:
            raise Exception(f"알 수 없는 장르: {performance.play.type}")

        return result

    def volume_credits_for(performance: EnrichedPerformance):
        # 포인트 적립
        result = 0

        result += max(performance.audience - 30, 0)
        if performance.play.type == "comedy":
            result += performance.audience // 5

        return result

    def play_for(performance: Performance):
        return plays[performance.playID]

    def amount_for(performance: EnrichedPerformance):
        result = 0

        if performance.play.type == "tragedy":
            result = 40000
            if performance.audience > 30:
                result += 1000 * (performance.audience - 30)
        elif performance.play.type == "comedy":
            result = 30000
            if performance.audience > 20:
                result += 10000 + 500 * (performance.audience - 20)
            result += 300 * performance.audience
        else:
            raise Exception(f"알 수 없는 장르: {performance.play.type}")

        return result

    def volume_credits_for(performance: EnrichedPerformance):
        # 포인트 적립
        result = 0

        result += max(performance.audience - 30, 0)
        if performance.play.type == "comedy":
            result += performance.audience // 5

        return result

    def total_amount(data: StatementData):
        return sum(perf.amount for perf in data.performances)

    def total_volume_credits(data: StatementData):
        return sum(perf.volume_credits for perf in data.performances)

    statement_data = StatementData(
        customer=invoice.customer,
        performances=[
            enrich_performance(performance) for performance in invoice.performances
        ],
    )
    statement_data.total_amount = total_amount(statement_data)
    statement_data.total_volume_credits = total_volume_credits(statement_data)

    return statement_data
