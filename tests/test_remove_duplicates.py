import pytest
from src.remove_duplicates import remove_duplicates

def test_remove_duplicates_typical_case():
    """Test removing duplicates from a typical list of integers."""
    assert remove_duplicates([1, 2, 3, 2, 4, 1, 5]) == [1, 2, 3, 4, 5]

def test_remove_duplicates_empty_list():
    """Test removing duplicates from an empty list."""
    assert remove_duplicates([]) == []

def test_remove_duplicates_all_same():
    """Test removing duplicates when all elements are the same."""
    assert remove_duplicates([1, 1, 1, 1]) == [1]

def test_remove_duplicates_preserve_order():
    """Test that the order of first occurrences is preserved."""
    assert remove_duplicates([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [3, 1, 4, 5, 9, 2, 6]

def test_remove_duplicates_mixed_types():
    """Test handling of lists with different orders and number of duplicates."""
    test_cases = [
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([5, 4, 3, 2, 1], [5, 4, 3, 2, 1]),
        ([1, 1, 2, 2, 3, 3, 4, 4, 5, 5], [1, 2, 3, 4, 5])
    ]
    
    for input_list, expected in test_cases:
        assert remove_duplicates(input_list) == expected