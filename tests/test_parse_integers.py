import pytest
from src.parse_integers import parse_and_sort_integers

def test_basic_integer_parsing():
    """Test basic comma-separated integer parsing."""
    assert parse_and_sort_integers("1,2,3") == [1, 2, 3]

def test_parsing_with_non_integer_characters():
    """Test parsing when input contains non-integer characters."""
    assert parse_and_sort_integers("10,5,abc2,3def") == [2, 3, 5, 10]

def test_empty_string():
    """Test handling of empty string."""
    assert parse_and_sort_integers("") == []

def test_mixed_integers_with_spaces():
    """Test parsing with spaces and mixed integers."""
    assert parse_and_sort_integers(" 1 , 20 , 3 ") == [1, 3, 20]

def test_repeated_integers():
    """Test parsing with repeated integers."""
    assert parse_and_sort_integers("5,5,3,3,1") == [1, 3, 3, 5, 5]

def test_large_integers():
    """Test parsing large integers."""
    assert parse_and_sort_integers("1000000,1,500") == [1, 500, 1000000]

def test_no_valid_integers():
    """Test case with no valid integers."""
    assert parse_and_sort_integers("abc,def,ghi") == []