import pytest
from src.find_missing_number import find_missing_number

def test_missing_number_in_middle():
    """Test finding a missing number in the middle of the sequence."""
    assert find_missing_number([1, 3, 4, 5]) == 2

def test_missing_first_number():
    """Test finding the first number is missing."""
    assert find_missing_number([2, 3, 4, 5, 6]) == 1

def test_missing_last_number():
    """Test finding the last number is missing."""
    assert find_missing_number([1, 2, 3, 4, 5]) == 6

def test_invalid_input_empty_list():
    """Test that an empty list raises a ValueError."""
    with pytest.raises(ValueError, match="Input must be a non-empty list of integers"):
        find_missing_number([])

def test_invalid_input_none():
    """Test that None input raises a ValueError."""
    with pytest.raises(ValueError, match="Input must be a non-empty list of integers"):
        find_missing_number(None)

def test_large_sequence():
    """Test a larger sequence with a missing number."""
    large_list = list(range(1, 101))
    large_list.remove(42)
    assert find_missing_number(large_list) == 42

def test_small_sequence():
    """Test a small sequence of numbers."""
    assert find_missing_number([2]) == 1

@pytest.mark.parametrize("invalid_input", [
    "not a list", 
    123, 
    [1, "string", 3], 
    [1.5, 2, 3]
])
def test_invalid_input_type(invalid_input):
    """Test various invalid input types."""
    with pytest.raises(ValueError, match="Input must be a non-empty list of integers"):
        find_missing_number(invalid_input)