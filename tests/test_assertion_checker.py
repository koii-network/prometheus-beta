import pytest
from src.assertion_checker import check_conditions

def test_valid_input():
    """Test with valid input within default range"""
    assert check_conditions([50, 75, 25]) == True

def test_valid_input_with_custom_range():
    """Test with valid input and custom range"""
    assert check_conditions([10, 20, 30], min_value=5, max_value=35) == True

def test_empty_list_raises_error():
    """Test that empty list raises an AssertionError"""
    with pytest.raises(AssertionError, match="List cannot be empty"):
        check_conditions([])

def test_non_list_input_raises_error():
    """Test that non-list input raises an AssertionError"""
    with pytest.raises(AssertionError, match="Input must be a list"):
        check_conditions("not a list")

def test_non_numeric_input_raises_error():
    """Test that non-numeric input raises an AssertionError"""
    with pytest.raises(AssertionError, match="Invalid type"):
        check_conditions([1, 2, "three"])

def test_out_of_range_input_raises_error():
    """Test that out of range input raises an AssertionError"""
    with pytest.raises(AssertionError, match="Value 150 is out of range"):
        check_conditions([50, 100, 150])

def test_out_of_range_with_custom_range():
    """Test out of range input with custom range"""
    with pytest.raises(AssertionError, match="Value 40 is out of range"):
        check_conditions([10, 20, 40], min_value=0, max_value=30)