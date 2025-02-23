import pytest
from src.number_separator import separate_evens_odds

def test_separate_evens_odds_mixed_numbers():
    """Test separating a mixed list of numbers."""
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    evens, odds = separate_evens_odds(numbers)
    assert evens == [2, 4, 6, 8, 10]
    assert odds == [1, 3, 5, 7, 9]

def test_separate_evens_odds_empty_list():
    """Test an empty input list."""
    numbers = []
    evens, odds = separate_evens_odds(numbers)
    assert evens == []
    assert odds == []

def test_separate_evens_odds_only_evens():
    """Test a list with only even numbers."""
    numbers = [2, 4, 6, 8, 10]
    evens, odds = separate_evens_odds(numbers)
    assert evens == [2, 4, 6, 8, 10]
    assert odds == []

def test_separate_evens_odds_only_odds():
    """Test a list with only odd numbers."""
    numbers = [1, 3, 5, 7, 9]
    evens, odds = separate_evens_odds(numbers)
    assert evens == []
    assert odds == [1, 3, 5, 7, 9]

def test_separate_evens_odds_negative_numbers():
    """Test a list with negative even and odd numbers."""
    numbers = [-1, -2, -3, -4, 0, 1, 2, 3, 4]
    evens, odds = separate_evens_odds(numbers)
    assert evens == [-2, -4, 0, 2, 4]
    assert odds == [-1, -3, 1, 3]