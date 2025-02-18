import pytest
from src.string_utils import to_title_case

def test_to_title_case_basic():
    assert to_title_case("hello world") == "Hello World"

def test_to_title_case_already_capitalized():
    assert to_title_case("Hello World") == "Hello World"

def test_to_title_case_mixed_case():
    assert to_title_case("hElLo wOrLd") == "Hello World"

def test_to_title_case_empty_string():
    assert to_title_case("") == ""

def test_to_title_case_single_word():
    assert to_title_case("python") == "Python"

def test_to_title_case_multiple_spaces():
    assert to_title_case("  hello   world  ") == "Hello World"

def test_to_title_case_invalid_input():
    with pytest.raises(TypeError):
        to_title_case(123)
    
    with pytest.raises(TypeError):
        to_title_case(None)