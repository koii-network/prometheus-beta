import pytest
from src.remove_duplicates import remove_duplicates

def test_remove_duplicates_basic():
    """Test basic functionality of removing duplicates."""
    assert remove_duplicates([1, 2, 3, 2, 4, 1, 5]) == [1, 2, 3, 4, 5]

def test_remove_duplicates_order_preservation():
    """Ensure original order of first occurrence is maintained."""
    input_list = [5, 2, 3, 2, 5, 4, 1, 3]
    assert remove_duplicates(input_list) == [5, 2, 3, 4, 1]

def test_remove_duplicates_no_duplicates():
    """Test list with no duplicates."""
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert remove_duplicates(input_list) == input_list

def test_remove_duplicates_all_duplicates():
    """Test list with all duplicates."""
    assert remove_duplicates([1, 1, 1, 1, 1]) == [1]

def test_remove_duplicates_empty_list():
    """Test empty list handling."""
    assert remove_duplicates([]) == []

def test_remove_duplicates_invalid_input_type():
    """Test raising TypeError for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        remove_duplicates("not a list")

def test_remove_duplicates_invalid_list_content():
    """Test raising ValueError for non-integer list elements."""
    with pytest.raises(ValueError, match="List must contain only integers"):
        remove_duplicates([1, 2, "3", 4, 5])

def test_remove_duplicates_large_list():
    """Test with a larger list of integers to ensure scalability."""
    large_list = list(range(20)) + list(range(10))
    assert remove_duplicates(large_list) == list(range(20))

def test_remove_duplicates_negative_integers():
    """Test handling of negative integers."""
    assert remove_duplicates([-1, 0, 1, -1, 2, 0, 3]) == [-1, 0, 1, 2, 3]