import pytest
from src.remove_duplicates import remove_duplicates

def test_remove_duplicates_basic():
    """Test basic functionality of removing duplicates."""
    input_list = [1, 2, 3, 2, 4, 1, 5]
    assert remove_duplicates(input_list) == [1, 2, 3, 4, 5]

def test_remove_duplicates_preserve_order():
    """Ensure order is preserved when removing duplicates."""
    input_list = [5, 3, 1, 3, 2, 5, 4]
    assert remove_duplicates(input_list) == [5, 3, 1, 2, 4]

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

def test_remove_duplicates_invalid_input():
    """Test invalid input raises TypeError."""
    with pytest.raises(TypeError):
        remove_duplicates("not a list")
    with pytest.raises(TypeError):
        remove_duplicates(123)

def test_remove_duplicates_mixed_types():
    """Test list with mixed types."""
    input_list = [1, 2, 2, 'a', 'a', 3, 1, 4]
    assert remove_duplicates(input_list) == [1, 2, 'a', 3, 4]