import pytest
from src.list_utils import remove_unique_elements

def test_remove_unique_elements_basic():
    # Basic test with duplicate elements
    assert set(remove_unique_elements([1, 2, 2, 3, 4, 4, 5])) == {2, 4}

def test_remove_unique_elements_no_duplicates():
    # Test with no duplicate elements
    assert remove_unique_elements([1, 2, 3, 4, 5]) == []

def test_remove_unique_elements_all_duplicates():
    # Test with all elements being duplicates
    assert set(remove_unique_elements([1, 1, 1, 1])) == {1}

def test_remove_unique_elements_empty_list():
    # Test with an empty list
    assert remove_unique_elements([]) == []

def test_remove_unique_elements_multiple_occurrences():
    # Test with multiple occurrences of duplicates
    assert set(remove_unique_elements([1, 2, 2, 2, 3, 3, 4, 4, 4, 4])) == {2, 3, 4}