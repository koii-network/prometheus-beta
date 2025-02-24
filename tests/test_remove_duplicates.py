import pytest
from src.remove_duplicates import remove_duplicates

def test_remove_duplicates_basic():
    """Test basic removal of duplicates"""
    assert remove_duplicates([1, 2, 3, 2, 4, 1, 5]) == [1, 2, 3, 4, 5]

def test_remove_duplicates_empty_list():
    """Test handling of empty list"""
    assert remove_duplicates([]) == []

def test_remove_duplicates_all_same():
    """Test list with all identical elements"""
    assert remove_duplicates([1, 1, 1, 1]) == [1]

def test_remove_duplicates_no_duplicates():
    """Test list with no duplicates"""
    assert remove_duplicates([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_remove_duplicates_mixed_types():
    """Test list with mixed duplicate patterns"""
    assert remove_duplicates([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [3, 1, 4, 5, 9, 2, 6]

def test_remove_duplicates_order_preservation():
    """Ensure first occurrence order is preserved"""
    input_list = [5, 2, 7, 2, 5, 3, 7, 8]
    expected = [5, 2, 7, 3, 8]
    assert remove_duplicates(input_list) == expected

def test_remove_duplicates_negative_numbers():
    """Test with negative numbers"""
    assert remove_duplicates([-1, 2, -1, 3, 2, -1]) == [-1, 2, 3]

def test_remove_duplicates_large_input():
    """Test with a large input to verify performance"""
    large_input = list(range(10000)) + list(range(5000))
    result = remove_duplicates(large_input)
    assert len(result) == 10000
    assert result == list(range(10000))