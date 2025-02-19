import pytest
from src.palindrome_mirror import create_palindrome_mirror

def test_basic_palindrome_mirror():
    """Test basic string palindrome mirror creation"""
    assert create_palindrome_mirror("hello") == "helloolleh"
    assert create_palindrome_mirror("world") == "worlddlrow"

def test_alphanumeric_palindrome_mirror():
    """Test palindrome mirror with numbers and characters"""
    assert create_palindrome_mirror("A1B2") == "A1B2B2A1"
    assert create_palindrome_mirror("123") == "123321"

def test_special_characters_and_spaces():
    """Test palindrome mirror with special characters and spaces"""
    assert create_palindrome_mirror("race a car") == "race a carrac a ecar"
    assert create_palindrome_mirror("Hi, World!") == "Hi, World!!dlroW ,iH"

def test_empty_string():
    """Test palindrome mirror with an empty string"""
    assert create_palindrome_mirror("") == ""

def test_single_character():
    """Test palindrome mirror with a single character"""
    assert create_palindrome_mirror("a") == "aa"

def test_invalid_input_type():
    """Test that TypeError is raised for non-string inputs"""
    with pytest.raises(TypeError, match="Input must be a string"):
        create_palindrome_mirror(123)
    with pytest.raises(TypeError, match="Input must be a string"):
        create_palindrome_mirror(None)