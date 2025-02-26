import pytest
from src.array_transformer import transform_array

def test_basic_transformation():
    """Test basic array transformation"""
    input_array = [[1, 2, 3], [4, 5], [6, 7, 8]]
    expected = [3, 2, 1, 5, 4, 8, 7, 6]
    assert transform_array(input_array) == expected

def test_empty_subarrays():
    """Test removal of empty sub-arrays"""
    input_array = [[1, 2], [], [3, 4], []]
    expected = [2, 1, 4, 3]
    assert transform_array(input_array) == expected

def test_duplicates_removal():
    """Test removal of duplicates while maintaining order"""
    input_array = [[1, 2, 2], [3, 1, 4], [2, 5]]
    expected = [2, 1, 3, 4, 5]
    assert transform_array(input_array) == expected

def test_complex_nested_array():
    """Test with more complex nested arrays"""
    input_array = [[1, 2], [3, [4, 5]], [6, 7]]
    expected = [2, 1, 5, 4, 3, 7, 6]
    assert transform_array(input_array) == expected

def test_invalid_input():
    """Test handling of invalid input"""
    with pytest.raises(TypeError):
        transform_array("not a list")

def test_empty_input():
    """Test empty input list"""
    assert transform_array([]) == []

def test_mixed_type_array():
    """Test array with mixed types"""
    input_array = [[1, 'a'], [2, 'b'], [1, 'c']]
    expected = ['a', 1, 'b', 2, 'c']
    assert transform_array(input_array) == expected