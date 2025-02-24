import pytest
from src.max_array_finder import find_max_number

def test_find_max_number_positive_integers():
    """Test finding max in an array of positive integers."""
    assert find_max_number([1, 2, 3, 4, 5]) == 5
    assert find_max_number([10, 5, 8, 12, 3]) == 12

def test_find_max_number_mixed_integers():
    """Test finding max in an array with positive and negative integers."""
    assert find_max_number([-1, -5, 0, 10, -3]) == 10
    assert find_max_number([-100, -50, -20]) == -20

def test_find_max_number_floating_point():
    """Test finding max in an array of floating-point numbers."""
    assert find_max_number([1.5, 2.7, 0.3, 4.1]) == 4.1
    assert find_max_number([-1.5, 2.7, -0.3, 4.1]) == 4.1

def test_find_max_number_single_element():
    """Test finding max in an array with a single element."""
    assert find_max_number([42]) == 42
    assert find_max_number([-42]) == -42

def test_find_max_empty_list_raises_error():
    """Test that an empty list raises a ValueError."""
    with pytest.raises(ValueError, match="Cannot find maximum of an empty list"):
        find_max_number([])

def test_find_max_non_list_input_raises_error():
    """Test that non-list inputs raise a TypeError."""
    with pytest.raises(TypeError, match="Input must be a list"):
        find_max_number("not a list")
    with pytest.raises(TypeError, match="Input must be a list"):
        find_max_number(123)

def test_find_max_non_numeric_elements_raises_error():
    """Test that lists with non-numeric elements raise a TypeError."""
    with pytest.raises(TypeError, match="All elements must be numeric"):
        find_max_number([1, 2, "three", 4])
    with pytest.raises(TypeError, match="All elements must be numeric"):
        find_max_number([1, 2, None, 4])