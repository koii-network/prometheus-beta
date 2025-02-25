import pytest
from src.array_common_element import has_common_element

def test_common_element_exists():
    """Test when arrays have a common element"""
    assert has_common_element([1, 2, 3], [3, 4, 5]) == True

def test_no_common_element():
    """Test when arrays have no common elements"""
    assert has_common_element([1, 2, 3], [4, 5, 6]) == False

def test_empty_arrays():
    """Test with empty arrays"""
    assert has_common_element([], []) == False
    assert has_common_element([1, 2], []) == False
    assert has_common_element([], [3, 4]) == False

def test_same_array():
    """Test when both inputs are the same array"""
    arr = [1, 2, 3]
    assert has_common_element(arr, arr) == True

def test_different_types():
    """Test with elements of different types"""
    assert has_common_element([1, 'a', 2], ['b', 'a', 3]) == True

def test_type_error():
    """Test type error handling"""
    with pytest.raises(TypeError):
        has_common_element(1, [1, 2])
    with pytest.raises(TypeError):
        has_common_element([1, 2], "not a list")
    with pytest.raises(TypeError):
        has_common_element(None, [1, 2])

def test_large_arrays():
    """Test with large arrays to verify performance"""
    large_arr1 = list(range(10000))
    large_arr2 = list(range(5000, 15000))
    assert has_common_element(large_arr1, large_arr2) == True