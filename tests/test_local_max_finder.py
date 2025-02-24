import pytest
from src.local_max_finder import find_local_maxima

def test_basic_local_maxima():
    """Test finding local maxima in a typical array"""
    assert find_local_maxima([1, 3, 2, 4, 1, 5]) == [1, 3, 5]

def test_ascending_array():
    """Test local maxima in an ascending array"""
    assert find_local_maxima([1, 2, 3, 4, 5]) == [4]

def test_descending_array():
    """Test local maxima in a descending array"""
    assert find_local_maxima([5, 4, 3, 2, 1]) == [0]

def test_single_element_array():
    """Test array with a single element"""
    assert find_local_maxima([42]) == [0]

def test_two_element_array_first_max():
    """Test two-element array where first is max"""
    assert find_local_maxima([5, 3]) == [0]

def test_two_element_array_second_max():
    """Test two-element array where second is max"""
    assert find_local_maxima([3, 5]) == [1]

def test_multiple_equal_maxima():
    """Test array with multiple potential local maxima"""
    assert find_local_maxima([1, 3, 3, 3, 1]) == [1, 2, 3]

def test_empty_list_raises_error():
    """Test that empty list raises ValueError"""
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        find_local_maxima([])

def test_non_list_input_raises_error():
    """Test that non-list input raises TypeError"""
    with pytest.raises(TypeError, match="Input must be a list"):
        find_local_maxima("not a list")