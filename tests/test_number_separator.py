import pytest
from src.number_separator import separate_evens_odds

def test_separate_evens_odds_mixed_numbers():
    """Test separation of mixed even and odd numbers."""
    numbers = [1, 2, 3, 4, 5, 6]
    evens, odds = separate_evens_odds(numbers)
    assert evens == [2, 4, 6]
    assert odds == [1, 3, 5]

def test_separate_evens_odds_empty_list():
    """Test behavior with an empty list."""
    numbers = []
    evens, odds = separate_evens_odds(numbers)
    assert evens == []
    assert odds == []

def test_separate_evens_odds_only_evens():
    """Test list with only even numbers."""
    numbers = [2, 4, 6, 8]
    evens, odds = separate_evens_odds(numbers)
    assert evens == [2, 4, 6, 8]
    assert odds == []

def test_separate_evens_odds_only_odds():
    """Test list with only odd numbers."""
    numbers = [1, 3, 5, 7]
    evens, odds = separate_evens_odds(numbers)
    assert evens == []
    assert odds == [1, 3, 5, 7]

def test_separate_evens_odds_zero_handling():
    """Test handling of zero (which is considered even)."""
    numbers = [0, -1, 1, -2, 2]
    evens, odds = separate_evens_odds(numbers)
    assert evens == [0, -2, 2]
    assert odds == [-1, 1]

def test_separate_evens_odds_negative_numbers():
    """Test handling of negative numbers."""
    numbers = [-1, -2, -3, -4, -5, -6]
    evens, odds = separate_evens_odds(numbers)
    assert evens == [-2, -4, -6]
    assert odds == [-1, -3, -5]