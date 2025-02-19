import pytest
from src.palindrome_mirror import create_palindrome_mirror

def test_basic_palindrome_mirror():
    assert create_palindrome_mirror('hello') == 'helloolleh'
    assert create_palindrome_mirror('123') == '123321'

def test_empty_string():
    assert create_palindrome_mirror('') == ''

def test_single_character():
    assert create_palindrome_mirror('a') == 'aa'

def test_special_characters():
    assert create_palindrome_mirror('hi!') == 'hi!!ih'

def test_spaces():
    assert create_palindrome_mirror('a b c') == 'a b ca b c'

def test_non_string_input():
    with pytest.raises(TypeError, match="Input must be a string"):
        create_palindrome_mirror(123)
        create_palindrome_mirror(None)