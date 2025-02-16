import pytest
from src.alternating_kebab_case import to_alternating_kebab_case

def test_basic_conversion():
    assert to_alternating_kebab_case("hello world") == "hello-WORLD"
    assert to_alternating_kebab_case("python is awesome") == "python-IS-awesome"

def test_mixed_case_input():
    assert to_alternating_kebab_case("Hello World") == "hello-WORLD"
    assert to_alternating_kebab_case("PythON is GreAT") == "python-IS-great"

def test_special_characters():
    assert to_alternating_kebab_case("hello@world!") == "hello-WORLD"
    assert to_alternating_kebab_case("python, programming") == "python-PROGRAMMING"

def test_single_word():
    assert to_alternating_kebab_case("hello") == "hello"
    assert to_alternating_kebab_case("WORLD") == "world"

def test_empty_string():
    assert to_alternating_kebab_case("") == ""

def test_whitespace_only():
    assert to_alternating_kebab_case("   ") == ""

def test_error_handling():
    with pytest.raises(TypeError):
        to_alternating_kebab_case(123)
    
    with pytest.raises(TypeError):
        to_alternating_kebab_case(None)