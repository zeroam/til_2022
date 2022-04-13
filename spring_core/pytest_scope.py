import pytest


class Prototype:
    def __init__(self):
        self.count = 0

    def add_count(self):
        self.count += 1


class Service:
    def __init__(self, prototype: Prototype):
        self.prototype = prototype

    def logic(self):
        self.prototype.add_count()


@pytest.fixture(scope="function")
def prototype():
    return Prototype()


@pytest.fixture(scope="module")
def service(prototype: Prototype):
    return Service(prototype)


def test_add_count(service: Service):
    service.logic()

    assert service.prototype.count == 1


def test_add_count(service: Service):
    service.logic()

    assert service.prototype.count == 1
