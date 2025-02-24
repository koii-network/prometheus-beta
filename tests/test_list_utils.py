import pytest
from src.list_utils import find_duplicates


def test_find_duplicates_basic():
    """Test basic duplicate finding."""
    assert find_duplicates([1, 2, 3, 4, 2, 5, 6, 3, 7]) == [2, 3]


def test_find_duplicates_multiple_duplicates():
    """Test finding multiple duplicates."""
    assert find_duplicates([1, 1, 2, 2, 3, 3, 4, 4]) == [1, 2, 3, 4]


def test_find_duplicates_order_preservation():
    """Test that duplicates are returned in the order of first appearance."""
    assert find_duplicates([3, 1, 2, 3, 1, 4, 2]) == [3, 1, 2]


def test_find_duplicates_empty_list():
    """Test behavior with an empty list."""
    assert find_duplicates([]) == []


def test_find_duplicates_no_duplicates():
    """Test behavior when no duplicates exist."""
    assert find_duplicates([1, 2, 3, 4, 5]) == []


def test_find_duplicates_all_same():
    """Test list with all identical elements."""
    assert find_duplicates([1, 1, 1, 1]) == [1]


def test_find_duplicates_negative_numbers():
    """Test with negative numbers."""
    assert find_duplicates([-1, -2, -1, -3, -2]) == [-1, -2]