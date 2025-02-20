import pytest
from src.number_separator import separate_evens_odds

def test_separate_evens_odds_mixed_numbers():
    """Test with a mix of even and odd numbers."""
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    evens, odds = separate_evens_odds(input_list)
    assert evens == [2, 4, 6, 8, 10]
    assert odds == [1, 3, 5, 7, 9]

def test_separate_evens_odds_all_even():
    """Test with all even numbers."""
    input_list = [2, 4, 6, 8, 10]
    evens, odds = separate_evens_odds(input_list)
    assert evens == [2, 4, 6, 8, 10]
    assert odds == []

def test_separate_evens_odds_all_odd():
    """Test with all odd numbers."""
    input_list = [1, 3, 5, 7, 9]
    evens, odds = separate_evens_odds(input_list)
    assert evens == []
    assert odds == [1, 3, 5, 7, 9]

def test_separate_evens_odds_empty_list():
    """Test with an empty list."""
    input_list = []
    evens, odds = separate_evens_odds(input_list)
    assert evens == []
    assert odds == []

def test_separate_evens_odds_zero():
    """Test with zero."""
    input_list = [0]
    evens, odds = separate_evens_odds(input_list)
    assert evens == [0]
    assert odds == []

def test_separate_evens_odds_negative_numbers():
    """Test with negative numbers."""
    input_list = [-1, -2, -3, -4, -5]
    evens, odds = separate_evens_odds(input_list)
    assert evens == [-2, -4]
    assert odds == [-1, -3, -5]