import pytest
import random
from src.sponge_case import to_sponge_case

def test_sponge_case_basic():
    # Set a fixed seed for consistent randomization in this test
    random.seed(42)
    result = to_sponge_case("hello world")
    assert result.lower() == "hello world".lower()
    assert result != "hello world"

def test_sponge_case_empty_string():
    random.seed(42)
    result = to_sponge_case("")
    assert result == ""

def test_sponge_case_single_character():
    random.seed(42)
    result = to_sponge_case("a")
    assert result.lower() == "a"

def test_sponge_case_non_string_input():
    with pytest.raises(TypeError):
        to_sponge_case(123)
    with pytest.raises(TypeError):
        to_sponge_case(None)

def test_sponge_case_preserves_non_alphabetic_characters():
    random.seed(42)
    result = to_sponge_case("hello, world! 123")
    assert result.replace(',', ',').replace('!', '!').replace(' ', ' ').isalpha() == False
    assert result.lower() == "hello, world! 123".lower()