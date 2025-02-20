import pytest
from src.remove_duplicates import remove_duplicates

def test_remove_duplicates_basic():
    """Test basic duplicate removal."""
    assert remove_duplicates([1, 2, 2, 3, 4, 4, 5]) == [1, 2, 3, 4, 5]

def test_remove_duplicates_string_list():
    """Test duplicate removal with string list."""
    assert remove_duplicates(['a', 'b', 'a', 'c', 'b']) == ['a', 'b', 'c']

def test_remove_duplicates_empty_list():
    """Test duplicate removal with empty list."""
    assert remove_duplicates([]) == []

def test_remove_duplicates_no_duplicates():
    """Test list with no duplicates."""
    assert remove_duplicates([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_remove_duplicates_preserve_order():
    """Test that first occurrence's order is preserved."""
    input_list = [3, 1, 2, 1, 3, 4, 2, 5]
    assert remove_duplicates(input_list) == [3, 1, 2, 4, 5]

def test_remove_duplicates_invalid_input():
    """Test that TypeError is raised for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        remove_duplicates("not a list")
    with pytest.raises(TypeError, match="Input must be a list"):
        remove_duplicates(123)