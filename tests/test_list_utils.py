import pytest
from src.list_utils import remove_unique_elements

def test_remove_unique_elements_basic():
    """Test basic functionality of removing unique elements"""
    assert remove_unique_elements([1, 2, 3, 2, 4, 1, 5]) == [1, 2, 2, 1]

def test_remove_unique_elements_no_duplicates():
    """Test list with no duplicates returns empty list"""
    assert remove_unique_elements([1, 2, 3, 4, 5]) == []

def test_remove_unique_elements_empty_list():
    """Test empty list returns empty list"""
    assert remove_unique_elements([]) == []

def test_remove_unique_elements_all_same():
    """Test list with all same elements"""
    assert remove_unique_elements([1, 1, 1, 1]) == [1, 1, 1, 1]

def test_remove_unique_elements_mixed_duplicates():
    """Test list with mixed duplicate counts"""
    assert remove_unique_elements([1, 1, 2, 2, 2, 3, 4, 4, 5]) == [1, 1, 2, 2, 2, 4, 4]

def test_remove_unique_elements_type_preservation():
    """Ensure the function works with different integer types"""
    assert remove_unique_elements([1, 1, 2, 2, 3, 3.0]) == [1, 1, 2, 2, 3, 3.0]