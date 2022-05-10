import abc
import model

from sqlalchemy.orm import selectinload


class AbstractRepository(abc.ABC):
    @abc.abstractclassmethod
    def add(self, batch: model.Batch):
        ...

    @abc.abstractclassmethod
    def get(self, reference) -> model.Batch:
        ...

    @abc.abstractclassmethod
    def get_from_line(self, orderid) -> model.Batch:
        ...

    @abc.abstractclassmethod
    def list(self) -> list[model.Batch]:
        ...


class SqlAlchemyRepository(AbstractRepository):
    def __init__(self, session):
        self.session = session

    def add(self, batch):
        self.session.add(batch)

    def get(self, reference) -> model.Batch:
        return self.session.query(model.Batch).filter_by(reference=reference).one()

    def get_from_line(self, orderid) -> model.Batch:
        return (
            self.session.query(model.Batch)
            .options(selectinload(model.Batch._allocations))
            .filter(model.OrderLine.orderid == orderid)
            .one()
        )

    def list(self):
        return self.session.query(model.Batch).all()
