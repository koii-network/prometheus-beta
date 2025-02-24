import pytest
from src.integer_parser import parse_and_sort_integers

def test_basic_comma_separated_integers():
    """Test parsing and sorting basic comma-separated integers."""
    assert parse_and_sort_integers("3,1,4,2") == [1, 2, 3, 4]

def test_string_with_spaces():
    """Test parsing integers with spaces."""
    assert parse_and_sort_integers(" 3 , 1 , 4 , 2 ") == [1, 2, 3, 4]

def test_string_with_non_integer_characters():
    """Test parsing integers with non-integer characters."""
    assert parse_and_sort_integers("3a,1b,4c,2d") == [1, 2, 3, 4]

def test_empty_string():
    """Test parsing an empty string."""
    assert parse_and_sort_integers("") == []

def test_string_with_no_valid_integers():
    """Test a string with no valid integers."""
    assert parse_and_sort_integers("abc,def,ghi") == []

def test_mixed_valid_and_invalid_input():
    """Test a mix of valid and invalid input."""
    assert parse_and_sort_integers("10,abc,20,def,30") == [10, 20, 30]

def test_large_numbers():
    """Test parsing and sorting large integers."""
    assert parse_and_sort_integers("1000000,500000,2000000") == [500000, 1000000, 2000000]