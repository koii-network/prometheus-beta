import pytest
from src.filter_multiples import filter_special_multiples

def test_filter_special_multiples_basic():
    """Test basic functionality of filtering multiples."""
    input_list = [1, 2, 3, 4, 5, 6, 9, 10, 12, 15, 18, 20]
    expected = [3, 5, 6, 9, 10, 12, 18, 20]
    assert filter_special_multiples(input_list) == expected

def test_filter_special_multiples_empty_list():
    """Test with an empty list."""
    assert filter_special_multiples([]) == []

def test_filter_special_multiples_no_matches():
    """Test when no numbers match the criteria."""
    input_list = [1, 2, 4, 7, 11, 13]
    assert filter_special_multiples(input_list) == []

def test_filter_special_multiples_all_matches():
    """Test when all numbers match the criteria."""
    input_list = [3, 5, 6, 9, 10, 12, 15, 18, 20]
    expected = [3, 5, 6, 9, 10, 12, 18, 20]
    assert filter_special_multiples(input_list) == expected

def test_filter_special_multiples_negative_numbers():
    """Test with negative numbers."""
    input_list = [-3, -5, -6, -9, -10, -15, 3, 5, 6, 9, 10, 15]
    expected = [-9, -6, -5, -3, 3, 5, 6, 9, 10]
    assert filter_special_multiples(input_list) == expected