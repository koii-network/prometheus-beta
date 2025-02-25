import pytest
from src.integer_sorter import sort_csv_integers

def test_basic_sorting():
    """Test basic comma-separated integer sorting."""
    assert sort_csv_integers("5,2,8,1") == [1, 2, 5, 8]

def test_with_whitespace():
    """Test sorting with whitespace around numbers."""
    assert sort_csv_integers(" 5 , 2 , 8 , 1 ") == [1, 2, 5, 8]

def test_with_non_numeric_characters():
    """Test handling of non-numeric characters."""
    assert sort_csv_integers("10abc, 20def, 30ghi") == [10, 20, 30]

def test_mixed_valid_invalid_inputs():
    """Test mixed valid and invalid inputs."""
    assert sort_csv_integers("10, invalid, 20, not a number, 30") == [10, 20, 30]

def test_empty_string():
    """Test empty string input."""
    assert sort_csv_integers("") == []

def test_no_valid_integers():
    """Test input with no valid integers."""
    assert sort_csv_integers("abc, def, ghi") == []

def test_repeated_numbers():
    """Test handling of repeated numbers."""
    assert sort_csv_integers("5,2,5,8,2,1") == [1, 2, 2, 5, 5, 8]