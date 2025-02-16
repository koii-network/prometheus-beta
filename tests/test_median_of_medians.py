import pytest
from src.median_of_medians import median_of_medians

def test_median_of_medians_basic():
    """Test basic functionality with an odd-length array"""
    arr = [1, 3, 5, 7, 9, 2, 4, 6, 8]
    assert median_of_medians(arr) == 5

def test_median_of_medians_even_length():
    """Test functionality with an even-length array"""
    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    assert median_of_medians(arr) == 4

def test_median_of_medians_all_same():
    """Test array with all identical elements"""
    arr = [5, 5, 5, 5, 5]
    assert median_of_medians(arr) == 5

def test_median_of_medians_sorted():
    """Test already sorted array"""
    arr = [1, 2, 3, 4, 5]
    assert median_of_medians(arr) == 3

def test_median_of_medians_reverse_sorted():
    """Test reverse sorted array"""
    arr = [5, 4, 3, 2, 1]
    assert median_of_medians(arr) == 3

def test_median_of_medians_large_array():
    """Test larger array"""
    arr = list(range(1, 101))  # 1 to 100
    assert median_of_medians(arr) == 50

def test_median_of_medians_with_duplicates():
    """Test array with duplicate values"""
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    assert median_of_medians(arr) == 4

def test_median_of_medians_empty_array():
    """Test that empty array raises ValueError"""
    with pytest.raises(ValueError):
        median_of_medians([])