import pytest
from src.addition_without_plus import add_without_plus

def test_add_without_plus_positive_numbers():
    assert add_without_plus(3, 4) == 7
    assert add_without_plus(10, 20) == 30
    assert add_without_plus(0, 5) == 5
    assert add_without_plus(5, 0) == 5

def test_add_without_plus_negative_numbers():
    assert add_without_plus(-3, 4) == 1
    assert add_without_plus(3, -4) == -1
    assert add_without_plus(-10, -20) == -30

def test_add_without_plus_zero():
    assert add_without_plus(0, 0) == 0

def test_add_without_plus_large_numbers():
    assert add_without_plus(1000, 2000) == 3000
    assert add_without_plus(-1000, 1000) == 0