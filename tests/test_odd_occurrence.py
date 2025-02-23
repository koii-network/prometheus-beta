import pytest
from src.odd_occurrence import find_odd_occurrence

def test_basic_odd_occurrence():
    """Test basic scenario with a single number occurring odd times"""
    assert find_odd_occurrence([1, 1, 2, 2, 3]) == 3

def test_multiple_odd_occurrence_numbers():
    """Test scenario with multiple numbers occurring odd times"""
    assert find_odd_occurrence([1, 1, 2, 2, 3, 3, 3]) == 3

def test_single_number():
    """Test scenario with a single number"""
    assert find_odd_occurrence([5]) == 5

def test_large_numbers():
    """Test with larger numbers"""
    assert find_odd_occurrence([10, 10, 20, 20, 30, 30, 40]) == 40

def test_repeated_numbers():
    """Test with highly repeated numbers"""
    assert find_odd_occurrence([5, 5, 5, 1, 1, 3, 3, 3]) == 5

def test_empty_list_raises_error():
    """Test that empty list raises ValueError"""
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        find_odd_occurrence([])

def test_no_odd_occurrence_numbers_raises_error():
    """Test that no odd occurrence numbers raises ValueError"""
    with pytest.raises(ValueError, match="No number appears an odd number of times"):
        find_odd_occurrence([1, 1, 2, 2, 3, 3])