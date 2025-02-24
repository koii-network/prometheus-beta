import pytest
from src.number_checker import is_even_or_odd

def test_even_numbers():
    """Test that positive and negative even numbers return 'even'"""
    assert is_even_or_odd(0) == 'even'
    assert is_even_or_odd(2) == 'even'
    assert is_even_or_odd(-4) == 'even'
    assert is_even_or_odd(100) == 'even'

def test_odd_numbers():
    """Test that positive and negative odd numbers return 'odd'"""
    assert is_even_or_odd(1) == 'odd'
    assert is_even_or_odd(-3) == 'odd'
    assert is_even_or_odd(99) == 'odd'

def test_invalid_input():
    """Test that non-integer inputs raise a TypeError"""
    with pytest.raises(TypeError):
        is_even_or_odd(3.14)
    
    with pytest.raises(TypeError):
        is_even_or_odd("not a number")
    
    with pytest.raises(TypeError):
        is_even_or_odd(None)