import abc
from allocation.domain import model


class AbstractRepository(abc.ABC):
    def __init__(self) -> None:
        self.seen: set[model.Product] = set()

    @abc.abstractmethod
    def _add(self, product: model.Product):
        raise NotImplementedError

    @abc.abstractmethod
    def _get(self, reference) -> model.Product:
        raise NotImplementedError

    def add(self, product: model.Product):
        self._add(product)
        self.seen.add(product)

    def get(self, sku) -> model.Product:
        product = self._get(sku)
        if product:
            self.seen.add(product)
        return product


class SqlAlchemyRepository(AbstractRepository):
    def __init__(self, session):
        super().__init__()
        self.session = session

    def _add(self, product):
        self.session.add(product)

    def _get(self, sku) -> model.Product:
        return self.session.query(model.Product).filter_by(sku=sku).first()
