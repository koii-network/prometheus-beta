import pytest
from src.second_highest import find_second_highest

def test_ascending_list():
    """Test second highest in an ascending sorted list."""
    assert find_second_highest([1, 2, 3, 4, 5]) == 4

def test_descending_list():
    """Test second highest in a descending sorted list."""
    assert find_second_highest([5, 4, 3, 2, 1]) == 4

def test_list_with_duplicates():
    """Test list with duplicate values."""
    assert find_second_highest([1, 2, 2, 3, 3, 5]) == 3

def test_single_element_list():
    """Test list with less than 2 elements."""
    assert find_second_highest([1]) is None
    assert find_second_highest([]) is None

def test_invalid_input_type():
    """Test invalid input type."""
    with pytest.raises(TypeError, match="Input must be a list"):
        find_second_highest("not a list")

def test_non_integer_list():
    """Test list with non-integer elements."""
    with pytest.raises(ValueError, match="List must contain only integers"):
        find_second_highest([1, 2, "3", 4])

def test_two_element_list():
    """Test list with exactly two elements."""
    assert find_second_highest([1, 2]) == 1
    assert find_second_highest([2, 1]) == 1