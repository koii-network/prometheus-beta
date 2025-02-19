import pytest
from src.palindrome_mirror import create_palindrome_mirror

def test_basic_string_palindrome_mirror():
    """Test palindrome mirror for a basic string."""
    assert create_palindrome_mirror("hello") == "helloolleh"

def test_number_string_palindrome_mirror():
    """Test palindrome mirror for a string with numbers."""
    assert create_palindrome_mirror("12345") == "1234554321"

def test_space_string_palindrome_mirror():
    """Test palindrome mirror for a string with spaces."""
    assert create_palindrome_mirror("a b c") == "a b cc b a"

def test_special_character_palindrome_mirror():
    """Test palindrome mirror for a string with special characters."""
    assert create_palindrome_mirror("hello@123") == "hello@123321@olleh"

def test_empty_string_palindrome_mirror():
    """Test palindrome mirror for an empty string."""
    assert create_palindrome_mirror("") == ""

def test_single_character_palindrome_mirror():
    """Test palindrome mirror for a single character."""
    assert create_palindrome_mirror("a") == "aa"

def test_invalid_input_type():
    """Test that a TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        create_palindrome_mirror(12345)
        create_palindrome_mirror(None)
        create_palindrome_mirror(["hello"])