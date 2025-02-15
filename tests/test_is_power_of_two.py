import pytest
from src.is_power_of_two import is_power_of_two

def test_power_of_two_positive_cases():
    """Test various positive cases for powers of two."""
    powers_of_two = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
    for num in powers_of_two:
        assert is_power_of_two(num) is True

def test_non_power_of_two_cases():
    """Test cases that are not powers of two."""
    non_powers = [0, 3, 5, 6, 7, 9, 10, 12, 15, 17, 31, 33]
    for num in non_powers:
        assert is_power_of_two(num) is False

def test_negative_numbers():
    """Test that negative numbers return False."""
    negative_nums = [-1, -2, -4, -8, -16]
    for num in negative_nums:
        assert is_power_of_two(num) is False

def test_invalid_input_types():
    """Test that invalid input types raise TypeError."""
    invalid_inputs = [3.14, "16", [2], {2}, None]
    for invalid_input in invalid_inputs:
        with pytest.raises(TypeError):
            is_power_of_two(invalid_input)