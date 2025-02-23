import pytest
from src.smallest_sum import find_smallest_sum

def test_basic_scenario():
    """Test a basic scenario with positive integers"""
    assert find_smallest_sum([1, 2, 3], [4, 5, 6]) == 5

def test_empty_lists():
    """Test behavior with empty lists"""
    assert find_smallest_sum([], []) == 0
    assert find_smallest_sum([1, 2], []) == 0
    assert find_smallest_sum([], [3, 4]) == 0

def test_negative_numbers():
    """Test scenarios with negative numbers"""
    assert find_smallest_sum([-1, -2], [1, 2]) == 0
    assert find_smallest_sum([-5, -3], [-2, -1]) == -7

def test_single_element_lists():
    """Test lists with single elements"""
    assert find_smallest_sum([1], [2]) == 3
    assert find_smallest_sum([0], [0]) == 0

def test_input_validation():
    """Test input validation and error handling"""
    with pytest.raises(TypeError):
        find_smallest_sum(None, [1, 2])
    
    with pytest.raises(TypeError):
        find_smallest_sum([1, 2], None)
    
    with pytest.raises(ValueError):
        find_smallest_sum("not a list", [1, 2])
    
    with pytest.raises(ValueError):
        find_smallest_sum([1, 2], "not a list")
    
    with pytest.raises(ValueError):
        find_smallest_sum([1, 'a'], [3, 4])

def test_complex_scenarios():
    """Test more complex input scenarios"""
    assert find_smallest_sum([10, 20, 30], [1, 2, 3]) == 11
    assert find_smallest_sum([-1, 5], [-2, 3]) == -3
    assert find_smallest_sum([100], [50, 75]) == 150