"""일반적인 전략 패턴 구현"""
from dataclasses import dataclass
from typing import Callable, Iterable, Optional


@dataclass
class Customer:
    name: str
    fidelity: int


@dataclass
class LineItem:
    product: str
    quantity: int
    price: float

    def total(self) -> int:
        return self.price * self.quantity


class Order:  # 콘텍스트
    def __init__(
        self,
        customer: Customer,
        cart: Iterable[LineItem],
        promotion: Optional[Callable] = None,
    ) -> None:
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    def total(self):
        if not hasattr(self, "__total"):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion(self)
        return self.total() - discount

    def __repr__(self) -> str:
        return f"<Order total: {self.total():.2f} due: {self.due():.2f}>"


def fidelity_promo(order: Order):
    """충성도 포인트가 1000점 이상인 고객에게 전체 5% 할인 적용"""
    return order.total() * 0.05 if order.customer.fidelity >= 1000 else 0


def bulk_item_promo(order: Order):
    """20개 이상의 동일 상품을 구입하면 10% 할인 적용"""
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * 0.1
    return discount


def large_order_promo(order: Order):
    """10종류 이상의 상품을 구입하면 전체 7% 할인 적용"""
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * 0.07
    return 0


promos = [
    globals()[name]
    for name in globals()
    if name.endswith("_promo") and name != "best_promo"
]


def best_promo(order):
    """최대로 할인받을 금액을 반환한다"""
    return max(promo(order) for promo in promos)


if __name__ == "__main__":
    joe = Customer("John Doe", 0)
    ann = Customer("Ann Smith", 1100)

    cart = [
        LineItem("banana", 4, 0.5),
        LineItem("apple", 10, 1.5),
        LineItem("watermellon", 5, 5.0),
    ]
    print("-- FidelityPromo --")
    print(Order(joe, cart, fidelity_promo))
    print(Order(ann, cart, fidelity_promo))
    print()

    banana_cart = [LineItem("banana", 30, 0.5), LineItem("apple", 10, 1.5)]
    print("-- BulkPromo --")
    print(Order(joe, banana_cart, bulk_item_promo))
    print()

    long_order = [LineItem(str(item_code), 1, 1.0) for item_code in range(10)]
    print("-- LongOrderPromo --")
    print(Order(joe, long_order, large_order_promo))
    print(Order(joe, cart, large_order_promo))
    print()

    print("-- BestPromo --")
    print(Order(joe, long_order, best_promo))
    print(Order(joe, banana_cart, best_promo))
    print(Order(ann, cart, best_promo))
