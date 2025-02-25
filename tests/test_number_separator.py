import pytest
from src.number_separator import separate_evens_odds

def test_mixed_numbers():
    """Test separation of mixed even and odd numbers."""
    result = separate_evens_odds([1, 2, 3, 4, 5, 6])
    assert result == ([2, 4, 6], [1, 3, 5])

def test_empty_list():
    """Test behavior with an empty list."""
    result = separate_evens_odds([])
    assert result == ([], [])

def test_only_even_numbers():
    """Test list with only even numbers."""
    result = separate_evens_odds([2, 4, 6, 8])
    assert result == ([2, 4, 6, 8], [])

def test_only_odd_numbers():
    """Test list with only odd numbers."""
    result = separate_evens_odds([1, 3, 5, 7])
    assert result == ([], [1, 3, 5, 7])

def test_negative_numbers():
    """Test separation with negative numbers."""
    result = separate_evens_odds([-1, -2, -3, -4, 0])
    assert result == ([-2, -4, 0], [-1, -3])

def test_large_list():
    """Test separation of a larger list of numbers."""
    numbers = list(range(1, 21))  # 1 to 20
    evens = list(range(2, 21, 2))
    odds = list(range(1, 21, 2))
    result = separate_evens_odds(numbers)
    assert result == (evens, odds)