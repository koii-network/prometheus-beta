import pytest
from src.local_maximum_finder import find_local_maxima

def test_find_local_maxima_basic():
    """Test basic functionality with multiple local maxima"""
    arr = [1, 3, 2, 4, 1, 5, 3]
    assert find_local_maxima(arr) == [1, 3, 5]

def test_find_local_maxima_single_element():
    """Test with a single element array"""
    arr = [42]
    assert find_local_maxima(arr) == [0]

def test_find_local_maxima_two_elements():
    """Test with two elements"""
    arr1 = [5, 3]
    assert find_local_maxima(arr1) == [0]
    
    arr2 = [3, 5]
    assert find_local_maxima(arr2) == [1]

def test_find_local_maxima_all_same():
    """Test with all elements being the same"""
    arr = [2, 2, 2, 2]
    assert find_local_maxima(arr) == []

def test_find_local_maxima_increasing():
    """Test with strictly increasing array"""
    arr = [1, 2, 3, 4, 5]
    assert find_local_maxima(arr) == [4]

def test_find_local_maxima_decreasing():
    """Test with strictly decreasing array"""
    arr = [5, 4, 3, 2, 1]
    assert find_local_maxima(arr) == [0]

def test_invalid_input_type():
    """Test with invalid input type"""
    with pytest.raises(TypeError):
        find_local_maxima("not a list")

def test_empty_list():
    """Test with empty list"""
    with pytest.raises(ValueError):
        find_local_maxima([])