import pytest
from src.addition import add_without_plus

def test_add_positive_numbers():
    assert add_without_plus(5, 3) == 8
    assert add_without_plus(10, 20) == 30
    assert add_without_plus(0, 7) == 7
    assert add_without_plus(7, 0) == 7

def test_add_negative_numbers():
    assert add_without_plus(-5, -3) == -8
    assert add_without_plus(-10, -20) == -30

def test_add_mixed_signs():
    assert add_without_plus(-5, 3) == -2
    assert add_without_plus(5, -3) == 2
    assert add_without_plus(0, -7) == -7
    assert add_without_plus(-7, 0) == -7

def test_large_numbers():
    assert add_without_plus(1000, 2000) == 3000
    assert add_without_plus(-1000, -2000) == -3000

def test_zero_addition():
    assert add_without_plus(0, 0) == 0