import pytest
from src.find_common import find_common

def test_find_common_basic():
    """Test basic functionality of find_common with different types of lists."""
    assert set(find_common([1, 2, 3], [3, 4, 5])) == {3}
    assert set(find_common(['a', 'b', 'c'], ['b', 'c', 'd'])) == {'b', 'c'}

def test_find_common_empty_lists():
    """Test find_common with empty lists."""
    assert find_common([], [1, 2, 3]) == []
    assert find_common([1, 2, 3], []) == []
    assert find_common([], []) == []

def test_find_common_no_overlap():
    """Test find_common with lists that have no common elements."""
    assert find_common([1, 2, 3], [4, 5, 6]) == []

def test_find_common_duplicate_elements():
    """Test find_common with lists containing duplicate elements."""
    assert set(find_common([1, 1, 2, 3], [1, 3, 3, 4])) == {1, 3}

def test_find_common_different_types():
    """Test find_common with lists of different types."""
    assert set(find_common([1, 'a', 2], [1, 'a', 3])) == {1, 'a'}

def test_find_common_type_integrity():
    """Ensure the function returns a list."""
    result = find_common([1, 2, 3], [3, 4, 5])
    assert isinstance(result, list)