import pytest
from src.number_check import is_even_or_odd

def test_positive_even_numbers():
    assert is_even_or_odd(0) == 'even'
    assert is_even_or_odd(2) == 'even'
    assert is_even_or_odd(100) == 'even'

def test_positive_odd_numbers():
    assert is_even_or_odd(1) == 'odd'
    assert is_even_or_odd(3) == 'odd'
    assert is_even_or_odd(99) == 'odd'

def test_negative_numbers():
    assert is_even_or_odd(-2) == 'even'
    assert is_even_or_odd(-1) == 'odd'
    assert is_even_or_odd(-100) == 'even'

def test_invalid_input():
    with pytest.raises(TypeError):
        is_even_or_odd(3.14)
    with pytest.raises(TypeError):
        is_even_or_odd("not a number")
    with pytest.raises(TypeError):
        is_even_or_odd(None)