import pytest
import random
from src.bogosort import bogosort, is_sorted, shuffle

def test_bogosort_basic():
    """Test basic sorting functionality"""
    arr = [3, 1, 4, 1, 5, 9, 2, 6]
    result = bogosort(arr)
    assert is_sorted(result)
    assert sorted(arr) == result

def test_bogosort_already_sorted():
    """Test list that is already sorted"""
    arr = [1, 2, 3, 4, 5]
    result = bogosort(arr)
    assert is_sorted(result)
    assert result == arr

def test_bogosort_reverse_sorted():
    """Test reverse sorted list"""
    arr = [5, 4, 3, 2, 1]
    result = bogosort(arr)
    assert is_sorted(result)
    assert sorted(arr) == result

def test_bogosort_empty_list():
    """Test empty list"""
    arr = []
    result = bogosort(arr)
    assert result == []

def test_bogosort_single_element():
    """Test single element list"""
    arr = [42]
    result = bogosort(arr)
    assert result == arr

def test_bogosort_with_duplicates():
    """Test list with duplicate elements"""
    arr = [3, 1, 4, 1, 4, 1, 5]
    result = bogosort(arr)
    assert is_sorted(result)
    assert sorted(arr) == result

def test_bogosort_invalid_input():
    """Test invalid input types"""
    with pytest.raises(TypeError):
        bogosort(None)
    with pytest.raises(TypeError):
        bogosort(123)
    with pytest.raises(TypeError):
        bogosort("not a list")

def test_bogosort_uncomparable_elements():
    """Test list with elements that cannot be compared"""
    with pytest.raises(ValueError):
        bogosort([1, 2, '3', 4, 5])

def test_is_sorted():
    """Test is_sorted function"""
    assert is_sorted([1, 2, 3, 4, 5]) == True
    assert is_sorted([5, 4, 3, 2, 1]) == False
    assert is_sorted([]) == True
    assert is_sorted([42]) == True

def test_shuffle():
    """Test shuffle function"""
    arr = [1, 2, 3, 4, 5]
    shuffled = shuffle(arr)
    
    # Shuffled list should have same length
    assert len(shuffled) == len(arr)
    
    # Shuffled list should have same elements
    assert sorted(shuffled) == sorted(arr)
    
    # Verify that shuffled is different from original (with high probability)
    assert shuffled != arr