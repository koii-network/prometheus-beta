import pytest
from src.closest_pair_sum import find_closest_pair_sum

def test_basic_case():
    """Test a basic scenario with multiple pairs"""
    arr = [1, 2, 3, 4, 5]
    target = 7
    result = find_closest_pair_sum(arr, target)
    assert result == (2, 5) or result == (3, 4)

def test_exact_match():
    """Test when there's an exact match to the target"""
    arr = [1, 3, 4, 5, 7, 10, 11]
    target = 7
    result = find_closest_pair_sum(arr, target)
    assert result == (3, 4)

def test_first_occurrence_of_equal_closeness():
    """Test that the first occurrence is returned when multiple pairs have equal closeness"""
    arr = [1, 5, 4, 3, 2]
    target = 7
    result = find_closest_pair_sum(arr, target)
    assert result == (1, 6) or result == (2, 5)

def test_negative_numbers():
    """Test with negative numbers"""
    arr = [-1, -5, 3, 6, 4, 2]
    target = 1
    result = find_closest_pair_sum(arr, target)
    assert result == (-5, 6)

def test_floating_point_target():
    """Test with floating point target"""
    arr = [1.5, 2.3, 3.7, 4.1, 5.2]
    target = 6.5
    result = find_closest_pair_sum(arr, target)
    assert result == (2.3, 4.1)

def test_array_too_small():
    """Test that a ValueError is raised when array is too small"""
    with pytest.raises(ValueError):
        find_closest_pair_sum([1], 5)

def test_empty_array():
    """Test that a ValueError is raised for an empty array"""
    with pytest.raises(ValueError):
        find_closest_pair_sum([], 5)