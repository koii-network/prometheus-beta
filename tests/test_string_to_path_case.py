import pytest
from src.string_to_path_case import convert_to_path_case

def test_convert_to_path_case_basic():
    assert convert_to_path_case("Hello World") == "hello/world"
    assert convert_to_path_case("some_string") == "some/string"
    assert convert_to_path_case("Mixed Case String") == "mixed/case/string"

def test_convert_to_path_case_multiple_separators():
    assert convert_to_path_case("Hello   World") == "hello/world"
    assert convert_to_path_case("Hello__World") == "hello/world"
    assert convert_to_path_case("Hello World_Test") == "hello/world/test"

def test_convert_to_path_case_leading_trailing_spaces():
    assert convert_to_path_case("  Hello World  ") == "hello/world"
    assert convert_to_path_case("  extra   spaces  ") == "extra/spaces"

def test_convert_to_path_case_edge_cases():
    assert convert_to_path_case("") == ""
    assert convert_to_path_case("   ") == ""

def test_convert_to_path_case_error_handling():
    with pytest.raises(TypeError):
        convert_to_path_case(123)
    with pytest.raises(TypeError):
        convert_to_path_case(None)

def test_convert_to_path_case_mixed_separators():
    assert convert_to_path_case("Hello_World Test") == "hello/world/test"
    assert convert_to_path_case("some/path/example") == "some/path/example"