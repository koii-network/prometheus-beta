import pytest
from src.string_converter import convert_to_kebab_case

def test_convert_to_kebab_case_basic():
    assert convert_to_kebab_case("Hello World") == "hello-world"
    assert convert_to_kebab_case("Python Programming") == "python-programming"

def test_convert_to_kebab_case_mixed_cases():
    assert convert_to_kebab_case("HelloWorld") == "hello-world"
    assert convert_to_kebab_case("PythonProgramming") == "python-programming"

def test_convert_to_kebab_case_with_special_chars():
    assert convert_to_kebab_case("Hello, World!") == "hello-world"
    assert convert_to_kebab_case("Python_Programming.Language") == "python-programming-language"

def test_convert_to_kebab_case_with_multiple_spaces():
    assert convert_to_kebab_case("  Hello   World  ") == "hello-world"

def test_convert_to_kebab_case_edge_cases():
    assert convert_to_kebab_case("") == ""
    assert convert_to_kebab_case("   ") == ""

def test_convert_to_kebab_case_with_numbers():
    assert convert_to_kebab_case("Hello2World3") == "hello2-world3"

def test_convert_to_kebab_case_type_error():
    with pytest.raises(TypeError):
        convert_to_kebab_case(None)
    with pytest.raises(TypeError):
        convert_to_kebab_case(123)
    with pytest.raises(TypeError):
        convert_to_kebab_case(["Hello", "World"])