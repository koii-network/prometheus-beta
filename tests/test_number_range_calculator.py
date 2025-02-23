import pytest
import sys
import io
from src.number_range_calculator import calculate_number_range

def test_basic_range_calculation(capsys):
    """Test basic range calculation with positive integers"""
    result = calculate_number_range("1,5,3,9")
    captured = capsys.readouterr()
    assert result == 8  # 9 - 1 = 8
    
def test_single_number(capsys):
    """Test with a single number"""
    result = calculate_number_range("7")
    captured = capsys.readouterr()
    assert result == 0  # Single number has zero range
    
def test_negative_numbers(capsys):
    """Test range calculation with negative numbers"""
    result = calculate_number_range("-10,5,0,15")
    captured = capsys.readouterr()
    assert result == 25  # 15 - (-10) = 25
    
def test_whitespace_handling(capsys):
    """Test handling of whitespace in input"""
    result = calculate_number_range(" 1 , 5 , 3 , 9 ")
    captured = capsys.readouterr()
    assert result == 8  # Should work with extra whitespace
    
def test_empty_string_raises_error():
    """Test that empty string raises a ValueError"""
    with pytest.raises(ValueError, match="Input string is empty"):
        calculate_number_range("")
        
def test_invalid_input_raises_error():
    """Test that non-integer input raises a ValueError"""
    with pytest.raises(ValueError, match="invalid literal"):
        calculate_number_range("1,2,three,4")