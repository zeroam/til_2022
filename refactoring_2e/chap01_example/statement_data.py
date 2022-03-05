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


class PerformanceCalculator:
    def __init__(self, performance: Performance, play: Play):
        self.performance = performance
        self.play = play

    @property
    def amount(self) -> int:
        result = 0

        if self.play.type == "tragedy":
            raise Exception(f"오류 발생: {self.play.type}")
        elif self.play.type == "comedy":
            result = 30000
            if self.performance.audience > 20:
                result += 10000 + 500 * (self.performance.audience - 20)
            result += 300 * self.performance.audience
        else:
            raise Exception(f"알 수 없는 장르: {self.play.type}")

        return result

    @property
    def volume_credits(self):
        result = max(self.performance.audience - 30, 0)
        if self.play.type == "comedy":
            result += self.performance.audience // 5

        return result


class TragedyCalculator(PerformanceCalculator):
    @property
    def amount(self) -> int:
        result = 40000
        if self.performance.audience > 30:
            result += 1000 * (self.performance.audience - 30)
        return result


class ComedyCalculator(PerformanceCalculator):
    pass


def create_performance_calculator(performance: Performance, play: Play):
    if play.type == "tragedy":
        return TragedyCalculator(performance, play)
    elif play.type == "comedy":
        return ComedyCalculator(performance, play)
    else:
        raise Exception(f"알 수 없는 장르: {play.type}")


def create_statement_data(invoice: Invoice, plays: dict[str, Play]) -> StatementData:
    def enrich_performance(performance: Performance) -> EnrichedPerformance:
        calculator = create_performance_calculator(performance, play_for(performance))
        result = EnrichedPerformance(
            playID=performance.playID,
            audience=performance.audience,
        )
        result.play = calculator.play
        result.amount = calculator.amount
        result.volume_credits = calculator.volume_credits
        return result

    def play_for(performance: Performance) -> Play:
        return plays[performance.playID]

    def total_amount(data: StatementData) -> int:
        return sum(perf.amount for perf in data.performances)

    def total_volume_credits(data: StatementData) -> int:
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
