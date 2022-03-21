import math


class Province:
    """지역"""

    def __init__(self, doc: dict):
        self._name = doc["name"]
        self._producers = []
        self._total_production = 0
        self._demand = doc["demand"]
        self._price = doc["price"]
        [self.add_producer(Producer(self, d)) for d in doc["producers"]]

    @property
    def name(self):
        return self._name

    @property
    def producers(self) -> list["Producer"]:
        return self._producers

    @property
    def total_production(self):
        return self._total_production

    @total_production.setter
    def total_production(self, arg: int):
        self._total_production = arg

    def add_producer(self, arg: "Producer"):
        self._producers.append(arg)
        self._total_production += arg.production

    @property
    def demand(self):
        return self._demand

    @demand.setter
    def demand(self, arg: str):
        self._demand = int(arg)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, arg):
        self._price = int(arg)

    @property
    def shortfall(self):
        """생산 부족분 계산"""
        return self.demand - self.total_production

    @property
    def satisfield_demand(self):
        return min(self.demand, self.total_production)

    @property
    def demand_value(self):
        return self.satisfield_demand * self.price

    @property
    def demand_cost(self):
        remaining_demand = self.demand
        result = 0
        for p in sorted(self.producers, key=lambda x: x.cost):
            contribution = min(remaining_demand, p.production)
            remaining_demand -= contribution
            result += contribution * p.cost

        return result

    @property
    def profit(self):
        """수익 계산"""
        return self.demand_value - self.demand_cost


class Producer:
    """생산자"""

    def __init__(self, province: Province, data):
        self._province = province
        self._cost = data["cost"]
        self._name = data["name"]
        self._production = data["production"] if data["production"] else 0

    @property
    def name(self):
        return self._name

    @property
    def cost(self):
        return self._cost

    @cost.setter
    def cost(self, arg):
        self._cost = int(arg)

    @property
    def production(self):
        return self._production

    @production.setter
    def production(self, amount: str):
        new_production = int(amount)
        self._province.total_production += new_production - self._production
        self._production = new_production
