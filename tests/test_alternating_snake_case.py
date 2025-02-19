import pytest
from src.alternating_snake_case import to_alternating_snake_case

def test_basic_string_conversion():
    assert to_alternating_snake_case("hello world") == "hello_world"
    assert to_alternating_snake_case("python is awesome") == "python_is_awesome"

def test_already_snake_case():
    assert to_alternating_snake_case("snake_case_string") == "snakecase_string"

def test_mixed_case():
    assert to_alternating_snake_case("Hello World") == "hello_world"

def test_empty_string():
    assert to_alternating_snake_case("") == ""

def test_single_word():
    assert to_alternating_snake_case("hello") == "hello"

def test_multiple_words():
    assert to_alternating_snake_case("one two three four") == "one_two_three_four"

def test_invalid_input():
    with pytest.raises(TypeError):
        to_alternating_snake_case(123)
    
    with pytest.raises(TypeError):
        to_alternating_snake_case(None)

def test_with_hyphenated_input():
    assert to_alternating_snake_case("hello-world test") == "helloworld_test"