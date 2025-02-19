import pytest
from src.palindrome_mirror import create_palindrome_mirror

def test_basic_string():
    assert create_palindrome_mirror("hello") == "helloolleh"

def test_empty_string():
    assert create_palindrome_mirror("") == ""

def test_single_character():
    assert create_palindrome_mirror("a") == "aa"

def test_with_numbers():
    assert create_palindrome_mirror("123") == "123321"

def test_with_special_characters():
    assert create_palindrome_mirror("!@#") == "!@##@!"

def test_with_spaces():
    assert create_palindrome_mirror("hello world") == "hello worlddlrow olleh"

def test_mixed_characters():
    assert create_palindrome_mirror("a1! b") == "a1! bb !1a"

def test_invalid_input():
    with pytest.raises(TypeError):
        create_palindrome_mirror(123)
    with pytest.raises(TypeError):
        create_palindrome_mirror(None)