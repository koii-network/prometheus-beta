import pytest
from src.string_utils import convert_to_uppercase_with_spaces

def test_basic_conversion():
    assert convert_to_uppercase_with_spaces("helloWorld") == "HELLO WORLD"
    assert convert_to_uppercase_with_spaces("convertToUpperCase") == "CONVERT TO UPPER CASE"

def test_already_spaced_string():
    assert convert_to_uppercase_with_spaces("hello world") == "HELLO WORLD"

def test_single_word():
    assert convert_to_uppercase_with_spaces("hello") == "HELLO"

def test_multiple_uppercase_letters():
    assert convert_to_uppercase_with_spaces("HelloWorldTest") == "HELLO WORLD TEST"

def test_empty_string():
    assert convert_to_uppercase_with_spaces("") == ""

def test_invalid_input():
    with pytest.raises(TypeError):
        convert_to_uppercase_with_spaces(123)
    
    with pytest.raises(TypeError):
        convert_to_uppercase_with_spaces(None)