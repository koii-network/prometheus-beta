import pytest
from src.string_converter import convert_to_uppercase

def test_convert_to_uppercase_basic():
    assert convert_to_uppercase("hello") == "HELLO"
    assert convert_to_uppercase("world") == "WORLD"

def test_convert_to_uppercase_mixed_case():
    assert convert_to_uppercase("HeLLo WoRLd") == "HELLO WORLD"

def test_convert_to_uppercase_empty_string():
    assert convert_to_uppercase("") == ""

def test_convert_to_uppercase_with_numbers_and_symbols():
    assert convert_to_uppercase("hello123!@#") == "HELLO123!@#"

def test_convert_to_uppercase_invalid_input():
    with pytest.raises(TypeError):
        convert_to_uppercase(123)
    
    with pytest.raises(TypeError):
        convert_to_uppercase(None)