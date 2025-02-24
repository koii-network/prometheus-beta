import pytest
from src.find_common import find_common

def test_find_common_basic():
    """Test basic functionality of finding common elements"""
    assert set(find_common([1, 2, 3], [3, 4, 5])) == {3}
    assert set(find_common(['a', 'b', 'c'], ['b', 'c', 'd'])) == {'b', 'c'}

def test_find_common_empty_lists():
    """Test scenarios with empty lists"""
    assert find_common([], [1, 2, 3]) == []
    assert find_common([1, 2, 3], []) == []
    assert find_common([], []) == []

def test_find_common_no_overlap():
    """Test lists with no common elements"""
    assert find_common([1, 2, 3], [4, 5, 6]) == []

def test_find_common_duplicates():
    """Test lists with duplicate elements"""
    assert set(find_common([1, 1, 2, 2], [2, 2, 3, 3])) == {2}

def test_find_common_different_types():
    """Test lists with different types of elements"""
    assert set(find_common([1, 'a', 2], ['a', 3, 2])) == {'a', 2}

def test_find_common_hashable_elements():
    """Ensure function works with hashable elements"""
    class CustomHashable:
        def __init__(self, value):
            self.value = value
        
        def __eq__(self, other):
            return self.value == other.value
        
        def __hash__(self):
            return hash(self.value)

    obj1 = CustomHashable(1)
    obj2 = CustomHashable(1)
    obj3 = CustomHashable(2)

    assert find_common([obj1, obj2], [obj2, obj3]) == [obj2]