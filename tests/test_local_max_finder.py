import pytest
from src.local_max_finder import find_local_maxima

def test_find_local_maxima_basic():
    """Test basic functionality of finding local maxima"""
    arr = [1, 3, 2, 4, 1, 5, 3]
    assert find_local_maxima(arr) == [1, 3, 5]

def test_find_local_maxima_single_element():
    """Test array with single element"""
    arr = [5]
    assert find_local_maxima(arr) == [0]

def test_find_local_maxima_two_elements():
    """Test array with two elements"""
    arr = [5, 3]
    assert find_local_maxima(arr) == [0]
    
    arr = [3, 5]
    assert find_local_maxima(arr) == [1]

def test_find_local_maxima_no_local_max():
    """Test array with no local maxima"""
    arr = [1, 2, 3, 4, 5]
    assert find_local_maxima(arr) == []
    
    arr = [5, 4, 3, 2, 1]
    assert find_local_maxima(arr) == [0]

def test_find_local_maxima_multiple_peaks():
    """Test array with multiple local peaks"""
    arr = [2, 4, 1, 5, 3, 7, 2]
    assert find_local_maxima(arr) == [1, 3, 5]

def test_find_local_maxima_invalid_input():
    """Test invalid input types"""
    with pytest.raises(TypeError):
        find_local_maxima("not a list")
    
    with pytest.raises(TypeError):
        find_local_maxima(123)

def test_find_local_maxima_empty_input():
    """Test empty input list"""
    with pytest.raises(ValueError):
        find_local_maxima([])