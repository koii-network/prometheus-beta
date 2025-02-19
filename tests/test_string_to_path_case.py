import pytest
from src.string_to_path_case import string_to_path_case

def test_basic_string_conversion():
    assert string_to_path_case("Hello World") == "hello-world"

def test_mixed_case_string():
    assert string_to_path_case("HelloWorld") == "hello-world"

def test_string_with_special_characters():
    assert string_to_path_case("Hello, World!") == "hello-world"

def test_string_with_multiple_special_characters():
    assert string_to_path_case("Hello   World!!!") == "hello-world"

def test_empty_string():
    assert string_to_path_case("") == ""

def test_string_with_numbers():
    assert string_to_path_case("Hello 123 World") == "hello-123-world"

def test_input_type_error():
    with pytest.raises(TypeError):
        string_to_path_case(123)

def test_string_with_existing_hyphens():
    assert string_to_path_case("Hello-World Test") == "hello-world-test"

def test_string_with_mixed_punctuation():
    assert string_to_path_case("Hello_World Test@Case") == "hello-world-test-case"