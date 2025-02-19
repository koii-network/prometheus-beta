import pytest
from src.sum_of_multiples import sum_of_multiples

def test_basic_multiple():
    """Test basic multiple calculation"""
    assert sum_of_multiples(10, [3, 5]) == 23  # 3 + 5 + 6 + 9 + 10

def test_single_multiple():
    """Test with a single multiple"""
    assert sum_of_multiples(20, [3]) == 63  # 3 + 6 + 9 + 12 + 15 + 18

def test_empty_multiples():
    """Test with empty multiples list"""
    assert sum_of_multiples(10, []) == 0

def test_large_limit():
    """Test with a larger limit"""
    assert sum_of_multiples(1000, [3, 5]) == 234168

def test_invalid_limit_zero():
    """Test that ValueError is raised for zero limit"""
    with pytest.raises(ValueError, match="Limit must be a positive integer"):
        sum_of_multiples(0, [3, 5])

def test_invalid_limit_negative():
    """Test that ValueError is raised for negative limit"""
    with pytest.raises(ValueError, match="Limit must be a positive integer"):
        sum_of_multiples(-10, [3, 5])

def test_invalid_multiple_zero():
    """Test that ValueError is raised for zero in multiples"""
    with pytest.raises(ValueError, match="All multiples must be positive integers"):
        sum_of_multiples(10, [3, 0, 5])

def test_invalid_multiple_negative():
    """Test that ValueError is raised for negative multiple"""
    with pytest.raises(ValueError, match="All multiples must be positive integers"):
        sum_of_multiples(10, [3, -5])

def test_duplicate_multiples():
    """Test that duplicate multiples are handled correctly"""
    assert sum_of_multiples(20, [3, 3, 5]) == 78