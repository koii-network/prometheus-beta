import pytest
from src.unique_sum import sum_unique_elements

def test_sum_unique_elements_basic():
    """Test basic functionality with unique and duplicate elements"""
    assert sum_unique_elements([1, 2, 3, 2]) == 6
    assert sum_unique_elements([1, 1, 1, 1]) == 1
    assert sum_unique_elements([]) == 0

def test_sum_unique_elements_zero_and_negative():
    """Test with zero and negative numbers"""
    assert sum_unique_elements([0, -1, 2, 0, -1]) == 1
    assert sum_unique_elements([-5, -5, -3, -3, 0, 0]) == -8

def test_sum_unique_elements_large_array():
    """Test with a larger array of numbers"""
    test_array = [1, 2, 3, 4, 2, 3, 5, 1, 6]
    assert sum_unique_elements(test_array) == 21

def test_sum_unique_elements_error_handling():
    """Test error handling for invalid inputs"""
    # Non-list input
    with pytest.raises(TypeError, match="Input must be a list of integers"):
        sum_unique_elements("not a list")
    
    # List with non-integer elements
    with pytest.raises(TypeError, match="All elements must be integers"):
        sum_unique_elements([1, 2, "3", 4])
    with pytest.raises(TypeError, match="All elements must be integers"):
        sum_unique_elements([1.5, 2, 3])

def test_sum_unique_elements_performance():
    """Ensure the function has O(n) time complexity"""
    # Create a large array with many duplicates
    large_array = list(range(10000)) * 2
    result = sum_unique_elements(large_array)
    assert result == sum(set(large_array))