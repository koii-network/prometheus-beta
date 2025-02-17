import pytest
from src.find_single_non_duplicate import find_single_non_duplicate

def test_single_non_duplicate_middle():
    """Test finding single non-duplicate element in the middle of the array."""
    arr = [1, 1, 2, 3, 3, 4, 4, 5, 5]
    assert find_single_non_duplicate(arr) == 2

def test_single_non_duplicate_beginning():
    """Test finding single non-duplicate element at the beginning."""
    arr = [2, 3, 3, 4, 4, 5, 5]
    assert find_single_non_duplicate(arr) == 2

def test_single_non_duplicate_end():
    """Test finding single non-duplicate element at the end."""
    arr = [1, 1, 2, 2, 3, 3, 4]
    assert find_single_non_duplicate(arr) == 4

def test_single_element_array():
    """Test array with a single element."""
    arr = [42]
    assert find_single_non_duplicate(arr) == 42

def test_invalid_input_types():
    """Test handling of invalid input types."""
    with pytest.raises(ValueError):
        find_single_non_duplicate(None)
    
    with pytest.raises(ValueError):
        find_single_non_duplicate([])

def test_no_single_element():
    """Test error case where no single element exists."""
    with pytest.raises(ValueError):
        find_single_non_duplicate([1, 1, 2, 2, 3, 3])