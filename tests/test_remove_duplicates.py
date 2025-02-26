import pytest
from src.remove_duplicates import remove_duplicates

def test_remove_duplicates_basic():
    """Test basic functionality of removing duplicates."""
    input_list = [1, 2, 3, 2, 4, 1, 5]
    expected = [1, 2, 3, 4, 5]
    assert remove_duplicates(input_list) == expected

def test_remove_duplicates_no_duplicates():
    """Test list with no duplicates."""
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert remove_duplicates(input_list) == input_list

def test_remove_duplicates_all_duplicates():
    """Test list with all duplicates."""
    input_list = [1, 1, 1, 1, 1]
    assert remove_duplicates(input_list) == [1]

def test_remove_duplicates_empty_list():
    """Test empty list."""
    assert remove_duplicates([]) == []

def test_remove_duplicates_order_preservation():
    """Test that original order is preserved."""
    input_list = [5, 2, 8, 2, 1, 5, 3, 8, 9]
    expected = [5, 2, 8, 1, 3, 9]
    assert remove_duplicates(input_list) == expected

def test_remove_duplicates_invalid_input_type():
    """Test that TypeError is raised for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        remove_duplicates("not a list")

def test_remove_duplicates_invalid_element_type():
    """Test that TypeError is raised for non-integer elements."""
    with pytest.raises(TypeError, match="All list elements must be integers"):
        remove_duplicates([1, 2, "3", 4])

def test_remove_duplicates_large_list():
    """Test a larger list with multiple duplicates."""
    input_list = list(range(20)) + list(range(10))
    expected = list(range(20))
    assert remove_duplicates(input_list) == expected