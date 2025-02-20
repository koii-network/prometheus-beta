import pytest
from src.number_separator import separate_evens_odds

def test_separate_evens_odds_mixed_numbers():
    """Test with a list of mixed even and odd numbers."""
    input_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    evens, odds = separate_evens_odds(input_nums)
    assert evens == [2, 4, 6, 8, 10]
    assert odds == [1, 3, 5, 7, 9]

def test_separate_evens_odds_all_even():
    """Test with a list of only even numbers."""
    input_nums = [2, 4, 6, 8, 10]
    evens, odds = separate_evens_odds(input_nums)
    assert evens == [2, 4, 6, 8, 10]
    assert odds == []

def test_separate_evens_odds_all_odd():
    """Test with a list of only odd numbers."""
    input_nums = [1, 3, 5, 7, 9]
    evens, odds = separate_evens_odds(input_nums)
    assert evens == []
    assert odds == [1, 3, 5, 7, 9]

def test_separate_evens_odds_empty_list():
    """Test with an empty list."""
    input_nums = []
    evens, odds = separate_evens_odds(input_nums)
    assert evens == []
    assert odds == []

def test_separate_evens_odds_negative_numbers():
    """Test with negative numbers."""
    input_nums = [-1, -2, -3, -4, -5, 0]
    evens, odds = separate_evens_odds(input_nums)
    assert evens == [-2, -4, 0]
    assert odds == [-1, -3, -5]