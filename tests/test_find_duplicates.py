import pytest
from src.find_duplicates import find_duplicates

def test_find_duplicates_basic():
    """Test basic functionality of finding duplicates."""
    assert find_duplicates([1, 2, 3, 4, 2, 3]) == [2, 3]

def test_find_duplicates_no_duplicates():
    """Test case with no duplicates."""
    assert find_duplicates([1, 2, 3, 4, 5]) == []

def test_find_duplicates_multiple_duplicates():
    """Test case with multiple duplicates."""
    assert find_duplicates([1, 1, 2, 2, 3, 3, 4, 4]) == [1, 2, 3, 4]

def test_find_duplicates_empty_list():
    """Test case with an empty list."""
    assert find_duplicates([]) == []

def test_find_duplicates_invalid_input_non_list():
    """Test case with non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        find_duplicates("not a list")

def test_find_duplicates_invalid_input_non_integers():
    """Test case with non-integer elements."""
    with pytest.raises(TypeError, match="All elements must be integers"):
        find_duplicates([1, 2, "3", 4])

def test_find_duplicates_order_preservation():
    """Test that duplicates are returned in sorted order."""
    assert find_duplicates([3, 1, 2, 2, 1, 3]) == [1, 2, 3]