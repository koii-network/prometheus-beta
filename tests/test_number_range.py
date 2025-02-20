import pytest
from src.number_range import find_number_range_difference

def test_basic_difference(capsys):
    """Test basic functionality with positive integers"""
    result = find_number_range_difference("1,5,3,9")
    assert result == 8
    captured = capsys.readouterr()
    assert captured.out.strip() == "8"

def test_single_number(capsys):
    """Test with a single number"""
    result = find_number_range_difference("7")
    assert result == 0
    captured = capsys.readouterr()
    assert captured.out.strip() == "0"

def test_negative_numbers(capsys):
    """Test with negative numbers"""
    result = find_number_range_difference("-5,2,10,-10")
    assert result == 20
    captured = capsys.readouterr()
    assert captured.out.strip() == "20"

def test_with_whitespace(capsys):
    """Test with whitespace around numbers"""
    result = find_number_range_difference(" 1 , 5 , 3 , 9 ")
    assert result == 8
    captured = capsys.readouterr()
    assert captured.out.strip() == "8"

def test_empty_string_raises_error():
    """Test that empty string raises a ValueError"""
    with pytest.raises(ValueError, match="Input string is empty"):
        find_number_range_difference("")

def test_non_integer_raises_error():
    """Test that non-integer input raises a ValueError"""
    with pytest.raises(ValueError, match="Invalid input"):
        find_number_range_difference("1,2,three,4")