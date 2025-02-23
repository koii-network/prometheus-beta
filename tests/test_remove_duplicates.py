import pytest
from src.remove_duplicates import remove_duplicates

def test_remove_duplicates_basic():
    """Test basic functionality of removing duplicates."""
    assert remove_duplicates([1, 2, 3, 2, 1, 5]) == [1, 2, 3, 5]

def test_remove_duplicates_strings():
    """Test removing duplicates from a list of strings."""
    assert remove_duplicates(['a', 'b', 'a', 'c']) == ['a', 'b', 'c']

def test_remove_duplicates_empty_list():
    """Test behavior with an empty list."""
    assert remove_duplicates([]) == []

def test_remove_duplicates_no_duplicates():
    """Test a list with no duplicates."""
    assert remove_duplicates([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_remove_duplicates_all_duplicates():
    """Test a list with all duplicate elements."""
    assert remove_duplicates([1, 1, 1, 1]) == [1]

def test_remove_duplicates_mixed_types():
    """Test removing duplicates with mixed types."""
    assert remove_duplicates([1, '1', 1, 'a', 'a', 2]) == [1, '1', 'a', 2]

def test_remove_duplicates_preserves_order():
    """Ensure the function preserves the original order of first occurrence."""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    assert remove_duplicates(input_list) == [3, 1, 4, 5, 9, 2, 6]