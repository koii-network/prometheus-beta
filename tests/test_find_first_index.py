import pytest
from src.find_first_index import find_first_index

def test_find_first_index_basic():
    """Test basic functionality of finding an existing value."""
    assert find_first_index([1, 2, 3, 4, 3], 3) == 2

def test_find_first_index_not_found():
    """Test when the target value is not in the list."""
    assert find_first_index([1, 2, 3, 4, 5], 6) == -1

def test_find_first_index_empty_list():
    """Test behavior with an empty list."""
    assert find_first_index([], 1) == -1

def test_find_first_index_first_element():
    """Test finding the first element in the list."""
    assert find_first_index([5, 2, 3, 4], 5) == 0

def test_find_first_index_last_element():
    """Test finding the last element in the list."""
    assert find_first_index([1, 2, 3, 4, 5], 5) == 4

def test_find_first_index_repeated_values():
    """Test when the target appears multiple times in the list."""
    assert find_first_index([1, 2, 3, 2, 4], 2) == 1

def test_find_first_index_negative_numbers():
    """Test with negative numbers."""
    assert find_first_index([-1, -2, 3, -1, 4], -1) == 0

def test_find_first_index_type_error():
    """Verify type handling."""
    with pytest.raises(TypeError):
        find_first_index([1, 2, 3], "3")