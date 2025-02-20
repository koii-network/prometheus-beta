import pytest
from src.unique_pairs import get_unique_pairs

def test_unique_pairs_basic():
    """Test basic functionality with a simple list of integers."""
    result = get_unique_pairs([1, 2, 3])
    assert result == [(1, 2), (1, 3), (2, 3)]

def test_unique_pairs_with_duplicates():
    """Test list with duplicate elements."""
    result = get_unique_pairs([1, 1, 2, 2, 3])
    assert result == [(1, 2), (1, 3), (2, 3)]

def test_unique_pairs_empty_list():
    """Test with an empty list."""
    result = get_unique_pairs([])
    assert result == []

def test_unique_pairs_single_element():
    """Test with a single-element list."""
    result = get_unique_pairs([5])
    assert result == []

def test_unique_pairs_invalid_input_type():
    """Test with invalid input type."""
    with pytest.raises(TypeError, match="Input must be a list"):
        get_unique_pairs("not a list")

def test_unique_pairs_non_integer_elements():
    """Test with non-integer elements."""
    with pytest.raises(ValueError, match="All elements must be integers"):
        get_unique_pairs([1, 2, "3"])

def test_unique_pairs_negative_numbers():
    """Test with negative numbers."""
    result = get_unique_pairs([-1, 0, 1])
    assert result == [(-1, 0), (-1, 1), (0, 1)]