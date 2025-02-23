import pytest
from src.filter_multiples import filter_multiples_3_or_5

def test_filter_multiples_basic():
    # Test with a simple list of numbers
    assert filter_multiples_3_or_5([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15]) == [3, 5, 6, 7, 9, 10]

def test_filter_multiples_empty_list():
    # Test with an empty list
    assert filter_multiples_3_or_5([]) == []

def test_filter_multiples_no_matches():
    # Test with a list where no numbers are exclusive multiples
    assert filter_multiples_3_or_5([1, 2, 4, 7, 8, 11, 13, 14]) == []

def test_filter_multiples_negative_numbers():
    # Test with negative numbers
    assert filter_multiples_3_or_5([-3, -5, -6, -10, -15, 3, 5, 6, 10, 15]) == [-6, -5, -3, 3, 5, 6, 10]

def test_filter_multiples_large_range():
    # Test with a larger range of numbers
    input_list = list(range(1, 31))
    expected = [3, 5, 6, 7, 9, 10, 11, 12, 14, 15, 18, 19, 21, 22, 24, 25, 27, 28]
    assert filter_multiples_3_or_5(input_list) == expected

def test_filter_multiples_sorted():
    # Test that the output is always sorted
    unsorted_input = [10, 3, 15, 6, 5, 1, 12]
    assert filter_multiples_3_or_5(unsorted_input) == [3, 5, 6, 10]