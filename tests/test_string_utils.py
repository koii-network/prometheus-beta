import pytest
from src.string_utils import to_title_case

def test_to_title_case_basic():
    assert to_title_case("hello world") == "Hello World"
    assert to_title_case("PYTHON PROGRAMMING") == "Python Programming"

def test_to_title_case_with_hyphens():
    assert to_title_case("python-programming-language") == "Python-Programming-Language"

def test_to_title_case_edge_cases():
    assert to_title_case("") == ""
    assert to_title_case("a") == "A"
    assert to_title_case("A") == "A"

def test_to_title_case_error_handling():
    with pytest.raises(TypeError):
        to_title_case(123)
    with pytest.raises(TypeError):
        to_title_case(None)