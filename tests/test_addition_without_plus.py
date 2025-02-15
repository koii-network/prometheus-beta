import pytest
from src.addition_without_plus import add_without_plus

def test_basic_addition():
    assert add_without_plus(3, 4) == 7
    assert add_without_plus(0, 0) == 0
    assert add_without_plus(10, 20) == 30

def test_negative_numbers():
    assert add_without_plus(-5, 3) == -2
    assert add_without_plus(-10, -5) == -15

def test_large_numbers():
    assert add_without_plus(1000, 2000) == 3000
    assert add_without_plus(9999, 1) == 10000

def test_zero_addition():
    assert add_without_plus(0, 100) == 100
    assert add_without_plus(100, 0) == 100

def test_types():
    with pytest.raises(TypeError):
        add_without_plus("5", 3)
    with pytest.raises(TypeError):
        add_without_plus(5, "3")