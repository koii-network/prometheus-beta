import pytest
from src.number_utils import analyze_numbers

def test_analyze_numbers_mixed_list():
    """Test with a mixed list of even and odd numbers."""
    result = analyze_numbers([1, 2, 3, 4, 5, 6])
    assert result == (12, 3)  # even sum is 2+4+6=12, odd count is 3

def test_analyze_numbers_all_even():
    """Test with a list of only even numbers."""
    result = analyze_numbers([2, 4, 6, 8])
    assert result == (20, 0)  # even sum is 20, odd count is 0

def test_analyze_numbers_all_odd():
    """Test with a list of only odd numbers."""
    result = analyze_numbers([1, 3, 5, 7])
    assert result == (0, 4)  # even sum is 0, odd count is 4

def test_analyze_numbers_empty_list():
    """Test with an empty list."""
    result = analyze_numbers([])
    assert result == (0, 0)  # even sum and odd count are 0

def test_analyze_numbers_with_floats():
    """Test with a mix of integers and floats."""
    result = analyze_numbers([1.5, 2, 3.7, 4, 5])
    assert result == (6, 3)  # even sum is 2+4=6, odd count is 3

def test_analyze_numbers_invalid_input_type():
    """Test with an invalid input type."""
    with pytest.raises(TypeError, match="Input must be a list of numbers"):
        analyze_numbers("not a list")

def test_analyze_numbers_invalid_list_content():
    """Test with a list containing non-numeric elements."""
    with pytest.raises(ValueError, match="List must contain only numbers"):
        analyze_numbers([1, 2, "three", 4])