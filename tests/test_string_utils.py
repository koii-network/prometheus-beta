import pytest
from src.string_utils import to_header_case

def test_to_header_case_basic():
    assert to_header_case("hello world") == "Hello World"

def test_to_header_case_hyphen():
    assert to_header_case("hello-world") == "Hello World"

def test_to_header_case_underscore():
    assert to_header_case("hello_world") == "Hello World"

def test_to_header_case_dot():
    assert to_header_case("hello.world") == "Hello World"

def test_to_header_case_mixed_separators():
    assert to_header_case("hello-world_test.case") == "Hello World Test Case"

def test_to_header_case_empty_string():
    assert to_header_case("") == ""

def test_to_header_case_single_word():
    assert to_header_case("hello") == "Hello"

def test_to_header_case_already_header_case():
    assert to_header_case("Hello World") == "Hello World"

def test_to_header_case_with_numbers():
    assert to_header_case("hello2world") == "Hello2world"

def test_to_header_case_with_extra_spaces():
    assert to_header_case("  hello   world  ") == "Hello World"