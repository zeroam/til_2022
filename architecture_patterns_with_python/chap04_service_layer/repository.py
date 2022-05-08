import abc
import model


class AbstractRepository(abc.ABC):
    @abc.abstractclassmethod
    def add(self, batch: model.Batch):
        ...

    @abc.abstractclassmethod
    def get(self, reference) -> model.Batch:
        ...


class SqlAlchemyRepository(AbstractRepository):
    def __init__(self, session):
        self.session = session

    def add(self, batch):
        self.session.add(batch)

    def get(self, reference) -> model.Batch:
        return self.session.query(model.Batch).filter_by(reference=reference).one()

    def list(self):
        return self.session.query(model.Batch).all()
