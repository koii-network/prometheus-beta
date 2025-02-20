import pytest
from src.number_range import calculate_number_range

def test_basic_number_range():
    """Test basic functionality with positive numbers"""
    assert calculate_number_range("1,5,3,9") == 8  # 9 - 1 = 8

def test_negative_numbers():
    """Test range calculation with negative numbers"""
    assert calculate_number_range("-10,5,0,3") == 15  # 5 - (-10) = 15

def test_single_number():
    """Test with a single number"""
    assert calculate_number_range("42") == 0  # Difference with itself is 0

def test_large_numbers():
    """Test with large numbers"""
    assert calculate_number_range("1000,5000,2500") == 4000  # 5000 - 1000 = 4000

def test_empty_string_raises_error():
    """Test that an empty string raises a ValueError"""
    with pytest.raises(ValueError, match="Input string must contain at least one number"):
        calculate_number_range("")

def test_non_integer_input_raises_error():
    """Test that non-integer input raises a ValueError"""
    with pytest.raises(ValueError, match="Input must be a string of comma-separated integers"):
        calculate_number_range("1,2,three,4")

def test_whitespace_handling():
    """Test that whitespace is handled correctly"""
    assert calculate_number_range(" 1 , 5 , 3 , 9 ") == 8