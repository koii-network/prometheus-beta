import pytest
from src.alternating_path_case import to_alternating_path_case

def test_basic_conversion():
    assert to_alternating_path_case("hello world") == "hello-World"
    assert to_alternating_path_case("python programming") == "python-Programming"

def test_single_word():
    assert to_alternating_path_case("hello") == "hello"

def test_multiple_words():
    assert to_alternating_path_case("this is a test") == "this-Is-A-Test"

def test_empty_string():
    assert to_alternating_path_case("") == ""

def test_whitespace_string():
    assert to_alternating_path_case("   ") == ""

def test_mixed_case_input():
    assert to_alternating_path_case("HeLLo WoRLd") == "hello-World"

def test_numeric_and_special_chars():
    assert to_alternating_path_case("hello 42 world!") == "hello-42-World!"