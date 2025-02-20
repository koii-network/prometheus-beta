import pytest
from src.missing_number import find_missing_number

def test_find_missing_number_basic():
    """Test finding a missing number in a simple sequence."""
    assert find_missing_number([1, 3, 4, 5]) == 2

def test_find_missing_number_start():
    """Test when the first number is missing."""
    assert find_missing_number([2, 3, 4, 5]) == 1

def test_find_missing_number_end():
    """Test when the last number is missing."""
    assert find_missing_number([1, 2, 3, 4]) == 5

def test_find_missing_number_large_sequence():
    """Test with a larger sequence."""
    nums = [x for x in range(1, 101) if x != 42]
    assert find_missing_number(nums) == 42

def test_invalid_input_empty_list():
    """Test handling of an empty list."""
    with pytest.raises(ValueError):
        find_missing_number([])

def test_invalid_input_negative_numbers():
    """Test handling of negative numbers."""
    with pytest.raises(ValueError):
        find_missing_number([1, 2, -3, 4])

def test_invalid_input_non_integers():
    """Test handling of non-integer inputs."""
    with pytest.raises(ValueError):
        find_missing_number([1, 2, 'a', 4])