import pytest
from src.sum_of_multiples import sum_of_multiples

def test_basic_multiples():
    """Test sum of multiples for basic scenarios"""
    assert sum_of_multiples(3, 5) == 533  # Expected sum of multiples of 3 and 5 up to 100

def test_same_multiple():
    """Test when both inputs are the same"""
    assert sum_of_multiples(7, 7) == 595  # Sum of multiples of 7 up to 100

def test_large_multiples():
    """Test with larger valid multiples"""
    assert sum_of_multiples(13, 17) == 540  # Sum of multiples of 13 and 17 up to 100

def test_boundary_values():
    """Test boundary values of the input range"""
    assert sum_of_multiples(1, 100) == 5050  # Sum of all numbers from 1 to 100
    assert sum_of_multiples(100, 1) == 5050  # Order shouldn't matter

def test_invalid_input_type():
    """Test invalid input types"""
    with pytest.raises(ValueError, match="Both a and b must be integers"):
        sum_of_multiples(3.5, 5)
    with pytest.raises(ValueError, match="Both a and b must be integers"):
        sum_of_multiples("3", 5)

def test_out_of_range_inputs():
    """Test inputs outside the valid range"""
    with pytest.raises(ValueError, match="Both a and b must be between 1 and 100"):
        sum_of_multiples(0, 5)
    with pytest.raises(ValueError, match="Both a and b must be between 1 and 100"):
        sum_of_multiples(3, 101)
    with pytest.raises(ValueError, match="Both a and b must be between 1 and 100"):
        sum_of_multiples(-1, 5)