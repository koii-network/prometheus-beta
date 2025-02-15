import pytest
from src.number_check import is_even_or_odd

def test_even_numbers():
    """Test various even numbers"""
    assert is_even_or_odd(0) == 'even'
    assert is_even_or_odd(2) == 'even'
    assert is_even_or_odd(100) == 'even'
    assert is_even_or_odd(-4) == 'even'

def test_odd_numbers():
    """Test various odd numbers"""
    assert is_even_or_odd(1) == 'odd'
    assert is_even_or_odd(3) == 'odd'
    assert is_even_or_odd(99) == 'odd'
    assert is_even_or_odd(-7) == 'odd'

def test_invalid_input():
    """Test error handling for invalid inputs"""
    with pytest.raises(TypeError):
        is_even_or_odd(3.14)
    with pytest.raises(TypeError):
        is_even_or_odd("not a number")
    with pytest.raises(TypeError):
        is_even_or_odd(None)