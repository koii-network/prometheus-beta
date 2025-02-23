import pytest
from src.triangular_numbers import count_triangular_numbers

def test_count_triangular_numbers():
    # Test basic cases
    assert count_triangular_numbers(0) == 0
    assert count_triangular_numbers(1) == 1
    assert count_triangular_numbers(3) == 2
    assert count_triangular_numbers(6) == 3
    assert count_triangular_numbers(10) == 4
    
    # Test larger numbers
    assert count_triangular_numbers(15) == 5
    assert count_triangular_numbers(21) == 6
    
    # Test edge cases
    assert count_triangular_numbers(100) == 14
    assert count_triangular_numbers(1000) == 44

def test_count_triangular_numbers_boundary():
    # Boundary testing
    assert count_triangular_numbers(0) == 0
    assert count_triangular_numbers(1) == 1

def test_count_triangular_numbers_negative():
    # Test negative input raises ValueError
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        count_triangular_numbers(-1)