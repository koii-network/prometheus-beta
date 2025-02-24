import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from array_average import calculate_mixed_avg

def test_basic_calculation():
    """Test with a standard set of numbers"""
    numbers = [1, 2, 3, 4, 5, 6]
    assert calculate_mixed_avg(numbers) == 3.5

def test_negative_numbers():
    """Test with negative numbers"""
    numbers = [-1, -2, -3, 4, 5, 6]
    assert calculate_mixed_avg(numbers) == 2.5

def test_floating_point_numbers():
    """Test with floating point numbers"""
    numbers = [1.5, 2.5, 3.5, 4.5, 5.5, 6.5]
    assert calculate_mixed_avg(numbers) == 4.5

def test_error_less_than_six_numbers():
    """Test error handling for less than 6 numbers"""
    with pytest.raises(ValueError, match="Input must be a list of exactly 6 numbers"):
        calculate_mixed_avg([1, 2, 3, 4, 5])

def test_error_more_than_six_numbers():
    """Test error handling for more than 6 numbers"""
    with pytest.raises(ValueError, match="Input must be a list of exactly 6 numbers"):
        calculate_mixed_avg([1, 2, 3, 4, 5, 6, 7])

def test_identical_numbers():
    """Test with identical numbers"""
    numbers = [2, 2, 2, 2, 2, 2]
    assert calculate_mixed_avg(numbers) == 2.0