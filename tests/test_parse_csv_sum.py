import pytest
from src.parse_csv_sum import parse_csv_sum

def test_parse_csv_sum_basic():
    """Test basic comma-separated sum functionality"""
    assert parse_csv_sum("1,2,3") == 6

def test_parse_csv_sum_with_spaces():
    """Test sum with spaces between numbers"""
    assert parse_csv_sum("1, 2, 3") == 6

def test_parse_csv_sum_single_number():
    """Test sum with a single number"""
    assert parse_csv_sum("42") == 42

def test_parse_csv_sum_empty_string():
    """Test sum with an empty string"""
    assert parse_csv_sum("") == 0

def test_parse_csv_sum_large_numbers():
    """Test sum with large numbers"""
    assert parse_csv_sum("1000000,2000000,3000000") == 6000000

def test_parse_csv_sum_negative_numbers():
    """Test sum with negative numbers"""
    assert parse_csv_sum("-1,2,-3") == -2

def test_parse_csv_sum_invalid_input():
    """Test error handling for invalid input"""
    with pytest.raises(ValueError):
        parse_csv_sum("1,2,a")
    
    with pytest.raises(ValueError):
        parse_csv_sum("1,2,")
    
    with pytest.raises(ValueError):
        parse_csv_sum("1.5,2,3")