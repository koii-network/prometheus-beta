import pytest
from src.unique_sorted_integers import get_unique_sorted_integers

def test_basic_unique_sorted():
    """Test basic functionality of returning unique sorted integers."""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    assert get_unique_sorted_integers(input_list) == [1, 2, 3, 4, 5, 6, 9]

def test_already_sorted_list():
    """Test a list that is already sorted."""
    input_list = [1, 2, 3, 4, 5]
    assert get_unique_sorted_integers(input_list) == [1, 2, 3, 4, 5]

def test_empty_list():
    """Test an empty list."""
    input_list = []
    assert get_unique_sorted_integers(input_list) == []

def test_list_with_negatives():
    """Test a list with negative numbers."""
    input_list = [-3, 1, -3, 0, 5, 1]
    assert get_unique_sorted_integers(input_list) == [-3, 0, 1, 5]

def test_type_error_non_list():
    """Test that a TypeError is raised for non-list inputs."""
    with pytest.raises(TypeError, match="Input must be a list"):
        get_unique_sorted_integers("not a list")

def test_type_error_non_integers():
    """Test that a TypeError is raised for lists with non-integer elements."""
    with pytest.raises(TypeError, match="All elements must be integers"):
        get_unique_sorted_integers([1, 2, "3", 4])