import pytest
from src.list_analysis import analyze_list_numbers

def test_mixed_numbers():
    """Test a list with mixed even and odd numbers."""
    result = analyze_list_numbers([1, 2, 3, 4, 5, 6])
    assert result == (12, 3)

def test_all_even_numbers():
    """Test a list with only even numbers."""
    result = analyze_list_numbers([2, 4, 6, 8])
    assert result == (20, 0)

def test_all_odd_numbers():
    """Test a list with only odd numbers."""
    result = analyze_list_numbers([1, 3, 5, 7])
    assert result == (0, 4)

def test_empty_list():
    """Test an empty list."""
    result = analyze_list_numbers([])
    assert result == (0, 0)

def test_negative_numbers():
    """Test a list with negative numbers."""
    result = analyze_list_numbers([-1, -2, -3, -4, -5, -6])
    assert result == (-12, 3)

def test_mixed_negative_and_positive():
    """Test a list with mixed negative and positive numbers."""
    result = analyze_list_numbers([-1, 2, -3, 4, -5, 6])
    assert result == (12, 3)

def test_float_numbers():
    """Test a list with floating point numbers."""
    result = analyze_list_numbers([1.5, 2.0, 3.3, 4.0, 5.7, 6.0])
    assert result == (12.0, 3)

def test_invalid_input_non_list():
    """Test that a TypeError is raised for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        analyze_list_numbers("not a list")

def test_invalid_input_non_numeric():
    """Test that a TypeError is raised for list with non-numeric elements."""
    with pytest.raises(TypeError, match="All list elements must be numeric"):
        analyze_list_numbers([1, 2, "three", 4])