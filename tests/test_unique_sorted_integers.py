import pytest
from src.unique_sorted_integers import get_unique_sorted_integers

def test_basic_unique_sorted():
    """Test basic functionality of unique sorted integers."""
    assert get_unique_sorted_integers([3, 1, 4, 1, 5, 9, 2, 6, 5]) == [1, 2, 3, 4, 5, 6, 9]

def test_already_sorted():
    """Test list that is already sorted."""
    assert get_unique_sorted_integers([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_all_duplicates():
    """Test list with all duplicate elements."""
    assert get_unique_sorted_integers([2, 2, 2, 2]) == [2]

def test_empty_list():
    """Test empty list."""
    assert get_unique_sorted_integers([]) == []

def test_negative_numbers():
    """Test list with negative numbers."""
    assert get_unique_sorted_integers([-3, -1, -3, 0, 1, -1]) == [-3, -1, 0, 1]

def test_invalid_input_type():
    """Test raising TypeError for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        get_unique_sorted_integers("not a list")

def test_invalid_list_type():
    """Test raising TypeError for list with non-integer elements."""
    with pytest.raises(TypeError, match="All elements must be integers"):
        get_unique_sorted_integers([1, 2, "3", 4])