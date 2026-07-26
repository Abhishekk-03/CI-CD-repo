import pytest
from Calculator import add, subtract, multiply, divide


def test_add():
    assert add(5, 5) == 10


def test_subtract():
    assert subtract(10, 5) == 5


def test_multiply():
    assert multiply(5, 5) == 25


def test_divide():
    assert divide(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)