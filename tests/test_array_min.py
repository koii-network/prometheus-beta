import pytest
from src.array_min import find_minimum

def test_find_minimum_positive_numbers():
    """Test finding minimum in a list of positive numbers."""
    assert find_minimum([1, 2, 3, 4, 5]) == 1
    assert find_minimum([5, 4, 3, 2, 1]) == 1
    assert find_minimum([10, 5, 8, 3, 7]) == 3

def test_find_minimum_mixed_numbers():
    """Test finding minimum in a list with mixed positive and negative numbers."""
    assert find_minimum([-1, 0, 1]) == -1
    assert find_minimum([-5, -2, -10, -1]) == -10
    assert find_minimum([-3, 0, 3]) == -3

def test_find_minimum_decimal_numbers():
    """Test finding minimum in a list with decimal numbers."""
    assert find_minimum([1.5, 2.3, 0.7, 3.1]) == 0.7
    assert find_minimum([-1.5, -2.3, -0.7]) == -2.3

def test_find_minimum_single_element():
    """Test finding minimum in a list with a single element."""
    assert find_minimum([42]) == 42

def test_find_minimum_error_empty_list():
    """Test raising ValueError for an empty list."""
    with pytest.raises(ValueError, match="Cannot find minimum of an empty list"):
        find_minimum([])

def test_find_minimum_error_non_list():
    """Test raising TypeError for non-list inputs."""
    with pytest.raises(TypeError, match="Input must be a list"):
        find_minimum("not a list")
    with pytest.raises(TypeError, match="Input must be a list"):
        find_minimum(123)

def test_find_minimum_error_non_numeric():
    """Test raising TypeError for lists with non-numeric elements."""
    with pytest.raises(TypeError, match="List must contain only numeric elements"):
        find_minimum([1, 2, "three"])
    with pytest.raises(TypeError, match="List must contain only numeric elements"):
        find_minimum([1, None, 3])