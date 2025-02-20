import pytest
from src.six_number_average import calculate_six_number_average

def test_six_number_average_standard_case():
    """Test with a standard set of numbers."""
    numbers = [1, 2, 3, 4, 5, 6]
    result = calculate_six_number_average(numbers)
    assert result == 3.5, f"Expected 3.5, but got {result}"

def test_six_number_average_unsorted():
    """Test with an unsorted set of numbers."""
    numbers = [6, 1, 5, 2, 4, 3]
    result = calculate_six_number_average(numbers)
    assert result == 3.5, f"Expected 3.5, but got {result}"

def test_six_number_average_negative_numbers():
    """Test with negative numbers."""
    numbers = [-1, -2, -3, 1, 2, 3]
    result = calculate_six_number_average(numbers)
    assert result == 0, f"Expected 0, but got {result}"

def test_six_number_average_floating_point():
    """Test with floating point numbers."""
    numbers = [1.5, 2.5, 3.5, 4.5, 5.5, 6.5]
    result = calculate_six_number_average(numbers)
    assert result == 4.0, f"Expected 4.0, but got {result}"

def test_six_number_average_invalid_input():
    """Test that an error is raised when not exactly 6 numbers are provided."""
    with pytest.raises(ValueError, match="Input must contain exactly 6 numbers"):
        calculate_six_number_average([1, 2, 3, 4, 5])
    
    with pytest.raises(ValueError, match="Input must contain exactly 6 numbers"):
        calculate_six_number_average([1, 2, 3, 4, 5, 6, 7])