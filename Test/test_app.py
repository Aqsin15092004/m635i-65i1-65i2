# tests/test_app.py - Demo Tests

import pytest
from app import add, multiply, factorial


class TestAdd:
    def test_positive_numbers(self):
        assert add(2, 3) == 5

    def test_negative_numbers(self):
        assert add(-1, -2) == -3

    def test_zero(self):
        assert add(0, 5) == 5


class TestMultiply:
    def test_simple_multiply(self):
        assert multiply(3, 4) == 12

    def test_multiply_by_zero(self):
        assert multiply(0, 99) == 0

    def test_negative_multiply(self):
        assert multiply(-2, 5) == -10


class TestFactorial:
    def test_zero(self):
        assert factorial(0) == 1

    def test_one(self):
        assert factorial(1) == 1

    def test_five(self):
        assert factorial(5) == 120

    def test_negative_raises_error(self):
        with pytest.raises(ValueError):
            factorial(-1)
