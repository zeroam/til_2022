import abc
from dataclasses import dataclass, field


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


@dataclass(init=False)
class EnrichedPerformance(Performance):
    play: Play
    amount: int
    volume_credits: int

    def __init__(self, performance: Performance, play: Play):
        super().__init__(playID=performance.playID, audience=performance.audience)
        calculator = create_performance_calculator(performance, play)
        self.play = calculator.play
        self.amount = calculator.amount
        self.volume_credits = calculator.volume_credits


@dataclass(init=False)
class StatementData:
    customer: str
    plays: dict[str, Play] = field(repr=False)
    performances: list[EnrichedPerformance]
    total_amount: int
    total_volume_credits: int

    def __init__(self, invoice: Invoice, plays: dict[str, Play]):
        self.customer = invoice.customer
        self.plays = plays
        self.performances = [
            EnrichedPerformance(performance, self.play_for(performance))
            for performance in invoice.performances
        ]
        self.total_amount = self.total_amount()
        self.total_volume_credits = self.total_volume_credits()

    def play_for(self, performance: EnrichedPerformance) -> Play:
        return self.plays[performance.playID]

    def total_amount(self) -> int:
        return sum(perf.amount for perf in self.performances)

    def total_volume_credits(self) -> int:
        return sum(perf.volume_credits for perf in self.performances)


class PerformanceCalculator(abc.ABC):
    def __init__(self, performance: Performance, play: Play):
        self.performance = performance
        self.play = play

    @abc.abstractproperty
    def amount(self) -> int:
        pass

    @property
    def volume_credits(self):
        return max(self.performance.audience - 30, 0)


class TragedyCalculator(PerformanceCalculator):
    @property
    def amount(self) -> int:
        result = 40000
        if self.performance.audience > 30:
            result += 1000 * (self.performance.audience - 30)
        return result


class ComedyCalculator(PerformanceCalculator):
    @property
    def amount(self) -> int:
        result = 30000
        if self.performance.audience > 20:
            result += 10000 + 500 * (self.performance.audience - 20)
        result += 300 * self.performance.audience
        return result

    @property
    def volume_credits(self):
        return super().volume_credits + self.performance.audience // 5


def create_performance_calculator(
    performance: Performance, play: Play
) -> PerformanceCalculator:
    if play.type == "tragedy":
        return TragedyCalculator(performance, play)
    elif play.type == "comedy":
        return ComedyCalculator(performance, play)
    else:
        raise Exception(f"알 수 없는 장르: {play.type}")
