import pytest
from src.find_index import find_first_index

def test_find_first_index_basic():
    """Test basic functionality of finding an index"""
    numbers = [1, 2, 3, 4, 5]
    assert find_first_index(numbers, 3) == 2
    assert find_first_index(numbers, 1) == 0
    assert find_first_index(numbers, 5) == 4

def test_find_first_index_not_found():
    """Test when target is not in the list"""
    numbers = [1, 2, 3, 4, 5]
    assert find_first_index(numbers, 6) == -1
    assert find_first_index(numbers, 0) == -1

def test_find_first_index_duplicate():
    """Test finding first index when multiple occurrences exist"""
    numbers = [1, 2, 2, 3, 2, 4]
    assert find_first_index(numbers, 2) == 1

def test_find_first_index_empty_list():
    """Test with an empty list"""
    numbers = []
    assert find_first_index(numbers, 1) == -1

def test_find_first_index_different_types():
    """Test error handling for non-integer inputs"""
    with pytest.raises(TypeError):
        find_first_index([1, 2, 3], "2")
    with pytest.raises(TypeError):
        find_first_index([1, 2, 3], 2.5)