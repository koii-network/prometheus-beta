import pytest
from src.unique_sorted_integers import get_unique_sorted_integers

def test_basic_unique_sorted():
    """Test basic functionality of getting unique sorted integers."""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    expected = [1, 2, 3, 4, 5, 6, 9]
    assert get_unique_sorted_integers(input_list) == expected

def test_already_sorted_list():
    """Test a list that is already sorted."""
    input_list = [1, 2, 3, 4, 5]
    expected = [1, 2, 3, 4, 5]
    assert get_unique_sorted_integers(input_list) == expected

def test_empty_list():
    """Test handling of an empty list."""
    input_list = []
    expected = []
    assert get_unique_sorted_integers(input_list) == expected

def test_single_element_list():
    """Test a list with a single element."""
    input_list = [42]
    expected = [42]
    assert get_unique_sorted_integers(input_list) == expected

def test_negative_numbers():
    """Test list with negative numbers and duplicates."""
    input_list = [-3, -1, 0, -3, 5, -1, 7]
    expected = [-3, -1, 0, 5, 7]
    assert get_unique_sorted_integers(input_list) == expected

def test_non_list_input():
    """Test raising TypeError for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        get_unique_sorted_integers(42)

def test_non_integer_elements():
    """Test raising TypeError for non-integer elements."""
    with pytest.raises(TypeError, match="All elements must be integers"):
        get_unique_sorted_integers([1, 2, "3", 4])