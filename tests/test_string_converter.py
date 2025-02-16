import pytest
from src.string_converter import convert_to_alternating_snake_case

def test_convert_to_alternating_snake_case_basic():
    assert convert_to_alternating_snake_case("hello world") == "hello_WORLD"
    assert convert_to_alternating_snake_case("python is awesome") == "python_IS_awesome"

def test_convert_to_alternating_snake_case_mixed_case():
    assert convert_to_alternating_snake_case("PyThOn CoDeS") == "python_CODES"

def test_convert_to_alternating_snake_case_special_chars():
    assert convert_to_alternating_snake_case("hello, world!") == "hello_WORLD"
    assert convert_to_alternating_snake_case("python 3.9") == "python_THREE"

def test_convert_to_alternating_snake_case_empty_string():
    assert convert_to_alternating_snake_case("") == ""

def test_convert_to_alternating_snake_case_single_word():
    assert convert_to_alternating_snake_case("python") == "python"

def test_convert_to_alternating_snake_case_error_handling():
    with pytest.raises(TypeError):
        convert_to_alternating_snake_case(123)
    with pytest.raises(TypeError):
        convert_to_alternating_snake_case(None)