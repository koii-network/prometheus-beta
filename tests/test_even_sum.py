import pytest
from src.even_sum import sum_positive_even_numbers

def test_sum_positive_even_numbers():
    """Test sum of positive even numbers in various scenarios."""
    # Basic case with mixed positive and negative numbers
    assert sum_positive_even_numbers([1, 2, 3, 4, 5, 6]) == 12
    
    # Case with negative numbers
    assert sum_positive_even_numbers([-1, -2, 1, 3, 4, 6]) == 10
    
    # Case with no even numbers
    assert sum_positive_even_numbers([1, 3, 5]) == 0
    
    # Case with empty list
    assert sum_positive_even_numbers([]) == 0
    
    # Case with only negative numbers
    assert sum_positive_even_numbers([-1, -2, -3, -4]) == 0
    
    # Case with large numbers
    assert sum_positive_even_numbers([1000, 2000, -3000, 4000]) == 7000

def test_input_types():
    """Test function behavior with different input types."""
    # Test with float inputs (should work for int-convertible floats)
    assert sum_positive_even_numbers([1.0, 2.0, 3.0, 4.0]) == 6
    
    # Test with mixed number types
    assert sum_positive_even_numbers([1, 2.0, 3, 4.0, -5]) == 6

def test_error_handling():
    """Test error handling for invalid inputs."""
    # Test with non-numeric input
    with pytest.raises(TypeError):
        sum_positive_even_numbers(['a', 'b', 'c'])
    
    # Test with None input
    with pytest.raises(TypeError):
        sum_positive_even_numbers(None)