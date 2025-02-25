import pytest
from src.find_first_index import find_first_index

def test_find_first_index_basic():
    """Test basic functionality of finding an existing element."""
    assert find_first_index([1, 2, 3, 2, 1], 2) == 1
    assert find_first_index([1, 2, 3, 2, 1], 1) == 0
    assert find_first_index([1, 2, 3, 2, 1], 3) == 2

def test_find_first_index_not_found():
    """Test when the target is not in the array."""
    assert find_first_index([1, 2, 3], 4) == -1
    assert find_first_index([], 1) == -1

def test_find_first_index_edge_cases():
    """Test edge cases like empty arrays and different types."""
    assert find_first_index([], 0) == -1
    assert find_first_index([None], None) == 0
    
def test_find_first_index_complex_types():
    """Test with complex types like lists, dicts, and objects."""
    assert find_first_index([[1,2], [3,4], [1,2]], [1,2]) == 0
    assert find_first_index([{'a':1}, {'b':2}, {'a':1}], {'a':1}) == 0
    
def test_find_first_index_different_types():
    """Test with elements of different types."""
    mixed_list = [1, '2', 3.0, True]
    assert find_first_index(mixed_list, '2') == 1
    # Note: In Python, True is 1, so this will find the first 1/True
    assert find_first_index(mixed_list, 1) == 0
    assert find_first_index(mixed_list, 3.0) == 2

def test_find_first_index_repeated_elements():
    """Test arrays with repeated elements."""
    arr = [1, 2, 2, 3, 2, 4]
    assert find_first_index(arr, 2) == 1
    assert find_first_index(arr, 4) == 5