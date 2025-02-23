import pytest
from src.csv_integer_parser import parse_and_sort_csv_integers

def test_basic_parsing_and_sorting():
    """Test basic comma-separated integer parsing and sorting."""
    assert parse_and_sort_csv_integers("3,1,4,1,5,9") == [1, 1, 3, 4, 5, 9]

def test_with_non_integer_characters():
    """Test handling of strings with non-integer characters."""
    assert parse_and_sort_csv_integers("10,abc,20,def,30") == [10, 20, 30]

def test_empty_string():
    """Test handling of empty string."""
    assert parse_and_sort_csv_integers("") == []

def test_whitespace_handling():
    """Test handling of whitespace around integers."""
    assert parse_and_sort_csv_integers(" 5 , 2 , 8 ") == [2, 5, 8]

def test_negative_integers():
    """Test handling of negative integers."""
    assert parse_and_sort_csv_integers("-3,1,-5,2") == [-5, -3, 1, 2]

def test_mixed_valid_invalid_input():
    """Test mixture of valid and invalid input."""
    assert parse_and_sort_csv_integers("10,abc,20,def,30,!@#") == [10, 20, 30]

def test_no_valid_integers():
    """Test input with no valid integers."""
    assert parse_and_sort_csv_integers("abc,def,!@#") == []

def test_none_input():
    """Test handling of None input."""
    assert parse_and_sort_csv_integers(None) == []