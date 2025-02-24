import pytest
from src.number_utils import is_even_or_odd

def test_is_even_or_odd_positive():
    assert is_even_or_odd(0) == 'even'
    assert is_even_or_odd(2) == 'even'
    assert is_even_or_odd(4) == 'even'
    assert is_even_or_odd(1) == 'odd'
    assert is_even_or_odd(3) == 'odd'
    assert is_even_or_odd(5) == 'odd'

def test_is_even_or_odd_negative():
    assert is_even_or_odd(-2) == 'even'
    assert is_even_or_odd(-4) == 'even'
    assert is_even_or_odd(-1) == 'odd'
    assert is_even_or_odd(-3) == 'odd'
    assert is_even_or_odd(-5) == 'odd'

def test_is_even_or_odd_invalid_input():
    with pytest.raises(TypeError):
        is_even_or_odd(3.14)
    with pytest.raises(TypeError):
        is_even_or_odd("2")
    with pytest.raises(TypeError):
        is_even_or_odd(None)