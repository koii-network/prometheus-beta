import pytest
from src.array_reversal import reverse_array

def test_reverse_array_normal():
    """Test reversing a list of integers."""
    test_list = [1, 2, 3, 4, 5]
    assert reverse_array(test_list) == [5, 4, 3, 2, 1]

def test_reverse_array_mixed_types():
    """Test reversing a list with mixed types."""
    test_list = [1, 'hello', True, 3.14]
    assert reverse_array(test_list) == [3.14, True, 'hello', 1]

def test_reverse_array_empty():
    """Test reversing an empty list."""
    test_list = []
    assert reverse_array(test_list) == []

def test_reverse_array_single_element():
    """Test reversing a list with a single element."""
    test_list = [42]
    assert reverse_array(test_list) == [42]

def test_reverse_array_invalid_input():
    """Test that a TypeError is raised for non-list inputs."""
    with pytest.raises(TypeError, match="Input must be a list"):
        reverse_array("not a list")
    with pytest.raises(TypeError, match="Input must be a list"):
        reverse_array(123)
    with pytest.raises(TypeError, match="Input must be a list"):
        reverse_array(None)