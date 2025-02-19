import pytest
from src.string_converter import to_header_case

def test_to_header_case_normal_string():
    assert to_header_case("hello world") == "HelloWorld"
    assert to_header_case("python is awesome") == "PythonIsAwesome"

def test_to_header_case_with_punctuation():
    assert to_header_case("hello, world!") == "HelloWorld"
    assert to_header_case("python's is great") == "PythonSIsGreat"

def test_to_header_case_mixed_case():
    assert to_header_case("hElLo wOrLd") == "HelloWorld"

def test_to_header_case_empty_string():
    assert to_header_case("") == ""
    assert to_header_case("   ") == ""

def test_to_header_case_single_word():
    assert to_header_case("python") == "Python"

def test_to_header_case_error_handling():
    with pytest.raises(TypeError):
        to_header_case(None)
    with pytest.raises(TypeError):
        to_header_case(123)
    with pytest.raises(TypeError):
        to_header_case(["hello"])