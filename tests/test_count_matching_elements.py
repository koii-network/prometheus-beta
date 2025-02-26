import pytest
from src.count_matching_elements import count_matching_elements

def test_basic_matching():
    """Test basic matching of elements between two arrays."""
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [3, 4, 5, 6, 7]
    assert count_matching_elements(arr1, arr2) == 3

def test_no_matching_elements():
    """Test case with no matching elements."""
    arr1 = [1, 2, 3]
    arr2 = [4, 5, 6]
    assert count_matching_elements(arr1, arr2) == 0

def test_all_matching_elements():
    """Test case where all elements match."""
    arr1 = [1, 2, 3]
    arr2 = [1, 2, 3, 4, 5]
    assert count_matching_elements(arr1, arr2) == 3

def test_empty_arrays():
    """Test with empty arrays."""
    arr1 = []
    arr2 = [1, 2, 3]
    assert count_matching_elements(arr1, arr2) == 0
    assert count_matching_elements(arr2, arr1) == 0

def test_duplicates_in_first_array():
    """Test array with duplicate elements."""
    arr1 = [1, 1, 2, 2, 3]
    arr2 = [1, 2]
    assert count_matching_elements(arr1, arr2) == 4

def test_invalid_input_type():
    """Test invalid input types raise TypeError."""
    with pytest.raises(TypeError, match="Both arguments must be lists"):
        count_matching_elements(123, [1, 2, 3])
    
    with pytest.raises(TypeError, match="Both arguments must be lists"):
        count_matching_elements([1, 2, 3], "not a list")

def test_invalid_element_type():
    """Test non-integer elements raise TypeError."""
    with pytest.raises(TypeError, match="All elements must be integers"):
        count_matching_elements([1, 2, '3'], [1, 2, 3])
    
    with pytest.raises(TypeError, match="All elements must be integers"):
        count_matching_elements([1, 2, 3], [1, 2, 'a'])