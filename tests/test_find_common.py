import pytest
from src.find_common import find_common

def test_find_common_basic():
    """Test finding common elements in simple lists"""
    assert sorted(find_common([1, 2, 3], [3, 4, 5])) == [3]
    assert sorted(find_common(['a', 'b', 'c'], ['b', 'c', 'd'])) == ['b', 'c']

def test_find_common_empty_lists():
    """Test with empty lists"""
    assert find_common([], [1, 2, 3]) == []
    assert find_common([1, 2, 3], []) == []
    assert find_common([], []) == []

def test_find_common_no_common_elements():
    """Test lists with no common elements"""
    assert find_common([1, 2, 3], [4, 5, 6]) == []
    assert find_common(['a', 'b'], ['x', 'y']) == []

def test_find_common_duplicate_elements():
    """Test lists with duplicate elements"""
    assert sorted(find_common([1, 1, 2, 3], [1, 3, 3, 4])) == [1, 3]

def test_find_common_different_types():
    """Test lists with different element types"""
    with pytest.raises(TypeError):
        find_common([1, 2, 3], ['a', 'b', 'c'])