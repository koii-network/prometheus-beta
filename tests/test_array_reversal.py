import pytest
from src.array_reversal import reverse_array

def test_reverse_array_basic():
    """Test reversing a basic list of integers."""
    input_list = [1, 2, 3, 4, 5]
    expected = [5, 4, 3, 2, 1]
    assert reverse_array(input_list) == expected

def test_reverse_array_empty():
    """Test reversing an empty list."""
    assert reverse_array([]) == []

def test_reverse_array_single_element():
    """Test reversing a list with a single element."""
    input_list = [42]
    assert reverse_array(input_list) == [42]

def test_reverse_array_mixed_types():
    """Test reversing a list with mixed types."""
    input_list = [1, 'a', True, 3.14]
    expected = [3.14, True, 'a', 1]
    assert reverse_array(input_list) == expected

def test_reverse_array_invalid_input():
    """Test that a TypeError is raised for non-list inputs."""
    with pytest.raises(TypeError, match="Input must be a list"):
        reverse_array("not a list")
    
    with pytest.raises(TypeError, match="Input must be a list"):
        reverse_array(123)
    
    with pytest.raises(TypeError, match="Input must be a list"):
        reverse_array(None)