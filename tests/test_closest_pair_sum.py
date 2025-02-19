import pytest
from src.closest_pair_sum import find_closest_pair_sum

def test_basic_functionality():
    """Test basic scenario with clear closest pair"""
    arr = [1, 2, 3, 4, 5]
    target = 7
    result = find_closest_pair_sum(arr, target)
    assert result == (2, 5) or result == (3, 4)

def test_floating_point_target():
    """Test with floating point target and values"""
    arr = [1.5, 2.3, 4.7, 5.1, 6.2]
    target = 7.5
    result = find_closest_pair_sum(arr, target)
    assert result in [(2.3, 5.1), (1.5, 6.2)]

def test_negative_numbers():
    """Test with negative numbers"""
    arr = [-3, -2, 0, 1, 2, 3]
    target = -1
    result = find_closest_pair_sum(arr, target)
    assert result == (-3, 2)

def test_single_occurrence():
    """Test array with only one valid pair"""
    arr = [10, 20, 30, 40]
    target = 50
    result = find_closest_pair_sum(arr, target)
    assert result == (10, 40)

def test_empty_list():
    """Test with empty list"""
    arr = []
    target = 5
    result = find_closest_pair_sum(arr, target)
    assert result is None

def test_single_element_list():
    """Test with single element list"""
    arr = [5]
    target = 10
    result = find_closest_pair_sum(arr, target)
    assert result is None

def test_type_errors():
    """Test type validation"""
    with pytest.raises(TypeError, match="Input must be a list"):
        find_closest_pair_sum(123, 10)
    
    with pytest.raises(TypeError, match="Target must be a number"):
        find_closest_pair_sum([1, 2, 3], "target")

def test_non_numeric_elements():
    """Test list with non-numeric elements"""
    with pytest.raises(ValueError, match="All list elements must be numeric"):
        find_closest_pair_sum([1, 2, "3"], 5)

def test_multiple_closest_pairs():
    """Test scenario with multiple pairs equally close to target"""
    arr = [1, 4, 3, 5, 2]
    target = 7
    result = find_closest_pair_sum(arr, target)
    assert result in [(3, 4), (2, 5)]  # First occurrence matters