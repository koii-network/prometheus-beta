import pytest
from src.palindrome_mirror import create_palindrome_mirror

def test_basic_string():
    """Test basic string palindrome mirror creation."""
    assert create_palindrome_mirror("hello") == "helloolleh"
    assert create_palindrome_mirror("world") == "worlddlrow"

def test_numbers():
    """Test palindrome mirror with numeric strings."""
    assert create_palindrome_mirror("12345") == "123454321"
    assert create_palindrome_mirror("0") == "00"

def test_special_characters():
    """Test palindrome mirror with special characters and spaces."""
    assert create_palindrome_mirror("A man, a plan!") == "A man, a plan!!nalp a ,nam A"
    assert create_palindrome_mirror("!@#$%") == "!@#$%$%#@!"

def test_empty_string():
    """Test palindrome mirror with empty string."""
    assert create_palindrome_mirror("") == ""

def test_non_string_input():
    """Test palindrome mirror with non-string inputs."""
    assert create_palindrome_mirror(42) == "4242"
    assert create_palindrome_mirror(3.14) == "3.143.14"
    assert create_palindrome_mirror(True) == "Truetrue"