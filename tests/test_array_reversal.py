import pytest
from src.array_reversal import reverse_array

def test_reverse_integer_array():
    """Test reversing an array of integers."""
    assert reverse_array([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]

def test_reverse_string_array():
    """Test reversing an array of strings."""
    assert reverse_array(['apple', 'banana', 'cherry']) == ['cherry', 'banana', 'apple']

def test_reverse_empty_array():
    """Test reversing an empty array."""
    assert reverse_array([]) == []

def test_reverse_single_element_array():
    """Test reversing an array with a single element."""
    assert reverse_array([42]) == [42]

def test_reverse_mixed_type_array():
    """Test reversing an array with mixed types."""
    assert reverse_array([1, 'two', 3.0, [4]]) == [[4], 3.0, 'two', 1]

def test_reverse_invalid_input():
    """Test that a TypeError is raised for non-iterable input."""
    with pytest.raises(TypeError):
        reverse_array(42)

def test_reverse_tuple():
    """Test that the function works with tuples as well."""
    assert reverse_array((1, 2, 3)) == [3, 2, 1]