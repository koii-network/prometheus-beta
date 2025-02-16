import pytest
from src.alternating_header_case import to_alternating_header_case

def test_alternating_header_case_normal_input():
    assert to_alternating_header_case("hello world python") == "Hello world Python"

def test_alternating_header_case_empty_string():
    assert to_alternating_header_case("") == ""

def test_alternating_header_case_single_word():
    assert to_alternating_header_case("hello") == "Hello"

def test_alternating_header_case_multiple_words():
    assert to_alternating_header_case("this is a test string") == "This is A test String"

def test_alternating_header_case_already_mixed_case():
    assert to_alternating_header_case("HeLLo WoRLd") == "Hello world"

def test_alternating_header_case_invalid_input():
    with pytest.raises(TypeError):
        to_alternating_header_case(123)
    with pytest.raises(TypeError):
        to_alternating_header_case(None)