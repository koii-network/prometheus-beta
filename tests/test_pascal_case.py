import pytest
from src.pascal_case import to_pascal_case

def test_to_pascal_case_normal_cases():
    assert to_pascal_case("hello world") == "HelloWorld"
    assert to_pascal_case("python programming") == "PythonProgramming"
    assert to_pascal_case("convert to pascal case") == "ConvertToPascalCase"

def test_to_pascal_case_with_special_characters():
    assert to_pascal_case("hello-world") == "HelloWorld"
    assert to_pascal_case("python_programming") == "PythonProgramming"
    assert to_pascal_case("convert to_pascal-case") == "ConvertToPascalCase"

def test_to_pascal_case_edge_cases():
    assert to_pascal_case("") == ""
    assert to_pascal_case("a") == "A"
    assert to_pascal_case("123 abc") == "123Abc"

def test_to_pascal_case_error_handling():
    with pytest.raises(TypeError):
        to_pascal_case(123)
    with pytest.raises(TypeError):
        to_pascal_case(None)