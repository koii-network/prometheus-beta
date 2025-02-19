import pytest
from src.sum_of_multiples import sum_of_multiples

def test_sum_of_multiples_basic():
    """Test basic functionality with simple inputs."""
    assert sum_of_multiples(10, [3, 5]) == 23  # 3 + 5 + 6 + 9 + 10

def test_sum_of_multiples_single_value():
    """Test with a single multiple value."""
    assert sum_of_multiples(20, [3]) == 63  # 3 + 6 + 9 + 12 + 15 + 18

def test_sum_of_multiples_overlapping_multiples():
    """Test that overlapping multiples are counted only once."""
    assert sum_of_multiples(20, [3, 5]) == 78  # Unique multiples

def test_sum_of_multiples_empty_multiples():
    """Test when multiples list is empty."""
    assert sum_of_multiples(10, []) == 0

def test_sum_of_multiples_invalid_limit():
    """Test that ValueError is raised for non-positive limit."""
    with pytest.raises(ValueError, match="Limit must be a positive integer"):
        sum_of_multiples(0, [3, 5])
    with pytest.raises(ValueError, match="Limit must be a positive integer"):
        sum_of_multiples(-5, [3, 5])

def test_sum_of_multiples_invalid_multiples():
    """Test that ValueError is raised for non-positive multiples."""
    with pytest.raises(ValueError, match="All multiples must be positive integers"):
        sum_of_multiples(10, [0, 3])
    with pytest.raises(ValueError, match="All multiples must be positive integers"):
        sum_of_multiples(10, [3, -5])

def test_sum_of_multiples_large_numbers():
    """Test function with larger numbers."""
    assert sum_of_multiples(1000, [3, 5]) == 234168