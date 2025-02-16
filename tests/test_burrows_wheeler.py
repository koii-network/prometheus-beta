import pytest
from src.burrows_wheeler import burrows_wheeler_transform

def test_simple_burrows_wheeler_transform():
    # Test a simple string
    result, index = burrows_wheeler_transform("banana")
    assert result == "annb$aa"
    assert index == 4

def test_empty_string_raises_error():
    # Test empty string raises ValueError
    with pytest.raises(ValueError, match="Input string cannot be empty"):
        burrows_wheeler_transform("")

def test_non_string_input_raises_error():
    # Test non-string input raises TypeError
    with pytest.raises(TypeError, match="Input must be a string"):
        burrows_wheeler_transform(123)

def test_single_character_string():
    # Test single character string
    result, index = burrows_wheeler_transform("a")
    assert result == "a$"
    assert index == 1

def test_repeated_characters():
    # Test string with repeated characters
    result, index = burrows_wheeler_transform("mississippi")
    assert len(result) == len("mississippi") + 1
    assert '$' in result

def test_special_characters():
    # Test string with special characters
    result, index = burrows_wheeler_transform("hello, world!")
    assert len(result) == len("hello, world!") + 1
    assert '$' in result