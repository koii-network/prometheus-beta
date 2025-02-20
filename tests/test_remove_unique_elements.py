import pytest
from src.remove_unique_elements import remove_unique_elements

def test_remove_unique_elements_basic():
    # Test with multiple duplicates
    assert set(remove_unique_elements([1, 2, 2, 3, 3, 4])) == {2, 3}

def test_remove_unique_elements_no_duplicates():
    # Test with no duplicates
    assert remove_unique_elements([1, 2, 3, 4]) == []

def test_remove_unique_elements_all_duplicates():
    # Test with all elements duplicated
    assert set(remove_unique_elements([1, 1, 2, 2, 3, 3])) == {1, 2, 3}

def test_remove_unique_elements_empty_list():
    # Test with empty list
    assert remove_unique_elements([]) == []

def test_remove_unique_elements_multiple_occurrences():
    # Test with multiple occurrences of duplicates
    assert set(remove_unique_elements([1, 1, 1, 2, 2, 3, 3, 3, 4])) == {1, 2, 3}

def test_remove_unique_elements_mixed_order():
    # Test with mixed order of duplicates
    assert set(remove_unique_elements([3, 1, 2, 1, 3, 2])) == {1, 2, 3}