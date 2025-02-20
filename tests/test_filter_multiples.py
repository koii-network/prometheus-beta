import pytest
from src.filter_multiples import filter_special_multiples

def test_basic_filtering():
    # Test basic filtering of multiples
    input_list = [1, 2, 3, 4, 5, 6, 9, 10, 12, 15, 18, 20]
    expected = [3, 5, 6, 9, 10, 12, 18, 20]
    assert filter_special_multiples(input_list) == expected

def test_empty_list():
    # Test with an empty list
    assert filter_special_multiples([]) == []

def test_no_matching_multiples():
    # Test with a list that has no special multiples
    assert filter_special_multiples([1, 2, 4, 7, 11]) == []

def test_only_special_multiples():
    # Test with only special multiples
    input_list = [3, 5, 6, 10, 9, 20]
    expected = [3, 5, 6, 9, 10, 20]
    assert filter_special_multiples(input_list) == expected

def test_negative_numbers():
    # Test with negative numbers
    input_list = [-3, -5, -6, -10, -9, -20, 3, 5, 6, 10, 9, 20]
    expected = [-3, -5, -6, -9, -10, -20, 3, 5, 6, 9, 10, 20]
    assert filter_special_multiples(input_list) == expected

def test_duplicates():
    # Test with duplicate numbers
    input_list = [3, 3, 5, 5, 6, 10, 9, 20]
    expected = [3, 5, 6, 9, 10, 20]
    assert filter_special_multiples(input_list) == expected