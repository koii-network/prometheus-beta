import pytest
from src.array_common_element import has_common_element

def test_arrays_with_common_element():
    """Test arrays that have a common element"""
    assert has_common_element([1, 2, 3], [4, 5, 2]) == True
    assert has_common_element(['a', 'b', 'c'], ['x', 'y', 'a']) == True

def test_arrays_without_common_element():
    """Test arrays without a common element"""
    assert has_common_element([1, 2, 3], [4, 5, 6]) == False
    assert has_common_element(['a', 'b', 'c'], ['x', 'y', 'z']) == False

def test_empty_arrays():
    """Test scenarios with empty arrays"""
    assert has_common_element([], [1, 2, 3]) == False
    assert has_common_element([1, 2, 3], []) == False
    assert has_common_element([], []) == False

def test_different_types():
    """Test arrays with different types of elements"""
    assert has_common_element([1, 2, 3], [3.0, 4, 5]) == True
    assert has_common_element(['1', 1], [1, '2']) == True

def test_invalid_input_types():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError):
        has_common_element(None, [1, 2, 3])
    with pytest.raises(TypeError):
        has_common_element([1, 2, 3], "not a list")
    with pytest.raises(TypeError):
        has_common_element(123, 456)