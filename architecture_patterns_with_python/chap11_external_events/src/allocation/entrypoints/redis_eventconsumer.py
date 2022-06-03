import json
import logging
import redis

from allocation import config
from allocation.domain import commands
from allocation.adapters import orm
from allocation.service_layer import messagebus, unit_of_work


logger = logging.getLogger(__name__)

r = redis.Redis(**config.get_redis_host_and_port())


def main():
    print("start")
    orm.start_mappers()
    pubsub = r.pubsub(ignore_subscribe_messages=True)
    pubsub.subscribe("change_batch_quantity", "allocate")

    for m in pubsub.listen():
        if m["channel"].decode() == "allocate":
            handle_allocate(m)
        elif m["channel"].decode() == "change_batch_quantity":
            handle_change_batch_quantity(m)
        else:
            print("not match")


def handle_allocate(m):
    logging.debug(f"handling {m}")
    data = json.loads(m["data"])
    cmd = commands.Allocate(orderid=data["orderid"], sku=data["sku"], qty=data["qty"])
    messagebus.handle(cmd, uow=unit_of_work.SqlAlchemyUnitOfWork())


def handle_change_batch_quantity(m):
    logging.debug(f"handling {m}")
    data = json.loads(m["data"])
    cmd = commands.ChangeBatchQuantity(ref=data["batchref"], qty=data["qty"])
    messagebus.handle(cmd, uow=unit_of_work.SqlAlchemyUnitOfWork())


if __name__ == "__main__":
    main()
