import pytest
from src.alternating_path_case import convert_to_alternating_path_case

def test_convert_to_alternating_path_case_basic():
    assert convert_to_alternating_path_case("hello world") == "hello-WORLD"
    assert convert_to_alternating_path_case("python is awesome") == "python-IS-awesome"

def test_convert_to_alternating_path_case_single_word():
    assert convert_to_alternating_path_case("hello") == "hello"

def test_convert_to_alternating_path_case_empty_string():
    assert convert_to_alternating_path_case("") == ""

def test_convert_to_alternating_path_case_multiple_words():
    assert convert_to_alternating_path_case("a b c d e") == "a-B-c-D-e"

def test_convert_to_alternating_path_case_error_handling():
    with pytest.raises(TypeError):
        convert_to_alternating_path_case(123)
    
    with pytest.raises(TypeError):
        convert_to_alternating_path_case(None)

def test_convert_to_alternating_path_case_edge_cases():
    assert convert_to_alternating_path_case(" ") == ""
    assert convert_to_alternating_path_case("   multiple   spaces   ") == "multiple-SPACES"