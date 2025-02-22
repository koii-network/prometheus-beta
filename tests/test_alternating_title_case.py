import pytest
from src.alternating_title_case import alternating_title_case

def test_alternating_title_case_basic():
    assert alternating_title_case("hello world python") == "Hello world Python"

def test_alternating_title_case_multiple_words():
    assert alternating_title_case("this is a test string") == "This is A test String"

def test_alternating_title_case_single_word():
    assert alternating_title_case("hello") == "Hello"

def test_alternating_title_case_empty_string():
    assert alternating_title_case("") == ""

def test_alternating_title_case_type_error():
    with pytest.raises(TypeError):
        alternating_title_case(123)

def test_alternating_title_case_mixed_case():
    assert alternating_title_case("HELLO world PYTHON test") == "Hello world Python test"