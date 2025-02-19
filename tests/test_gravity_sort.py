import pytest
from src.gravity_sort import gravity_sort

def test_gravity_sort_basic():
    """Test basic sorting functionality"""
    assert gravity_sort([5, 3, 1, 4, 2]) == [1, 2, 3, 4, 5]

def test_gravity_sort_already_sorted():
    """Test array that is already sorted"""
    assert gravity_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_gravity_sort_reverse_sorted():
    """Test array in reverse order"""
    assert gravity_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_gravity_sort_with_duplicates():
    """Test array with duplicate values"""
    assert gravity_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3]) == [1, 1, 2, 3, 3, 4, 5, 5, 6, 9]

def test_gravity_sort_empty_array():
    """Test empty array"""
    assert gravity_sort([]) == []

def test_gravity_sort_single_element():
    """Test array with single element"""
    assert gravity_sort([42]) == [42]

def test_gravity_sort_negative_numbers():
    """Test that negative numbers raise a ValueError"""
    with pytest.raises(ValueError, match="Gravity sort only works with non-negative integers"):
        gravity_sort([-1, 5, 3, 2])

def test_gravity_sort_large_numbers():
    """Test array with larger numbers"""
    assert gravity_sort([100, 50, 75, 25, 10]) == [10, 25, 50, 75, 100]