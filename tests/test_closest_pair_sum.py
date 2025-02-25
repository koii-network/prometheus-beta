import pytest
from src.closest_pair_sum import find_closest_pair_sum

def test_basic_functionality():
    """Test finding closest pair in a basic scenario"""
    arr = [1, 2, 3, 4, 5]
    target = 7
    result = find_closest_pair_sum(arr, target)
    assert result == (2, 5) or result == (3, 4)

def test_multiple_closest_pairs():
    """Test when multiple pairs have equal closeness"""
    arr = [1, 2, 3, 4, 5, 6]
    target = 7
    result = find_closest_pair_sum(arr, target)
    assert result == (1, 6)  # First occurrence should be returned

def test_negative_numbers():
    """Test array with negative numbers"""
    arr = [-1, -2, 3, 4, 5]
    target = 2
    result = find_closest_pair_sum(arr, target)
    assert result == (-2, 4)

def test_floating_point_target():
    """Test with floating point target"""
    arr = [1.5, 2.5, 3.5, 4.5]
    target = 6.0
    result = find_closest_pair_sum(arr, target)
    assert result == (2.5, 3.5)

def test_error_on_insufficient_elements():
    """Test error raised for arrays with fewer than 2 elements"""
    with pytest.raises(ValueError):
        find_closest_pair_sum([], 5)
    
    with pytest.raises(ValueError):
        find_closest_pair_sum([1], 5)

def test_large_array():
    """Test with a larger array"""
    arr = list(range(1, 101))
    target = 150
    result = find_closest_pair_sum(arr, target)
    assert result == (74, 75)

def test_exact_match():
    """Test when a pair matches the target exactly"""
    arr = [10, 20, 30, 40, 50]
    target = 50
    result = find_closest_pair_sum(arr, target)
    assert result == (20, 30)