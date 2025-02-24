import pytest
from src.remove_duplicates import remove_duplicates

def test_remove_duplicates_basic():
    """Test basic functionality of removing duplicates."""
    assert remove_duplicates([1, 2, 3, 2, 1]) == [1, 2, 3]

def test_remove_duplicates_empty_list():
    """Test behavior with an empty list."""
    assert remove_duplicates([]) == []

def test_remove_duplicates_no_duplicates():
    """Test list with no duplicates."""
    assert remove_duplicates([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_remove_duplicates_all_duplicates():
    """Test list with all duplicate values."""
    assert remove_duplicates([1, 1, 1, 1]) == [1]

def test_remove_duplicates_mixed_types():
    """Test list with mixed types of duplicates."""
    assert remove_duplicates([1, '1', 1, 'a', 'a', 2]) == [1, '1', 'a', 2]

def test_remove_duplicates_preserve_order():
    """Test that the first occurrence of each element is preserved."""
    assert remove_duplicates([3, 1, 2, 1, 3, 4]) == [3, 1, 2, 4]

def test_remove_duplicates_invalid_input():
    """Test that a TypeError is raised for non-list inputs."""
    with pytest.raises(TypeError, match="Input must be a list"):
        remove_duplicates("not a list")
    
    with pytest.raises(TypeError, match="Input must be a list"):
        remove_duplicates(123)
    
    with pytest.raises(TypeError, match="Input must be a list"):
        remove_duplicates(None)