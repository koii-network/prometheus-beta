import pytest
from src.two_sum import find_two_sum

def test_basic_two_sum():
    """Test finding two numbers that sum to the target."""
    assert find_two_sum([2, 7, 11, 15], 9) == (0, 1)

def test_multiple_solutions():
    """Test finding the first solution when multiple exist."""
    assert find_two_sum([3, 2, 4], 6) == (1, 2)

def test_same_number_solution():
    """Test when the same number is used twice."""
    assert find_two_sum([3, 3], 6) == (0, 1)

def test_no_solution():
    """Test when no solution exists."""
    assert find_two_sum([1, 2, 3, 4], 10) is None

def test_empty_list():
    """Test with an empty list."""
    assert find_two_sum([], 5) is None

def test_invalid_input_not_list():
    """Test that TypeError is raised for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        find_two_sum("not a list", 5)

def test_invalid_target():
    """Test that TypeError is raised for invalid target."""
    with pytest.raises(TypeError, match="Target must be a number"):
        find_two_sum([1, 2, 3], "not a number")

def test_non_numeric_list():
    """Test that ValueError is raised for non-numeric list."""
    with pytest.raises(ValueError, match="List must contain only numeric elements"):
        find_two_sum([1, 2, "three"], 5)

def test_large_list():
    """Test with a larger list to ensure efficiency."""
    large_list = list(range(1000))
    assert find_two_sum(large_list, 1998) == (999, 999)

def test_negative_numbers():
    """Test with negative numbers."""
    assert find_two_sum([-1, -2, -3, -4, -5], -8) == (2, 4)

def test_mixed_numbers():
    """Test with mixed positive and negative numbers."""
    assert find_two_sum([-1, 2, 3, -4, 5], 1) == (1, 3)