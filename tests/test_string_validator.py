import pytest
from src.string_validator import is_numeric_string

def test_valid_numeric_string():
    """Test that strings with only digits return True."""
    assert is_numeric_string("12345") == True
    assert is_numeric_string("0") == True
    assert is_numeric_string("9876543210") == True

def test_invalid_numeric_string():
    """Test that strings with non-digit characters return False."""
    assert is_numeric_string("123abc") == False
    assert is_numeric_string("12.34") == False
    assert is_numeric_string("-123") == False
    assert is_numeric_string(" 123") == False
    assert is_numeric_string("123 ") == False

def test_empty_string():
    """Test that an empty string returns False."""
    assert is_numeric_string("") == False

def test_type_error():
    """Test that non-string inputs raise a TypeError."""
    with pytest.raises(TypeError, match="Input must be a string"):
        is_numeric_string(12345)
    with pytest.raises(TypeError, match="Input must be a string"):
        is_numeric_string(None)
    with pytest.raises(TypeError, match="Input must be a string"):
        is_numeric_string(["123"])