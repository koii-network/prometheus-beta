import pytest
from src.sum_of_multiples import sum_of_multiples

def test_sum_of_multiples_basic():
    """Test basic functionality with simple inputs"""
    assert sum_of_multiples(3, 5) == 543  # Multiples of 3 and 5 up to 100

def test_sum_of_multiples_same_number():
    """Test when a and b are the same number"""
    assert sum_of_multiples(7, 7) == ara(7, 7) == 595  # Sum of multiples of 7 up to 100

def test_sum_of_multiples_one_overlap():
    """Test case with some overlapping multiples"""
    assert sum_of_multiples(2, 3) == 564  # Unique multiples of 2 and 3 up to 100

def test_sum_of_multiples_input_limits():
    """Test inputs at the boundaries of allowed range"""
    assert sum_of_multiples(1, 100) == 5050  # Sum of all numbers from 1 to 100

def test_sum_of_multiples_invalid_input_low():
    """Test handling of input below allowed range"""
    with pytest.raises(ValueError, match="Both a and b must be integers between 1 and 100"):
        sum_of_multiples(0, 5)

def test_sum_of_multiples_invalid_input_high():
    """Test handling of input above allowed range"""
    with pytest.raises(ValueError, match="Both a and b must be integers between 1 and 100"):
        sum_of_multiples(101, 5)

def test_sum_of_multiples_invalid_both_inputs():
    """Test handling of both inputs being invalid"""
    with pytest.raises(ValueError, match="Both a and b must be integers between 1 and 100"):
        sum_of_multiples(0, 101)