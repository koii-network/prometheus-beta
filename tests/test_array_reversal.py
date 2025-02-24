import pytest
from src.array_reversal import reverse_integer_array

def test_reverse_normal_array():
    """Test reversing a standard integer array."""
    input_arr = [1, 2, 3, 4, 5]
    expected = [5, 4, 3, 2, 1]
    assert reverse_integer_array(input_arr) == expected

def test_reverse_empty_array():
    """Test reversing an empty array."""
    assert reverse_integer_array([]) == []

def test_reverse_single_element_array():
    """Test reversing an array with a single element."""
    input_arr = [42]
    assert reverse_integer_array(input_arr) == [42]

def test_reverse_array_with_negative_numbers():
    """Test reversing an array with negative integers."""
    input_arr = [-1, -2, -3, -4, -5]
    expected = [-5, -4, -3, -2, -1]
    assert reverse_integer_array(input_arr) == expected

def test_reverse_array_with_mixed_numbers():
    """Test reversing an array with mixed positive and negative integers."""
    input_arr = [-10, 0, 5, 100, -42]
    expected = [-42, 100, 5, 0, -10]
    assert reverse_integer_array(input_arr) == expected

def test_raise_error_non_list_input():
    """Test that a TypeError is raised for non-list inputs."""
    with pytest.raises(TypeError, match="Input must be a list"):
        reverse_integer_array(42)
    with pytest.raises(TypeError, match="Input must be a list"):
        reverse_integer_array("not a list")

def test_raise_error_non_integer_elements():
    """Test that a TypeError is raised for lists with non-integer elements."""
    with pytest.raises(TypeError, match="All elements must be integers"):
        reverse_integer_array([1, 2, '3'])
    with pytest.raises(TypeError, match="All elements must be integers"):
        reverse_integer_array([1.5, 2, 3])