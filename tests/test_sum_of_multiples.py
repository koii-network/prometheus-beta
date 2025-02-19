import pytest
from src.sum_of_multiples import sum_of_multiples

def test_basic_multiples():
    """Test sum of multiples with simple input."""
    assert sum_of_multiples(10, [3, 5]) == 23  # 3 + 5 + 6 + 9 + 10

def test_single_multiple():
    """Test sum of multiples with a single number."""
    assert sum_of_multiples(10, [3]) == 18  # 3 + 6 + 9

def test_no_multiples():
    """Test with an empty list of multiples."""
    assert sum_of_multiples(10, []) == 0

def test_large_limit():
    """Test with a larger limit."""
    assert sum_of_multiples(1000, [3, 5]) == 234168

def test_invalid_negative_limit():
    """Test raising ValueError for negative limit."""
    with pytest.raises(ValueError, match="Limit must be a positive integer"):
        sum_of_multiples(-10, [3, 5])

def test_invalid_zero_limit():
    """Test raising ValueError for zero limit."""
    with pytest.raises(ValueError, match="Limit must be a positive integer"):
        sum_of_multiples(0, [3, 5])

def test_invalid_negative_multiple():
    """Test raising ValueError for negative multiple."""
    with pytest.raises(ValueError, match="All multiples must be positive integers"):
        sum_of_multiples(10, [3, -5])

def test_invalid_zero_multiple():
    """Test raising ValueError for zero multiple."""
    with pytest.raises(ValueError, match="All multiples must be positive integers"):
        sum_of_multiples(10, [3, 0])

def test_duplicate_multiples():
    """Test handling of duplicate multiples."""
    assert sum_of_multiples(20, [3, 3, 5]) == 78  # Should not double-count