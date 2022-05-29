import logging
from typing import Callable

from allocation.domain import commands, events
from . import handlers, unit_of_work

logger = logging.getLogger(__name__)

Message = commands.Command | events.Event


def handle(message: Message, uow: unit_of_work.AbstractUnitOfWork):
    results = []
    queue = [message]
    while queue:
        message = queue.pop(0)
        if isinstance(message, events.Event):
            handle_event(message, queue, uow)
        elif isinstance(message, commands.Command):
            cmd_result = handle_command(message, queue, uow)
            results.append(cmd_result)
        else:
            raise Exception(f"{message} was not an Event or Command")
    return results


def handle_event(
    event: events.Event,
    queue: list[Message],
    uow: unit_of_work.AbstractUnitOfWork,
):
    for handler in EVENT_HANDLERS[type(event)]:
        try:
            logger.debug(f"handling event {event} with handler {handler}")
            handler(event, uow=uow)
            queue.extend(uow.collect_new_events())
        except Exception:
            logger.exception(f"Exception handling event {event}")
            continue


def handle_command(
    command: commands.Command,
    queue: list[Message],
    uow: unit_of_work.AbstractUnitOfWork,
):
    try:
        handler = COMMAND_HANDLERS[type(command)]
        result = handler(command, uow=uow)
        queue.extend(uow.collect_new_events())
        return result
    except Exception:
        logger.exception(f"Exception handling command {command}")
        raise


EVENT_HANDLERS: dict[type[events.Event], list[Callable]] = {
    events.OutOfStock: [handlers.send_out_of_stock_notification],
}

COMMAND_HANDLERS: dict[type[commands.Command], Callable] = {
    commands.Allocate: handlers.allocate,
    commands.CreateBatch: handlers.add_batch,
    commands.ChangeBatchQuantity: handlers.change_batch_quantity,
}
