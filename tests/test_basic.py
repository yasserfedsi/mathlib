from mathlib import calculate
import pytest

calc = calculate.Calculator()


def test_invalid_input():
    with pytest.raises(TypeError):
        calc.add("abc", 1)


def test_add():
    assert calc.add(2, 3) == 5


def test_subtract():
    assert calc.subtract(5, 3) == 2


def test_multiply():
    assert calc.multiply(4, 3) == 12


def test_divide():
    assert calc.divide(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ValueError, match="Division by zero is not allowed"):
        calc.divide(10, 0)


def test_dividend_zero():
    assert calc.divide(0, 10) == 0
