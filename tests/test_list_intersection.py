import pytest
from src.list_intersection import find_list_intersection

def test_list_intersection_basic():
    """Test basic list intersection."""
    assert sorted(find_list_intersection([1, 2, 3], [3, 4, 5])) == [3]

def test_list_intersection_no_common_elements():
    """Test lists with no common elements."""
    assert find_list_intersection([1, 2], [3, 4]) == []

def test_list_intersection_duplicate_elements():
    """Test lists with duplicate elements."""
    assert sorted(find_list_intersection([1, 2, 2, 3], [2, 3, 3, 4])) == [2, 3]

def test_list_intersection_empty_lists():
    """Test intersection with empty lists."""
    assert find_list_intersection([], [1, 2, 3]) == []
    assert find_list_intersection([1, 2, 3], []) == []

def test_list_intersection_different_types():
    """Test lists with different element types."""
    assert sorted(find_list_intersection([1, 'a', 2], [2, 'a', 3])) == [2, 'a']