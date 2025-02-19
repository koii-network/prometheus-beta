import pytest
from src.alternating_title_case import alternating_title_case

def test_alternating_title_case_normal():
    assert alternating_title_case("hello world python coding") == "Hello world Python coding"

def test_alternating_title_case_single_word():
    assert alternating_title_case("hello") == "Hello"

def test_alternating_title_case_empty_string():
    assert alternating_title_case("") == ""

def test_alternating_title_case_multiple_words():
    assert alternating_title_case("this is a test of alternating case") == "This is A test OF alternating CASE"

def test_alternating_title_case_invalid_input():
    with pytest.raises(TypeError):
        alternating_title_case(123)

def test_alternating_title_case_with_mixed_case():
    assert alternating_title_case("HELLO world PYTHON programming") == "Hello world Python programming"