import string
import random
from abc import ABC, abstractmethod
from typing import Callable


def generate_id(length=8):
    # helper function for generating an id
    return "".join(random.choices(string.ascii_uppercase, k=length))


class SupportTicket:
    def __init__(self, customer, issue) -> None:
        self.id = generate_id()
        self.customer = customer
        self.issue = issue


def fifo_ordering(tickets: list[SupportTicket]) -> list[SupportTicket]:
    return tickets.copy()


def filo_ordering(tickets: list[SupportTicket]) -> list[SupportTicket]:
    copied_tickets = tickets.copy()
    copied_tickets.reverse()
    return copied_tickets


def random_ordering(tickets: list[SupportTicket]) -> list[SupportTicket]:
    copied_tickets = tickets.copy()
    random.shuffle(copied_tickets)
    return copied_tickets


class CustomSupport:
    def __init__(self, processing_strategy: Callable[[list[SupportTicket]], list[SupportTicket]]):
        self.tickets = []
        self.processing_strategy = processing_strategy

    def create_ticket(self, customer, issue):
        self.tickets.append(SupportTicket(customer, issue))

    def process_tickets(self):
        tickets = self.processing_strategy(self.tickets)

        # if it's empty, don't do anything
        if len(tickets) == 0:
            print("There are no tickets to process. Well done!")
            return

        for ticket in tickets:
            self.process_ticket(ticket)


    def process_ticket(self, ticket: SupportTicket):
        print("==================================")
        print(f"Processing ticket id: {ticket.id}")
        print(f"Customer: {ticket.customer}")
        print(f"Issue: {ticket.issue}")
        print("==================================")


if __name__ == "__main__":
    # create the application
    app = CustomSupport(random_ordering)

    # register a few tickets
    app.create_ticket("John Smith", "My computer makes strange sounds!")
    app.create_ticket("Linus Sebastian", "I can't upload any videos, please help.")
    app.create_ticket("Arjan Egges", "VSCode doesn't automatically solve my bugs.")

    # process the tickets
    app.process_tickets()
