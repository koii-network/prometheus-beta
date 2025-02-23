import pytest
from src.reverse_list import reverse_list

def test_reverse_list_normal():
    """Test reversing a standard list of integers."""
    input_list = [1, 2, 3, 4, 5]
    assert reverse_list(input_list) == [5, 4, 3, 2, 1]

def test_reverse_list_empty():
    """Test reversing an empty list."""
    assert reverse_list([]) == []

def test_reverse_list_single_element():
    """Test reversing a list with a single element."""
    assert reverse_list([42]) == [42]

def test_reverse_list_duplicate_elements():
    """Test reversing a list with duplicate elements."""
    input_list = [1, 2, 2, 3, 1]
    assert reverse_list(input_list) == [1, 3, 2, 2, 1]

def test_reverse_list_negative_numbers():
    """Test reversing a list with negative numbers."""
    input_list = [-1, 0, 5, -10]
    assert reverse_list(input_list) == [-10, 5, 0, -1]

def test_reverse_list_invalid_input():
    """Test that a TypeError is raised for non-list inputs."""
    with pytest.raises(TypeError, match="Input must be a list"):
        reverse_list("not a list")
    
    with pytest.raises(TypeError, match="Input must be a list"):
        reverse_list(123)
    
    with pytest.raises(TypeError, match="Input must be a list"):
        reverse_list(None)