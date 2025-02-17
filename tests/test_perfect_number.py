import pytest
from src.perfect_number import is_perfect_number

def test_perfect_numbers():
    """Test known perfect numbers"""
    perfect_numbers = [6, 28, 496, 8128]
    for num in perfect_numbers:
        assert is_perfect_number(num) is True

def test_non_perfect_numbers():
    """Test non-perfect numbers"""
    non_perfect_numbers = [1, 10, 15, 100]
    for num in non_perfect_numbers:
        assert is_perfect_number(num) is False

def test_first_perfect_number():
    """Verify the first perfect number"""
    assert is_perfect_number(6) is True

def test_error_handling():
    """Test error handling for invalid inputs"""
    with pytest.raises(ValueError):
        is_perfect_number(0)
    
    with pytest.raises(ValueError):
        is_perfect_number(-5)
    
    with pytest.raises(ValueError):
        is_perfect_number(3.14)
    
    with pytest.raises(ValueError):
        is_perfect_number("not a number")