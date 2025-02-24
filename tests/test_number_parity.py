import pytest
from src.number_parity import is_even_or_odd

def test_even_numbers():
    """Test that positive and negative even numbers are correctly identified."""
    assert is_even_or_odd(0) == 'even'
    assert is_even_or_odd(2) == 'even'
    assert is_even_or_odd(4) == 'even'
    assert is_even_or_odd(-2) == 'even'
    assert is_even_or_odd(-4) == 'even'

def test_odd_numbers():
    """Test that positive and negative odd numbers are correctly identified."""
    assert is_even_or_odd(1) == 'odd'
    assert is_even_or_odd(3) == 'odd'
    assert is_even_or_odd(-1) == 'odd'
    assert is_even_or_odd(-3) == 'odd'

def test_invalid_input():
    """Test that invalid input types raise a TypeError."""
    with pytest.raises(TypeError):
        is_even_or_odd(3.14)
    
    with pytest.raises(TypeError):
        is_even_or_odd("not a number")
    
    with pytest.raises(TypeError):
        is_even_or_odd(None)

def test_large_numbers():
    """Test parity for large positive and negative numbers."""
    assert is_even_or_odd(1000000) == 'even'
    assert is_even_or_odd(-1000001) == 'odd'