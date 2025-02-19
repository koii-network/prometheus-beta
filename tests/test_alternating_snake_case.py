import pytest
from src.alternating_snake_case import convert_to_alternating_snake_case

def test_convert_to_alternating_snake_case_normal_case():
    assert convert_to_alternating_snake_case("hello world") == 'hello_WORLD'
    assert convert_to_alternating_snake_case("Python is AWESOME") == 'python_IS_awesome'

def test_convert_to_alternating_snake_case_single_word():
    assert convert_to_alternating_snake_case("hello") == 'hello'
    assert convert_to_alternating_snake_case("HELLO") == 'hello'

def test_convert_to_alternating_snake_case_multiple_words():
    assert convert_to_alternating_snake_case("one two three four") == 'one_TWO_three_FOUR'

def test_convert_to_alternating_snake_case_empty_string():
    assert convert_to_alternating_snake_case("") == ""

def test_convert_to_alternating_snake_case_invalid_input():
    with pytest.raises(TypeError):
        convert_to_alternating_snake_case(123)
    with pytest.raises(TypeError):
        convert_to_alternating_snake_case(None)