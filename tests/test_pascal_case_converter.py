import pytest
from src.pascal_case_converter import to_pascal_case

def test_to_pascal_case_basic_words():
    assert to_pascal_case("hello world") == "HelloWorld"
    assert to_pascal_case("user name") == "UserName"

def test_to_pascal_case_with_underscores():
    assert to_pascal_case("user_name") == "UserName"
    assert to_pascal_case("first_last_name") == "FirstLastName"

def test_to_pascal_case_with_hyphens():
    assert to_pascal_case("hello-world") == "HelloWorld"
    assert to_pascal_case("user-profile") == "UserProfile"

def test_to_pascal_case_with_mixed_separators():
    assert to_pascal_case("hello_world-test") == "HelloWorldTest"
    assert to_pascal_case("user name_profile") == "UserNameProfile"

def test_to_pascal_case_empty_string():
    assert to_pascal_case("") == ""

def test_to_pascal_case_single_word():
    assert to_pascal_case("hello") == "Hello"

def test_to_pascal_case_with_special_characters():
    assert to_pascal_case("hello@world") == "HelloWorld"
    assert to_pascal_case("user#name") == "UserName"

def test_to_pascal_case_with_numbers():
    assert to_pascal_case("user123name") == "User123Name"
    assert to_pascal_case("hello_world_2023") == "HelloWorld2023"