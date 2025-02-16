import pytest
from src.alternating_kebab_case import to_alternating_kebab_case

def test_to_alternating_kebab_case_basic():
    assert to_alternating_kebab_case("hello world python") == "hello-WORLD-python"

def test_to_alternating_kebab_case_single_word():
    assert to_alternating_kebab_case("hello") == "hello"

def test_to_alternating_kebab_case_multiple_words():
    assert to_alternating_kebab_case("this is a test string") == "this-IS-a-TEST-string"

def test_to_alternating_kebab_case_empty_string():
    assert to_alternating_kebab_case("") == ""

def test_to_alternating_kebab_case_with_special_chars():
    assert to_alternating_kebab_case("hello, world! python?") == "hello-WORLD-python"

def test_to_alternating_kebab_case_invalid_input():
    with pytest.raises(TypeError):
        to_alternating_kebab_case(123)
    with pytest.raises(TypeError):
        to_alternating_kebab_case(None)