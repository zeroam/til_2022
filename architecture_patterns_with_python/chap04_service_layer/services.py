import model
from model import OrderLine
from repository import AbstractRepository


class InvalidSku(Exception):
    pass


class NotFound(Exception):
    pass


def is_valid_sku(sku, batches):
    return sku in {b.sku for b in batches}


def allocate(line: OrderLine, repo: AbstractRepository, session) -> str:
    batches = repo.list()
    if not is_valid_sku(line.sku, batches):
        raise InvalidSku(f"Invalid sku {line.sku}")
    batchref = model.allocate(line, batches)
    session.commit()
    return batchref


def deallocate(orderid: str, sku: str, repo: AbstractRepository, session) -> None:
    # get batchref from order_line
    batch = repo.get_from_line(orderid)
    if not batch:
        raise NotFound(f"not found order: {orderid}")

    line = next(filter(lambda x: x.orderid == orderid, batch._allocations))
    if line.sku != sku:
        raise InvalidSku(f"Invalid sku {sku}")

    # remove line
    batch.deallocate(line)

    session.commit()
