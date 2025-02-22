import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from median_of_medians import median_of_medians

def test_median_of_medians_basic():
    """Test basic functionality with different list sizes"""
    # Odd number of elements
    assert median_of_medians([1, 3, 5, 7, 9]) == 5
    assert median_of_medians([9, 7, 5, 3, 1]) == 5
    
    # Even number of elements (should return the lower of the two middle values)
    assert median_of_medians([1, 2, 3, 4]) == 2

def test_median_of_medians_large_list():
    """Test with a larger list of unsorted integers"""
    large_list = [42, 15, 23, 8, 16, 4, 99, 50, 33, 11, 77, 62]
    assert median_of_medians(large_list) == 33

def test_median_of_medians_duplicate_elements():
    """Test with lists containing duplicate elements"""
    assert median_of_medians([5, 5, 5, 5, 5]) == 5
    assert median_of_medians([1, 2, 2, 3, 3, 3, 4, 4, 5]) == 3

def test_median_of_medians_negative_numbers():
    """Test with negative numbers"""
    assert median_of_medians([-5, -3, -1, 0, 2, 4, 6]) == 0

def test_median_of_medians_single_element():
    """Test with a single element list"""
    assert median_of_medians([42]) == 42

def test_median_of_medians_empty_list():
    """Test that an empty list raises a ValueError"""
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        median_of_medians([])

def test_median_of_medians_floating_point():
    """Test with floating point numbers"""
    assert median_of_medians([1.5, 2.3, 0.7, 4.1, 3.6]) == 2.3

def test_median_of_medians_performance():
    """Simple performance sanity check"""
    import random
    
    # Large list of random integers
    large_list = random.sample(range(1, 10000), 1000)
    result = median_of_medians(large_list)
    
    # Verify the result is an element from the list
    assert result in large_list