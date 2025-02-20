import pytest
from src.odd_frequency_finder import find_odd_frequency_number

def test_basic_odd_frequency():
    # Basic case with one number appearing odd times
    assert find_odd_frequency_number([1, 1, 2, 2, 3]) == 3

def test_multiple_odd_frequency_numbers():
    # Case with multiple numbers appearing odd times, should return smallest
    assert find_odd_frequency_number([1, 1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5]) == 3

def test_single_number():
    # Case with a single number
    assert find_odd_frequency_number([5]) == 5

def test_repeated_number():
    # Case with a number repeated odd times
    assert find_odd_frequency_number([7, 7, 7]) == 7

def test_empty_list_raises_error():
    # Empty list should raise ValueError
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        find_odd_frequency_number([])

def test_no_odd_frequency_numbers_raises_error():
    # List with no numbers appearing odd times should raise ValueError
    with pytest.raises(ValueError, match="No number appears an odd number of times"):
        find_odd_frequency_number([1, 1, 2, 2, 3, 3])

def test_large_list():
    # Larger list with an odd frequency number
    test_list = [1, 1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 5, 6, 6]
    assert find_odd_frequency_number(test_list) == 5