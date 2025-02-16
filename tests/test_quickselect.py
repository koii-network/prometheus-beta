import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from quickselect import quickselect

def test_quickselect_normal_cases():
    """Test quickselect with normal input arrays"""
    assert quickselect([3, 1, 4, 1, 5, 9, 2, 6, 5], 3) == 2
    assert quickselect([7, 10, 4, 3, 20, 15], 3) == 7
    assert quickselect([1, 2, 3, 4, 5], 1) == 1
    assert quickselect([1, 2, 3, 4, 5], 5) == 5

def test_quickselect_with_duplicates():
    """Test quickselect with arrays containing duplicate elements"""
    assert quickselect([3, 3, 3, 3, 3], 3) == 3
    assert quickselect([1, 2, 2, 3, 3, 4], 4) == 3

def test_quickselect_large_range():
    """Test quickselect with a large range of numbers"""
    large_list = list(range(1000, 0, -1))
    assert quickselect(large_list, 500) == 501

def test_quickselect_error_cases():
    """Test error handling for invalid inputs"""
    with pytest.raises(ValueError, match="Input array cannot be empty"):
        quickselect([], 1)
    
    with pytest.raises(ValueError, match="k must be between 1 and"):
        quickselect([1, 2, 3], 0)
    
    with pytest.raises(ValueError, match="k must be between 1 and"):
        quickselect([1, 2, 3], 4)

def test_quickselect_single_element():
    """Test quickselect with a single-element array"""
    assert quickselect([42], 1) == 42