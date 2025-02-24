import pytest
from src.number_sum import sum_comma_separated_numbers

def test_basic_sum():
    """Test summing a simple comma-separated string of numbers."""
    assert sum_comma_separated_numbers("1,2,3") == 6

def test_single_number():
    """Test summing a single number."""
    assert sum_comma_separated_numbers("42") == 42

def test_empty_string():
    """Test handling of an empty string."""
    assert sum_comma_separated_numbers("") == 0

def test_numbers_with_spaces():
    """Test handling of numbers with spaces."""
    assert sum_comma_separated_numbers(" 1 , 2 , 3 ") == 6

def test_negative_numbers():
    """Test handling of negative numbers."""
    assert sum_comma_separated_numbers("-1,2,-3") == -2

def test_invalid_input():
    """Test that invalid input raises a ValueError."""
    with pytest.raises(ValueError, match="Input string must contain only integers and commas"):
        sum_comma_separated_numbers("1,2,a")

def test_invalid_input_extra_characters():
    """Test that input with extra non-numeric characters raises a ValueError."""
    with pytest.raises(ValueError, match="Input string must contain only integers and commas"):
        sum_comma_separated_numbers("1,2,3.14")