import pytest
from src.alternating_path_case import convert_to_alternating_path_case

def test_convert_to_alternating_path_case():
    # Test basic conversion
    assert convert_to_alternating_path_case("hello world") == "hello-World"
    assert convert_to_alternating_path_case("PYTHON PROGRAMMING") == "python-Programming"
    assert convert_to_alternating_path_case("test STRING conversion") == "test-String-Conversion"

def test_single_word():
    assert convert_to_alternating_path_case("hello") == "hello"

def test_empty_string():
    assert convert_to_alternating_path_case("") == ""

def test_multiple_words():
    assert convert_to_alternating_path_case("one two three four") == "one-Two-Three-Four"

def test_invalid_input():
    with pytest.raises(TypeError):
        convert_to_alternating_path_case(123)
    with pytest.raises(TypeError):
        convert_to_alternating_path_case(None)