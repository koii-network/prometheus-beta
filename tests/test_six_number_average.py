import pytest
from src.six_number_average import calculate_six_number_average

def test_basic_case():
    """Test a basic scenario with mixed positive numbers"""
    numbers = [1, 2, 3, 4, 5, 6]
    assert calculate_six_number_average(numbers) == 3.5

def test_negative_numbers():
    """Test with a mix of negative and positive numbers"""
    numbers = [-3, -2, -1, 1, 2, 3]
    assert calculate_six_number_average(numbers) == 0

def test_floating_point_numbers():
    """Test with floating point numbers"""
    numbers = [1.5, 2.5, 3.5, 4.5, 5.5, 6.5]
    assert calculate_six_number_average(numbers) == 4.5

def test_input_validation():
    """Test that the function raises ValueError for incorrect number of inputs"""
    with pytest.raises(ValueError, match="Input must be a list of exactly six numbers"):
        calculate_six_number_average([1, 2, 3, 4, 5])
    
    with pytest.raises(ValueError, match="Input must be a list of exactly six numbers"):
        calculate_six_number_average([1, 2, 3, 4, 5, 6, 7])

def test_large_numbers():
    """Test with large numbers"""
    numbers = [1000, 2000, 3000, 4000, 5000, 6000]
    assert calculate_six_number_average(numbers) == 3500