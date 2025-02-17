import pytest
from src.addition import add_without_plus

def test_add_basic_positive_numbers():
    assert add_without_plus(3, 4) == 7
    assert add_without_plus(10, 20) == 30

def test_add_zero():
    assert add_without_plus(0, 5) == 5
    assert add_without_plus(5, 0) == 5
    assert add_without_plus(0, 0) == 0

def test_add_negative_numbers():
    assert add_without_plus(-3, 4) == 1
    assert add_without_plus(3, -4) == -1
    assert add_without_plus(-5, -3) == -8

def test_large_numbers():
    assert add_without_plus(1000, 2000) == 3000
    assert add_without_plus(99999, 1) == 100000

def test_type_error():
    with pytest.raises(TypeError):
        add_without_plus("3", 4)
    with pytest.raises(TypeError):
        add_without_plus(3, "4")