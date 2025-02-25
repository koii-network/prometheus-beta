import pytest
from src.advanced_string_reversal import advanced_string_reversal

def test_basic_reversal():
    """Test basic string reversal."""
    assert advanced_string_reversal("hello") == "olleh"

def test_palindrome_preservation():
    """Test that palindromes remain unchanged."""
    assert advanced_string_reversal("racecar") == "racecar"
    assert advanced_string_reversal("hello racecar world") == "olleh racecar dlrow"

def test_number_reversal():
    """Test reversal of numeric substrings."""
    assert advanced_string_reversal("123") == "321"
    assert advanced_string_reversal("hello 123 world") == "olleh 321 dlrow"

def test_mixed_string():
    """Test mixed string with words, numbers, and other characters."""
    assert advanced_string_reversal("hello 123 world") == "olleh 321 dlrow"
    assert advanced_string_reversal("a1b2c3") == "a1b2c3"

def test_special_characters():
    """Test strings with special characters."""
    assert advanced_string_reversal("hello, world!") == "olleh, dlrow!"
    assert advanced_string_reversal("123 abc 456") == "321 cba 654"

def test_error_handling():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError):
        advanced_string_reversal(123)
    with pytest.raises(TypeError):
        advanced_string_reversal(None)

def test_empty_string():
    """Test behavior with empty string."""
    assert advanced_string_reversal("") == ""

def test_complex_mixed_string():
    """Test a more complex mixed string."""
    assert advanced_string_reversal("a1 bob 22 racecar!") == "a1 bob 22 racecar!"