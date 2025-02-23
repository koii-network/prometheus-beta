import pytest
from src.alternating_camel_case import to_alternating_camel_case

def test_basic_conversion():
    assert to_alternating_camel_case("hello world") == "helloWorld"
    assert to_alternating_camel_case("python programming") == "pythonProgramming"

def test_uppercase_input():
    assert to_alternating_camel_case("PYTHON IS AWESOME") == "pythonIsAwesome"

def test_mixed_case_input():
    assert to_alternating_camel_case("Python-Programming-Language") == "pythonProgrammingLanguage"

def test_special_characters():
    assert to_alternating_camel_case("hello, world!") == "helloWorld"
    assert to_alternating_camel_case("python__programming") == "pythonProgramming"

def test_single_word():
    assert to_alternating_camel_case("hello") == "hello"
    assert to_alternating_camel_case("HELLO") == "hello"

def test_empty_string():
    assert to_alternating_camel_case("") == ""

def test_only_special_characters():
    assert to_alternating_camel_case("!!!") == ""

def test_error_handling():
    with pytest.raises(TypeError):
        to_alternating_camel_case(123)
    
    with pytest.raises(TypeError):
        to_alternating_camel_case(None)

def test_multiple_spaces():
    assert to_alternating_camel_case("hello   world") == "helloWorld"