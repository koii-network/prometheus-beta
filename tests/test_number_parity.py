import pytest
from src.number_parity import is_even_or_odd

def test_even_numbers():
    assert is_even_or_odd(0) == 'even'
    assert is_even_or_odd(2) == 'even'
    assert is_even_or_odd(4) == 'even'
    assert is_even_or_odd(-2) == 'even'
    assert is_even_or_odd(-4) == 'even'

def test_odd_numbers():
    assert is_even_or_odd(1) == 'odd'
    assert is_even_or_odd(3) == 'odd'
    assert is_even_or_odd(5) == 'odd'
    assert is_even_or_odd(-1) == 'odd'
    assert is_even_or_odd(-3) == 'odd'

def test_invalid_input():
    with pytest.raises(TypeError):
        is_even_or_odd(3.14)
    
    with pytest.raises(TypeError):
        is_even_or_odd("2")
    
    with pytest.raises(TypeError):
        is_even_or_odd(None)