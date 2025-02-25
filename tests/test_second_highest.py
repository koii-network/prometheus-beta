import pytest
from src.second_highest import find_second_highest

def test_ascending_sorted_list():
    """Test finding second highest in an ascending sorted list."""
    assert find_second_highest([1, 2, 3, 4, 5]) == 4

def test_descending_sorted_list():
    """Test finding second highest in a descending sorted list."""
    assert find_second_highest([5, 4, 3, 2, 1]) == 4

def test_list_with_duplicates():
    """Test finding second highest in a list with duplicate values."""
    assert find_second_highest([1, 2, 2, 3, 3, 4, 5]) == 4

def test_list_with_all_duplicates():
    """Test list with all duplicate values."""
    assert find_second_highest([3, 3, 3, 3]) is None

def test_single_element_list():
    """Test list with only one element."""
    assert find_second_highest([1]) is None

def test_empty_list():
    """Test empty list."""
    assert find_second_highest([]) is None

def test_invalid_input_type():
    """Test raising TypeError for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        find_second_highest("not a list")

def test_invalid_list_content():
    """Test raising ValueError for non-integer list."""
    with pytest.raises(ValueError, match="List must contain only integers"):
        find_second_highest([1, 2, 'three', 4])

def test_mixed_sorted_list():
    """Test mixed but sorted list of integers."""
    assert find_second_highest([-5, -3, 0, 2, 10]) == 2