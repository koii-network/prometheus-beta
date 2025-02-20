import pytest
from src.filter_multiples import filter_unique_multiples

def test_filter_unique_multiples_basic():
    # Test basic scenario with mix of multiples
    assert filter_unique_multiples([1, 2, 3, 5, 6, 9, 10, 15]) == [3, 5, 6, 10]

def test_filter_unique_multiples_empty_list():
    # Test with empty list
    assert filter_unique_multiples([]) == []

def test_filter_unique_multiples_no_matches():
    # Test list with no matching multiples
    assert filter_unique_multiples([1, 2, 4, 7, 8]) == []

def test_filter_unique_multiples_all_multiples():
    # Test list with all numbers being multiples
    assert filter_unique_multiples([3, 5, 6, 9, 10, 15, 12, 20]) == [3, 5, 6, 10, 12, 20]

def test_filter_unique_multiples_negative_numbers():
    # Test with negative numbers
    assert filter_unique_multiples([-3, -5, -6, -9, -10, -15]) == [-3, -5, -6, -10]

def test_filter_unique_multiples_sorting():
    # Test sorting of the result
    assert filter_unique_multiples([10, 3, 15, 6, 5, 9]) == [3, 5, 6, 10]