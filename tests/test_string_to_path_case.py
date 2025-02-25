import pytest
from src.string_to_path_case import to_path_case

def test_basic_conversion():
    assert to_path_case("Hello World") == "hello/world"
    assert to_path_case("Python Programming") == "python/programming"

def test_mixed_case():
    assert to_path_case("PythonProgramming") == "pythonprogramming"
    assert to_path_case("Python_Programming") == "python/programming"

def test_special_characters():
    assert to_path_case("Hello, World!") == "hello/world"
    assert to_path_case("Test@123 Case") == "test/123/case"

def test_numbers():
    assert to_path_case("123 Test Case") == "123/test/case"

def test_empty_string():
    assert to_path_case("") == ""

def test_multiple_spaces():
    assert to_path_case("Hello   World") == "hello/world"

def test_error_handling():
    with pytest.raises(TypeError):
        to_path_case(123)
    with pytest.raises(TypeError):
        to_path_case(None)

def test_edge_cases():
    assert to_path_case(" ") == ""
    assert to_path_case("!@#$%^&*()") == ""