import pytest
from src.addition import add_without_plus

def test_add_without_plus_positive_numbers():
    assert add_without_plus(5, 3) == 8
    assert add_without_plus(10, 20) == 30
    assert add_without_plus(100, 200) == 300

def test_add_without_plus_zero():
    assert add_without_plus(0, 0) == 0
    assert add_without_plus(5, 0) == 5
    assert add_without_plus(0, 7) == 7

def test_add_without_plus_negative_numbers():
    assert add_without_plus(-5, 3) == -2
    assert add_without_plus(5, -3) == 2
    assert add_without_plus(-10, -20) == -30

def test_add_without_plus_large_numbers():
    assert add_without_plus(1000, 2000) == 3000
    assert add_without_plus(99999, 1) == 100000