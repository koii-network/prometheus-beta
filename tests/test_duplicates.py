import pytest
from src.duplicates import find_duplicates

def test_find_duplicates_basic():
    """Test finding basic duplicates in a list."""
    assert find_duplicates([1, 2, 3, 2, 4, 1]) == [1, 2]

def test_find_duplicates_no_duplicates():
    """Test when no duplicates exist."""
    assert find_duplicates([1, 2, 3, 4, 5]) == []

def test_find_duplicates_all_duplicates():
    """Test when all elements are duplicates."""
    assert find_duplicates([1, 1, 1, 1]) == [1]

def test_find_duplicates_multiple_duplicates():
    """Test with multiple sets of duplicates."""
    assert find_duplicates([1, 2, 2, 3, 3, 4, 5, 5]) == [2, 3, 5]

def test_find_duplicates_empty_list():
    """Test with an empty list."""
    assert find_duplicates([]) == []

def test_find_duplicates_invalid_input_type():
    """Test raising TypeError for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        find_duplicates("not a list")

def test_find_duplicates_invalid_element_type():
    """Test raising TypeError for list with non-integer elements."""
    with pytest.raises(TypeError, match="All elements must be integers"):
        find_duplicates([1, 2, "3", 4])

def test_find_duplicates_sorted_output():
    """Test that the output is sorted."""
    assert find_duplicates([3, 1, 2, 2, 1, 3]) == [1, 2, 3]