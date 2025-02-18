import pytest
from src.string_validator import is_numeric_string

def test_numeric_string_only_digits():
    """Test strings containing only digits."""
    assert is_numeric_string('12345') is True
    assert is_numeric_string('0') is True
    assert is_numeric_string('9876543210') is True

def test_numeric_string_with_non_digits():
    """Test strings with non-digit characters."""
    assert is_numeric_string('123.45') is False
    assert is_numeric_string('-123') is False
    assert is_numeric_string('12a34') is False
    assert is_numeric_string('') is False
    assert is_numeric_string(' ') is False
    assert is_numeric_string('   ') is False
    assert is_numeric_string('1 2 3') is False

def test_numeric_string_edge_cases():
    """Test edge cases."""
    assert is_numeric_string(str(2**63 - 1)) is True
    assert is_numeric_string('0' * 100) is True