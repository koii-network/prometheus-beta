import pytest
from src.alternating_path_case import to_alternating_path_case

def test_alternating_path_case_basic():
    assert to_alternating_path_case("hello world") == "hello-WORLD"
    assert to_alternating_path_case("python programming language") == "python-PROGRAMMING-language"

def test_alternating_path_case_with_separators():
    assert to_alternating_path_case("hello_world") == "hello-WORLD"
    assert to_alternating_path_case("python-programming-language") == "python-PROGRAMMING-language"

def test_alternating_path_case_empty_input():
    assert to_alternating_path_case("") == ""

def test_alternating_path_case_single_word():
    assert to_alternating_path_case("hello") == "hello"

def test_alternating_path_case_error_handling():
    with pytest.raises(TypeError):
        to_alternating_path_case(123)
    with pytest.raises(TypeError):
        to_alternating_path_case(None)