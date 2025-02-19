import pytest
from src.sum_odd_numbers import sum_odd_numbers

def test_sum_odd_numbers_basic():
    """Test basic functionality with small numbers."""
    assert sum_odd_numbers(5) == 9  # 1 + 3 + 5
    assert sum_odd_numbers(10) == 25  # 1 + 3 + 5 + 7 + 9

def test_sum_odd_numbers_edge_cases():
    """Test edge cases."""
    assert sum_odd_numbers(0) == 0
    assert sum_odd_numbers(1) == 1
    assert sum_odd_numbers(2) == 1

def test_sum_odd_numbers_large_input():
    """Test with a larger input to verify performance."""
    result = sum_odd_numbers(100)
    assert result == 2500

def test_sum_odd_numbers_error_handling():
    """Test error handling for invalid inputs."""
    with pytest.raises(TypeError):
        sum_odd_numbers("10")
    
    with pytest.raises(TypeError):
        sum_odd_numbers(3.14)
    
    with pytest.raises(ValueError):
        sum_odd_numbers(-5)