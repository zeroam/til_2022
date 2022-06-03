from __future__ import annotations
from allocation.adapters import email, redis_eventpublisher
from allocation.domain import commands, events, model
from allocation.domain.model import OrderLine, Product
from allocation.service_layer import unit_of_work


class InvalidSku(Exception):
    pass


def is_valid_sku(sku, batches):
    return sku in {b.sku for b in batches}


def add_batch(
    cmd: commands.CreateBatch,
    uow: unit_of_work.AbstractUnitOfWork,
) -> None:
    with uow:
        product = uow.products.get(sku=cmd.sku)
        if product is None:
            product = model.Product(cmd.sku, batches=[])
            uow.products.add(product)
        product.batches.append(model.Batch(cmd.ref, cmd.sku, cmd.qty, cmd.eta))
        uow.commit()


def allocate(
    cmd: commands.Allocate,
    uow: unit_of_work.AbstractUnitOfWork,
) -> str:
    line = OrderLine(cmd.orderid, cmd.sku, cmd.qty)
    with uow:
        product: Product = uow.products.get(sku=line.sku)
        if product is None:
            raise InvalidSku(f"Invalid sku {line.sku}")
        batchref = product.allocate(line)
        uow.commit()
    return batchref


def change_batch_quantity(
    cmd: commands.ChangeBatchQuantity,
    uow: unit_of_work.AbstractUnitOfWork,
):
    with uow:
        product = uow.products.get_by_batchref(batchref=cmd.ref)
        product.change_batch_quantity(ref=cmd.ref, qty=cmd.qty)
        uow.commit()


def send_out_of_stock_notification(
    event: events.OutOfStock,
    uow: unit_of_work.AbstractUnitOfWork,
):
    email.send("stock@made.com", f"Out of stock for {event.sku}")


def publish_allocated_event(
    event: events.Allocated,
    uow: unit_of_work.AbstractUnitOfWork,
):
    redis_eventpublisher.publish("line_allocated", event)
