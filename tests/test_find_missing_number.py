import pytest
from src.find_missing_number import find_missing_number

def test_find_missing_number_normal_case():
    """Test finding a missing number in a normal scenario."""
    assert find_missing_number([1, 3, 4, 5]) == 2

def test_find_missing_number_first_missing():
    """Test when the first number is missing."""
    assert find_missing_number([2, 3, 4, 5]) == 1

def test_find_missing_number_last_missing():
    """Test when the last number is missing."""
    assert find_missing_number([1, 2, 3, 4]) == 5

def test_find_missing_number_large_range():
    """Test with a larger range of numbers."""
    assert find_missing_number([1, 2, 4, 5, 6, 7, 8, 9, 10]) == 3

def test_find_missing_number_invalid_input():
    """Test error handling for invalid inputs."""
    with pytest.raises(ValueError):
        find_missing_number([])
    
    with pytest.raises(ValueError):
        find_missing_number(None)

def test_find_missing_number_single_element():
    """Test with a single-element list where 1 is not the missing number."""
    assert find_missing_number([2]) == 1