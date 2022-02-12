import py
import pytest
from vector2d import Vector2d


@pytest.fixture
def v1():
    return Vector2d(3, 4)


def test_unpacking(v1):
    x, y = v1
    assert x == 3
    assert y == 4


def test_repr_and_eq(v1):
    v1_clone = eval(repr(v1))
    assert v1 == v1_clone


def test_str(v1):
    assert str(v1) == "(3.0, 4.0)"


def test_bytes(v1):
    octets = bytes(v1)
    print(octets)
    assert octets == b"d\x00\x00\x00\x00\x00\x00\x08@\x00\x00\x00\x00\x00\x00\x10@"


def test_from_bytes(v1):
    octets = b"d\x00\x00\x00\x00\x00\x00\x08@\x00\x00\x00\x00\x00\x00\x10@"
    assert Vector2d.frombytes(octets) == v1


def test_abs(v1):
    assert abs(v1) == 5


def test_bool(v1):
    assert bool(v1) == True
    assert bool(Vector2d(0, 0)) == False


def test_format(v1):
    assert format(v1) == "(3.0, 4.0)"
    assert format(v1, ".2f") == "(3.00, 4.00)"
    assert format(v1, ".3e") == "(3.000e+00, 4.000e+00)"


def test_format_p():
    v = Vector2d(1, 1)

    assert format(v, "p") == "<1.4142135623730951, 0.7853981633974483>"
    assert format(v, ".3ep") == "<1.414e+00, 7.854e-01>"
    assert format(v, "0.5fp") == "<1.41421, 0.78540>"


def test_hash(v1):
    assert hash(v1) == 1079245023883434373

    s = set([v1])
    assert (v1 in s) == True
