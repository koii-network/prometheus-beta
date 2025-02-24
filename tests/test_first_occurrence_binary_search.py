import pytest
from src.first_occurrence_binary_search import find_first_occurrence

def test_find_first_occurrence_basic():
    """Test basic functionality of finding first occurrence"""
    arr = [1, 2, 2, 3, 3, 3, 4, 5]
    assert find_first_occurrence(arr, 3) == 3
    assert find_first_occurrence(arr, 2) == 1

def test_find_first_occurrence_not_found():
    """Test scenario where target is not in the array"""
    arr = [1, 2, 3, 4, 5]
    assert find_first_occurrence(arr, 6) == -1
    assert find_first_occurrence(arr, 0) == -1

def test_find_first_occurrence_single_element():
    """Test with a single-element array"""
    arr = [5]
    assert find_first_occurrence(arr, 5) == 0
    assert find_first_occurrence(arr, 6) == -1

def test_find_first_occurrence_empty_array():
    """Test with an empty array"""
    arr = []
    assert find_first_occurrence(arr, 5) == -1

def test_find_first_occurrence_first_element():
    """Test when first element is the target"""
    arr = [1, 1, 2, 3, 4, 5]
    assert find_first_occurrence(arr, 1) == 0

def test_find_first_occurrence_last_element():
    """Test when last element is the target"""
    arr = [1, 2, 3, 4, 5, 5]
    assert find_first_occurrence(arr, 5) == 4

def test_invalid_input_type():
    """Test invalid input types"""
    with pytest.raises(TypeError):
        find_first_occurrence("not a list", 5)
    
    with pytest.raises(TypeError):
        find_first_occurrence([1, 2, 3], "not an int")

def test_invalid_array_contents():
    """Test invalid array contents"""
    with pytest.raises(ValueError):
        find_first_occurrence([-1, 2, 3], 2)
    
    with pytest.raises(ValueError):
        find_first_occurrence([1, 2, "3"], 2)