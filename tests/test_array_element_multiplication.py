import pytest
from src.array_element_multiplication import multiply_corresponding_elements

def test_multiply_numeric_arrays():
    # Test with numeric arrays
    arr1 = [1, 2, 3]
    arr2 = [4, 5, 6]
    assert multiply_corresponding_elements(arr1, arr2) == [4, 10, 18]

def test_multiply_mixed_type_arrays():
    # Test with mixed type arrays
    arr1 = [2, 'hello', 3.5]
    arr2 = [3, 2, 2.0]
    assert multiply_corresponding_elements(arr1, arr2) == [6, 'hellohello', 7.0]

def test_empty_arrays():
    # Test with empty arrays
    assert multiply_corresponding_elements([], []) == []

def test_arrays_different_lengths():
    # Test with arrays of different lengths
    with pytest.raises(ValueError, match="Input arrays must have the same length"):
        multiply_corresponding_elements([1, 2], [1, 2, 3])

def test_single_element_arrays():
    # Test with single-element arrays
    arr1 = [42]
    arr2 = [2]
    assert multiply_corresponding_elements(arr1, arr2) == [84]