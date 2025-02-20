import pytest
from src.multi_array_transformer import transform_multi_array

def test_transform_multi_array_basic():
    # Basic transformation
    input_array = [[1, 2, 3], [4, 5], [6, 7, 8]]
    expected = [3, 2, 1, 5, 4, 8, 7, 6]
    assert transform_multi_array(input_array) == expected

def test_transform_multi_array_with_empty_subarrays():
    # Test removing empty sub-arrays
    input_array = [[1, 2], [], [3, 4], []]
    expected = [2, 1, 4, 3]
    assert transform_multi_array(input_array) == expected

def test_transform_multi_array_with_duplicates():
    # Test removing duplicates while maintaining order
    input_array = [[1, 2, 2], [3, 1, 4], [4, 5]]
    expected = [2, 1, 4, 3, 5]
    assert transform_multi_array(input_array) == expected

def test_transform_multi_array_empty_input():
    # Test with an empty input array
    input_array = []
    expected = []
    assert transform_multi_array(input_array) == expected

def test_transform_multi_array_mixed_types():
    # Test with mixed data types
    input_array = [[1, 'a'], ['b', 2], [3, 'a']]
    expected = ['a', 1, 2, 'b', 3, 'a']
    assert transform_multi_array(input_array) == expected