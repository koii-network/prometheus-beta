import pytest
from src.palindrome_mirror import create_palindrome_mirror

def test_basic_string():
    """Test palindrome mirror with a basic string."""
    assert create_palindrome_mirror("hello") == "helloolleh"

def test_empty_string():
    """Test palindrome mirror with an empty string."""
    assert create_palindrome_mirror("") == ""

def test_single_character():
    """Test palindrome mirror with a single character."""
    assert create_palindrome_mirror("a") == "aa"

def test_with_numbers():
    """Test palindrome mirror with numbers."""
    assert create_palindrome_mirror("123") == "123321"

def test_with_special_characters():
    """Test palindrome mirror with special characters."""
    assert create_palindrome_mirror("a1!") == "a1!!1a"

def test_with_spaces():
    """Test palindrome mirror with spaces."""
    assert create_palindrome_mirror("hello world") == "hello world dlrow olleh"

def test_invalid_input_type():
    """Test that TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        create_palindrome_mirror(123)
        create_palindrome_mirror(None)
        create_palindrome_mirror(["hello"])