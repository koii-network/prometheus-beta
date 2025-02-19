import pytest
from src.alternating_snake_case import convert_to_alternating_snake_case

def test_convert_to_alternating_snake_case_basic():
    assert convert_to_alternating_snake_case("hello world") == "hello_WORLD"
    assert convert_to_alternating_snake_case("python is awesome") == "python_IS_awesome"

def test_convert_to_alternating_snake_case_mixed_case():
    assert convert_to_alternating_snake_case("Python Is Great") == "python_IS_great"
    assert convert_to_alternating_snake_case("HELLO world TEST") == "hello_WORLD_test"

def test_convert_to_alternating_snake_case_existing_snake_case():
    assert convert_to_alternating_snake_case("hello_world") == "hello_WORLD"
    assert convert_to_alternating_snake_case("python_is_fun") == "python_IS_fun"

def test_convert_to_alternating_snake_case_empty_string():
    assert convert_to_alternating_snake_case("") == ""

def test_convert_to_alternating_snake_case_single_word():
    assert convert_to_alternating_snake_case("hello") == "hello"

def test_convert_to_alternating_snake_case_invalid_input():
    with pytest.raises(TypeError):
        convert_to_alternating_snake_case(None)
    with pytest.raises(TypeError):
        convert_to_alternating_snake_case(123)