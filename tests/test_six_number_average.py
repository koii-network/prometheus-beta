import pytest
from src.six_number_average import calculate_small_large_average

def test_calculate_small_large_average_standard_case():
    """Test with a standard set of numbers"""
    numbers = [1, 2, 3, 4, 5, 6]
    result = calculate_small_large_average(numbers)
    assert result == 3.5  # (1+2+3)/3 + (4+5+6)/3) / 2 = 3.5

def test_calculate_small_large_average_unsorted():
    """Test with an unsorted list of numbers"""
    numbers = [6, 2, 1, 5, 3, 4]
    result = calculate_small_large_average(numbers)
    assert result == 3.5

def test_calculate_small_large_average_negative_numbers():
    """Test with negative numbers"""
    numbers = [-1, -2, -3, 1, 2, 3]
    result = calculate_small_large_average(numbers)
    assert result == 0

def test_calculate_small_large_average_floating_point():
    """Test with floating point numbers"""
    numbers = [1.5, 2.5, 3.5, 4.5, 5.5, 6.5]
    result = calculate_small_large_average(numbers)
    assert pytest.approx(result, 4.5)

def test_calculate_small_large_average_invalid_input():
    """Test that function raises ValueError for incorrect number of inputs"""
    with pytest.raises(ValueError, match="Input must contain exactly six numbers"):
        calculate_small_large_average([1, 2, 3, 4, 5])
    
    with pytest.raises(ValueError, match="Input must contain exactly six numbers"):
        calculate_small_large_average([1, 2, 3, 4, 5, 6, 7])