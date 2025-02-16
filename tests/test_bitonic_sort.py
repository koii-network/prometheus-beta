import pytest
from src.bitonic_sort import bitonic_sort

def test_bitonic_sort_ascending():
    """Test bitonic sort with ascending order"""
    arr = [3, 7, 4, 8, 6, 2, 1, 5]
    assert bitonic_sort(arr) == [1, 2, 3, 4, 5, 6, 7, 8]

def test_bitonic_sort_descending():
    """Test bitonic sort with descending order"""
    arr = [3, 7, 4, 8, 6, 2, 1, 5]
    assert bitonic_sort(arr, ascending=False) == [8, 7, 6, 5, 4, 3, 2, 1]

def test_bitonic_sort_empty_list():
    """Test bitonic sort with an empty list"""
    assert bitonic_sort([]) == []

def test_bitonic_sort_single_element():
    """Test bitonic sort with a single element"""
    assert bitonic_sort([42]) == [42]

def test_bitonic_sort_already_sorted():
    """Test bitonic sort with an already sorted list"""
    arr = [1, 2, 3, 4, 5]
    assert bitonic_sort(arr) == [1, 2, 3, 4, 5]

def test_bitonic_sort_reverse_sorted():
    """Test bitonic sort with a reverse sorted list"""
    arr = [5, 4, 3, 2, 1]
    assert bitonic_sort(arr) == [1, 2, 3, 4, 5]

def test_bitonic_sort_with_duplicates():
    """Test bitonic sort with duplicate elements"""
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    assert bitonic_sort(arr) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

def test_bitonic_sort_invalid_input():
    """Test bitonic sort with invalid input"""
    with pytest.raises(TypeError):
        bitonic_sort("not a list")

def test_bitonic_sort_non_comparable():
    """Test bitonic sort with non-comparable elements"""
    # This test might need to be adjusted based on exact implementation
    class NonComparable:
        pass
    
    non_comparable_list = [NonComparable(), NonComparable()]
    with pytest.raises(TypeError):
        bitonic_sort(non_comparable_list)