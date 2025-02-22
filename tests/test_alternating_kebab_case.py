import pytest
from src.alternating_kebab_case import alternating_kebab_case

def test_alternating_kebab_case_basic():
    assert alternating_kebab_case("hello world") == "Hello-world"
    assert alternating_kebab_case("python is awesome") == "Python-is-awesome"

def test_alternating_kebab_case_empty_string():
    assert alternating_kebab_case("") == ""

def test_alternating_kebab_case_single_word():
    assert alternating_kebab_case("hello") == "Hello"

def test_alternating_kebab_case_multiple_words():
    assert alternating_kebab_case("one two three four") == "One-two-three-four"

def test_alternating_kebab_case_mixed_case():
    assert alternating_kebab_case("HeLLo WoRLd") == "Hello-world"

def test_alternating_kebab_case_whitespace():
    assert alternating_kebab_case("  hello   world  ") == "Hello-world"