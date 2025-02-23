import pytest
from src.array_common_element import has_common_element

def test_common_element_exists():
    """Test when a common element exists"""
    arr1 = [1, 2, 3, 4]
    arr2 = [4, 5, 6, 7]
    assert has_common_element(arr1, arr2) == True

def test_no_common_element():
    """Test when no common element exists"""
    arr1 = [1, 2, 3]
    arr2 = [4, 5, 6]
    assert has_common_element(arr1, arr2) == False

def test_empty_arrays():
    """Test with empty arrays"""
    arr1 = []
    arr2 = []
    assert has_common_element(arr1, arr2) == False

def test_one_empty_array():
    """Test with one empty array"""
    arr1 = [1, 2, 3]
    arr2 = []
    assert has_common_element(arr1, arr2) == False

def test_first_element_common():
    """Test when first elements are common"""
    arr1 = [1, 2, 3]
    arr2 = [1, 4, 5]
    assert has_common_element(arr1, arr2) == True

def test_last_element_common():
    """Test when last elements are common"""
    arr1 = [1, 2, 3]
    arr2 = [4, 5, 3]
    assert has_common_element(arr1, arr2) == True

def test_invalid_input_types():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError):
        has_common_element("not a list", [1, 2, 3])
    
    with pytest.raises(TypeError):
        has_common_element([1, 2, 3], "not a list")

def test_different_element_types():
    """Test common elements with different types"""
    arr1 = [1, "a", 3.14]
    arr2 = ["b", 3.14, 5]
    assert has_common_element(arr1, arr2) == True