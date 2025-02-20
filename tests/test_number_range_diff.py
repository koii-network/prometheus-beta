import pytest
from src.number_range_diff import calculate_number_range_diff

def test_basic_number_range_diff():
    """Test basic functionality with positive integers"""
    assert calculate_number_range_diff("1,5,3,9") == 8

def test_negative_numbers():
    """Test with negative numbers"""
    assert calculate_number_range_diff("-1,5,-10,3") == 15

def test_mixed_numbers():
    """Test with mixed positive and negative numbers"""
    assert calculate_number_range_diff("-5,0,5,10") == 15

def test_single_number():
    """Test with a single number"""
    assert calculate_number_range_diff("7") == 0

def test_whitespace_handling():
    """Test with whitespace in the input string"""
    assert calculate_number_range_diff(" 1 , 5 , 3 , 9 ") == 8

def test_empty_string_raises_error():
    """Test that an empty string raises a ValueError"""
    with pytest.raises(ValueError, match="Input string cannot be empty"):
        calculate_number_range_diff("")

def test_non_integer_input_raises_error():
    """Test that non-integer input raises a ValueError"""
    with pytest.raises(ValueError, match="Input must be a comma-separated string of integers"):
        calculate_number_range_diff("1,2,a,4")