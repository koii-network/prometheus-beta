import pytest
from src.palindrome_mirror import palindrome_mirror

def test_palindrome_mirror_basic():
    """Test basic string palindrome mirror creation."""
    assert palindrome_mirror("hello") == "helloolleh"
    assert palindrome_mirror("python") == "pythonnohtyp"

def test_palindrome_mirror_empty_string():
    """Test palindrome mirror with an empty string."""
    assert palindrome_mirror("") == ""

def test_palindrome_mirror_single_character():
    """Test palindrome mirror with a single character."""
    assert palindrome_mirror("a") == "aa"

def test_palindrome_mirror_numbers():
    """Test palindrome mirror with numbers."""
    assert palindrome_mirror("123") == "123321"

def test_palindrome_mirror_special_characters():
    """Test palindrome mirror with special characters."""
    assert palindrome_mirror("!@#") == "!@#@#!"

def test_palindrome_mirror_spaces():
    """Test palindrome mirror with spaces."""
    assert palindrome_mirror("a b c") == "a b ca b c"

def test_palindrome_mirror_mixed_input():
    """Test palindrome mirror with mixed characters."""
    result = palindrome_mirror("Hello, World! 123")
    assert result == "Hello, World! 123321 !dlroW ,olleH"

def test_palindrome_mirror_type_error():
    """Test that a TypeError is raised for non-string inputs."""
    with pytest.raises(TypeError, match="Input must be a string"):
        palindrome_mirror(123)
    with pytest.raises(TypeError, match="Input must be a string"):
        palindrome_mirror(None)