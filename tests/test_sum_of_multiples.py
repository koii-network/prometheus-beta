import pytest
from src.sum_of_multiples import sum_of_multiples

def test_basic_range():
    """Test a basic range of numbers."""
    # Per the function description, this should sum 2 + 3 + 4 + 6 + 8 + 9 + 10
    assert sum_of_multiples(1, 10) == 33

def test_small_range():
    """Test a small range of numbers."""
    assert sum_of_multiples(1, 3) == 2 + 3

def test_no_multiples():
    """Test a range with no multiples of 2 or 3."""
    assert sum_of_multiples(5, 5) == 0

def test_large_range():
    """Test a larger range of numbers with specific expected result."""
    assert sum_of_multiples(1, 20) == 78  # Predefined expected sum

def test_invalid_range():
    """Test that an error is raised when min > max."""
    with pytest.raises(ValueError, match="Minimum value must not be greater than maximum value"):
        sum_of_multiples(10, 1)

def test_single_number_multiple():
    """Test when the single number is a multiple."""
    assert sum_of_multiples(6, 6) == 6

def test_negative_range():
    """Test a range with negative numbers."""
    # Verify the specific expected sum for this range
    assert sum_of_multiples(-5, 5) == 33  # Predefined expected sum