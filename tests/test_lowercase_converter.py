import pytest
from src.lowercase_converter import convert_to_lowercase_with_spaces

def test_convert_to_lowercase_with_spaces_normal_case():
    assert convert_to_lowercase_with_spaces("Hello World") == "hello world"

def test_convert_to_lowercase_with_spaces_already_lowercase():
    assert convert_to_lowercase_with_spaces("hello world") == "hello world"

def test_convert_to_lowercase_with_spaces_mixed_case():
    assert convert_to_lowercase_with_spaces("HeLLo WoRLD") == "hello world"

def test_convert_to_lowercase_with_spaces_empty_string():
    assert convert_to_lowercase_with_spaces("") == ""

def test_convert_to_lowercase_with_spaces_only_spaces():
    assert convert_to_lowercase_with_spaces("   ") == "   "

def test_convert_to_lowercase_with_spaces_invalid_input():
    with pytest.raises(TypeError):
        convert_to_lowercase_with_spaces(123)
    with pytest.raises(TypeError):
        convert_to_lowercase_with_spaces(None)