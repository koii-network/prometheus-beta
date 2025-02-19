import pytest
from src.find_second_highest import find_second_highest

def test_ascending_sorted_list():
    """Test a sorted list in ascending order."""
    assert find_second_highest([1, 2, 3, 4, 5]) == 4

def test_descending_sorted_list():
    """Test a sorted list in descending order."""
    assert find_second_highest([5, 4, 3, 2, 1]) == 4

def test_list_with_duplicate_values():
    """Test a list with duplicate values."""
    assert find_second_highest([1, 2, 2, 3, 3, 4, 5]) == 4

def test_list_with_all_same_values():
    """Test a list where all values are the same."""
    assert find_second_highest([2, 2, 2, 2]) == None

def test_small_list():
    """Test lists with fewer than 2 elements."""
    assert find_second_highest([]) == None
    assert find_second_highest([1]) == None

def test_invalid_input_type():
    """Test handling of non-list inputs."""
    with pytest.raises(TypeError):
        find_second_highest("not a list")
    with pytest.raises(TypeError):
        find_second_highest(123)

def test_non_integer_list():
    """Test handling of lists with non-integer elements."""
    with pytest.raises(ValueError):
        find_second_highest([1, 2, "3", 4])
    with pytest.raises(ValueError):
        find_second_highest([1.5, 2.5, 3.5])