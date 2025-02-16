import pytest
from src.string_case_converter import convert_to_alternate_path_case

def test_convert_to_alternate_path_case_basic():
    assert convert_to_alternate_path_case("hello world python") == "hello-WORLD-python"

def test_convert_to_alternate_path_case_single_word():
    assert convert_to_alternate_path_case("hello") == "hello"

def test_convert_to_alternate_path_case_empty_string():
    assert convert_to_alternate_path_case("") == ""

def test_convert_to_alternate_path_case_multiple_words():
    assert convert_to_alternate_path_case("one two three four five") == "one-TWO-three-FOUR-five"

def test_convert_to_alternate_path_case_invalid_input():
    with pytest.raises(TypeError):
        convert_to_alternate_path_case(123)
    with pytest.raises(TypeError):
        convert_to_alternate_path_case(None)